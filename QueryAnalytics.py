from configparser import ConfigParser
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from json import dumps, loads
from prettytable import PrettyTable

def read_config(section):
	config_file = open('QueryAnalytics.ini', mode='r', encoding='utf-8')
	config = ConfigParser()
	config.readfp(config_file)
	config_file.close()
	if config.has_section(section) and config.has_option(section, 'AppID') and config.has_option(section, 'APIKey'):
		app_id = config.get(section, 'AppID')
		api_key = config.get(section, 'APIKey')
		return (app_id, api_key)

	raise ValueError('Invalid config')


def print_output(data):
	table = data['Tables'][0]
	print('\t'.join([c['ColumnName'] for c in table['Columns']]))
	for row in table['Rows']:
		print('\t'.join([str(r) for r in row]))


def execute_query(query, app_id, api_key):
	if not query:
		return

	query_url = 'https://api.applicationinsights.io/beta/apps/' + app_id + '/query'
	query_headers = {
		'X-Api-Key': api_key,
		'Content-Type': 'application/json; charset=utf-8'
	}

	try:
		query_json = dumps({'query': query})
		request = Request(query_url, data=bytes(query_json, encoding='utf-8'), headers=query_headers, method='POST')
		response = urlopen(request)
		output = loads(response.read())
		print_output(output)
	except HTTPError as e:
		print('Error:', e.msg)

def run_script(filename, app_id, api_key):
	file = open(filename, mode='r', encoding='utf-8')
	query = file.read().replace('\n', ' ')
	file.close()
	execute_query(query, app_id, api_key)


def run_interactive(app_id, api_key):
	query = ''
	print('> ', end='')
	while True:
		line = input().strip()
		if line:
			query += line + ' '
			print('- ', end='')
		else:
			execute_query(query, app_id, api_key)
			query = ''
			print('> ', end='')


def main():
	try:
		if len(argv) == 2:
			config_section = argv[1]
			(app_id, api_key) = read_config(config_section)
			run_interactive(app_id, api_key)
		elif len(argv) == 3:
			config_section = argv[1]
			script_filename = argv[2]
			(app_id, api_key) = read_config(config_section)
			run_script(script_filename, app_id, api_key)
		else:
			print('Usage: QueryAnalytics.py <config section> [script file]')
	except KeyboardInterrupt:
		pass
	except Exception as e:
		print('Error:', e.args[0])


if __name__ == '__main__':
	main()
