from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_template_html():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_handler():
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if (result['dominant_emotion'] == None):
        return "Invalid text! Please try again."
    return result, 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)