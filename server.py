from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():

    text_to_analyze=request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)
    domemo=response['dominant_emotion']
    
    
    if domemo is None:
        return "Invalid input! Try again."
    else:
        return "The given text the system response is {}. The dominant emotion is {}.".format( response, domemo)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
    

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
