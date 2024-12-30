''' Executing this function initiates the application of emotin
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask
from flask import request, render_template
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("\emotionDetector")

@app.route("/emotionDetector")
def em_detector():
    """Sends text from the HTML form for analysis using the method in emotion_detection.py"""
    #Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    #Pass the text to the analyzer function
    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    #Check if label is None, indicating err or invalid response
    if anger_score is None:
        return "Invalid input ! Try again."
    #Return a formatted string with the outputs
    return f"For the given statement, the system response is: 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """Renders the webpage for entering Strings and viewing results."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
