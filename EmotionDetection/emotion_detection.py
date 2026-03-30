# import json
# import requests

# def emotion_detector(text_to_analyze):
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     my_obj = { "raw_document": { "text": text_to_analyze } }

#     response = requests.post(url, json=my_obj, headers=header, timeout=10)

#     formatted_response = json.loads(response.text)
#     formatted_response = formatted_response["emotionPredictions"][0]
#     predicted_emotions = formatted_response["emotion"]
#     dominant_emotion = max(predicted_emotions, key=predicted_emotions.get)

#     predicted_emotions["dominant_emotion"] = dominant_emotion

#     return predicted_emotions

import re
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text using an external API.
    
    Args:
        text_to_analyze (str): The text to analyze.
        
    Returns:
        dict: A dictionary of predicted emotions with a 'dominant_emotion' key.
              If input is blank or server returns 400, all values are None.
    """
    # Handle blank input, too short input, or input with only numbers/symbols
    if (not text_to_analyze 
        or len(text_to_analyze.strip()) < 2 
        or re.fullmatch(r'[^a-zA-Z]+', text_to_analyze.strip())):
        return {k: None for k in ["joy","sadness","anger","fear","disgust","dominant_emotion"]}
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=my_obj, headers=header, timeout=10)

    # Handle server response
    if response.status_code == 400:
        # Invalid input (blank text or bad request)
        return {
            "joy": None,
            "sadness": None,
            "anger": None,
            "fear": None,
            "disgust": None,
            "surprise": None,
            "dominant_emotion": None
        }

    # Process valid response
    formatted_response = json.loads(response.text)
    formatted_response = formatted_response["emotionPredictions"][0]
    predicted_emotions = formatted_response["emotion"]
    dominant_emotion = max(predicted_emotions, key=predicted_emotions.get)
    predicted_emotions["dominant_emotion"] = dominant_emotion

    return predicted_emotions