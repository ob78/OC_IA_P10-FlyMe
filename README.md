# Welcome to Fly Me Bot !

This bot has been created using [Bot Framework](https://dev.botframework.com).

It does implement the following features :

- Use [LUIS](https://www.luis.ai) to implement core AI capabilities
- Implement a multi-turn conversation using Dialogs
- Handle user interruptions for such things as `Help` or `Cancel`
- Prompt for and validate requests for information from the user
- Use [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/cloudservices) to monitor your bot

### Overview

This bot uses [LUIS](https://www.luis.ai), an AI based cognitive service, to implement language understanding
and [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/cloudservices), an extensible Application Performance Management (APM) service for web developers on multiple platforms.

It can be used to book a travel with the following information :
- Origin
- Destination
- Start date
- End date
- Budget

## To try this sample

- Clone the repository
- In a terminal, navigate to the bot folder
- Activate your desired virtual environment
- In the terminal, type `pip install -r requirements.txt`
- Run your bot with `python app.py`

## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- You can test the bot using Bot Framework Emulator

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- File -> Open Bot
- Enter a Bot URL of `http://localhost:8000/api/messages`

## Deployment to Azure

The bot has been deployed to Azure.
