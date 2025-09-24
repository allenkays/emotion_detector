import requests
import json


def emotion_detector(text_to_analyze):
    """
        Function to detect emotions from text

        input: str

        returns:
        dictionary object
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    if not text_to_analyze:
        return "Text cannot be empty. Please enter some text!"
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    return (response.text)

    """
    # Format the response to a dictionary of key value pairs with json
    formatted_response = json.loads(response.text)
    
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['emotionPredictions'][0]
        score = formatted_response['emotionPredictions'][label[0]]
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        #score = None
    
    return {'label': label, 'score': score}
    """
  