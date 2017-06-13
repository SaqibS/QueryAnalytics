# Query Analytics

## Introduction

This script allows you to query [Microsoft Application Insights](https://docs.microsoft.com/en-us/azure/application-insights/app-insights-overview) using the custom [Analytics language](https://docs.microsoft.com/en-us/azure/application-insights/app-insights-analytics).

The "normal" way to query Analytics is using the web portal. Instead, this script lets you interactively type in queries at the terminal. You can also save queries in files, and execute at the command line.

## Interactive Usage

To query Analytics interactively, you must specify the configuration of the Application Insights instance to connect to. By default, a connection called "demo" is already configured, so just run:

```
python QueryAnalytics.py demo
```

A prompt will be displayed, indicated by the `>` character. When you press enter, a continuation prompt, `-`, will be displayed. Pressing enter on a blank line will cause the command to be executed.

```
> requests
- | count
-
Count
6898865
>
```

## Executing Saved Queries

The file `demo_query.txt` contains a simple query that can be executed - just provide it as the second command-line argument:

```
python QueryAnalytics.py demo demo_query.txt
```

## Configuration

All this is no use unless you can query your own data. The file QueryAnalytics.ini contains one section, corresponding to the "demo" connection. You can add similar sections for each of your Application Insights instances.

```
[demo]
AppID=DEMO_APP
APIKey=DEMO_KEY
```

[This article](https://dev.applicationinsights.io/documentation/Authorization/API-key-and-App-ID) explains how to get the app ID and API key for your Application Insights instance.

