from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from config import DefaultConfig
from msrest.authentication import CognitiveServicesCredentials

CONFIG = DefaultConfig()


def test_greetings_intent():
    runtime_credentials = CognitiveServicesCredentials(CONFIG.LUIS_API_KEY)
    client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)

    test_request = "Hello"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "GreetingsIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent

    """
    client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)

    test_request = { "query" : "Hello" }
    test_response = client_runtime.prediction.get_slot_prediction(CONFIG.LUIS_APP_ID, "Production", test_request)

    expected_intent = "GreetingsIntent"
    actual_intent = test_response.prediction.top_intent

    assert actual_intent == expected_intent
    """

def test_none_intent():
    runtime_credentials = CognitiveServicesCredentials(CONFIG.LUIS_API_KEY)
    client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)

    test_request = "I want to rent a car"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "NoneIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent

    """
    runtime_credentials = CognitiveServicesCredentials(CONFIG.LUIS_API_KEY)
    client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)

    test_request = { "query" : "I want to rent a car" }
    test_response = client_runtime.prediction.get_slot_prediction(CONFIG.LUIS_APP_ID, "Production", test_request)

    expected_intent = "NoneIntent"
    actual_intent = test_response.prediction.top_intent

    assert actual_intent == expected_intent
    """

def test_order_travel_intent():
    runtime_credentials = CognitiveServicesCredentials(CONFIG.LUIS_API_KEY)
    client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)

    test_request = "I need to book a flight"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "OrderTravelIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent

    """
    runtime_credentials = CognitiveServicesCredentials(CONFIG.LUIS_API_KEY)
    client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)

    test_request = { "query" : "I need to book a flight" }
    test_response = client_runtime.prediction.get_slot_prediction(CONFIG.LUIS_APP_ID, "Production", test_request)

    expected_intent = "OrderTravelIntent"
    actual_intent = test_response.prediction.top_intent

    assert actual_intent == expected_intent
    """