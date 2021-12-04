#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    #WEB APP CONFIGURATION
    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    """
    LUIS_APP_ID = "fc967b69-b16b-4d66-9b82-760605b4381a"
    LUIS_API_KEY = "555aae1ebd3e4afa94366773c27ee427"
    LUIS_API_HOST_NAME = "westeurope.api.cognitive.microsoft.com"
    """
    
    #OK
    """
    LUIS_APP_ID = "fc967b69-b16b-4d66-9b82-760605b4381a"
    LUIS_API_KEY = "32ca343b80904445a7a9bdd1d4d784fa"
    LUIS_API_HOST_NAME = "francecentral.api.cognitive.microsoft.com"
	"""
    
    #LUIS APP CONFIGURATION
    #LUIS_APP_ID = "9ebbde08-519c-4741-8664-2597fc361871"
    LUIS_APP_ID = "52c42e40-1395-47e1-9fcb-d8e59de2d71b"
    LUIS_API_KEY = "87488d948aba4eb39f8986e82d88d0a2"
    LUIS_API_HOST_NAME = "francecentral.api.cognitive.microsoft.com"
    LUIS_API_ENDPOINT = "https://flyme-luis.cognitiveservices.azure.com/"
    
    #APP INSIGHTS CONFIGURATION 
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey", "bc43e9d0-ee04-471f-a00b-db18c00e73a0")
