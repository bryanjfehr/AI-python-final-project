"""
This module sends text to the Watson EmotionPredict library for analysis and returns a String 
containing the data from the response.
"""
import requests  # Import the requests library to handle HTTP requests
import json #Import the JSON library

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
    formatted_response = json.loads(response.text)
    if response.status_code == 200:     # If text field is not blank, proceed with detection
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        # Use max() method to find the highest score
        dominant_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
        # Use a for loop to find the matching key value
        for match in formatted_response['emotionPredictions'][0]['emotion']:
            if formatted_response['emotionPredictions'][0]['emotion'][match] == dominant_score:
                dominant_emotion_name = match
        #Return the dictionary with the different emotion scores
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion_name
        }
    elif response.status_code == 400:       # If text field is blank return dictionary with None values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }