"""
This module provides a Flask server for detecting emotions in text
using an external NLP service.
"""
from flask import Flask, request, jsonify
# pylint: disable=import-error
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Analyzes the text provided in the request arguments and returns 
    emotional scores and the dominant emotion.
    """
    # 1. Retrieve the 'textToAnalyze' parameter from the URL
    text_to_analyze = request.args.get('textToAnalyze')

    # 2. Check if the parameter was actually provided
    if not text_to_analyze:
        return jsonify({"message": "Invalid input! Please provide text."}), 400

    # 3. Call the emotion detection function
    response = emotion_detector(text_to_analyze)

    # 4. Extract the dominant emotion
    emotions = response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    # 5. Return a structured response
    return {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": dominant_emotion
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
