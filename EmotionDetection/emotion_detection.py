import requests
import json

def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = body, headers = headers)
    text_response = response.text
    formatted_response = json.loads(text_response)
    emotion_obj = formatted_response['emotionPredictions'][0]['emotion']
    dominant_key = max(emotion_obj, key=emotion_obj.get)
    emotion_obj['dominant_emotion'] = dominant_key
    return emotion_obj