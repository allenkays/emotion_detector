import json
import requests


def emotion_detector(text_to_analyze):
    """
    Function to detect emotions from text.

    Input:
        text_to_analyze (str) : The text to be analyzed

    Returns:
        dict : Dictionary containing emotion scores and dominant emotion
               {
                   'anger': float or None,
                   'disgust': float or None,
                   'fear': float or None,
                   'joy': float or None,
                   'sadness': float or None,
                   'dominant_emotion': str or None
               }
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Handle empty input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers=header)

    # Handle API error (400)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Convert JSON response text into a dictionary
    response_dict = json.loads(response.text)

    # Extract emotions
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)

    # Determine dominant emotion
    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }
