''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request

# Import the emotion_detector function from the package
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and their
        various scores, as well as the dominant emotion.
    '''
    # Fetch text to analyze
    text_to_analyze = request.args.get("textToAnalyze")
    # Get prediction
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    # compose message to return
    message = f"""
    For the given statement, the system response is 'anger': {response['anger']},
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}
    and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.
    """
    return message

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

app.run(host="0.0.0.0", port=5000)
