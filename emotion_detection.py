"""
This module sends text to the Watson EmotionPredict library for analysis and returns a String 
containing the data from the response.
"""
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    """This module sends text to the Watson emotion detection AI library and returns the text"""
    # URL of the emotion detection library
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Define the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the required headers for the API service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the headers & text for analysis
    response = requests.post(url, json = myobj, headers=header)
    # Return the text part of the response object
    return response.text
