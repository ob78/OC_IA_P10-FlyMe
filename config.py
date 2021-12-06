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
    
    #LUIS APP CONFIGURATION
    LUIS_APP_ID = "52c42e40-1395-47e1-9fcb-d8e59de2d71b"
    LUIS_API_KEY = "87488d948aba4eb39f8986e82d88d0a2"
    LUIS_API_HOST_NAME = "francecentral.api.cognitive.microsoft.com"
    LUIS_API_ENDPOINT = "https://flyme-luis.cognitiveservices.azure.com/"
    
    #APP INSIGHTS CONFIGURATION 
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey", "bc43e9d0-ee04-471f-a00b-db18c00e73a0")
