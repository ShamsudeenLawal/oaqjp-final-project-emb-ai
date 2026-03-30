import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=my_obj, headers=header, timeout=10)
    
    formatted_response = json.loads(response.text)
    formatted_response = formatted_response["emotionPredictions"][0]
    predicted_emotions = formatted_response["emotion"]
    dominant_emotion = max(predicted_emotions, key=predicted_emotions.get)

    predicted_emotions["dominant_emotion"] = dominant_emotion

    return predicted_emotions
