"""
Flask server for emotion detection.

This server exposes an endpoint `/emotionDetector` that analyzes user-provided
text and returns the probabilities of various emotions along with the dominant
emotion. It also handles invalid or blank inputs gracefully.
"""


from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
        Function renders the homepage
        
        Returns:
            homepage
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """
    This function renders the call to the emotion_detector function

    Returns:
        Dictionary response or None
    """
    # Handle GET (query params) and POST (form data)
    if request.method == "GET":
        text_to_analyze = request.args.get("textToAnalyze", "")
    else:  # POST
        text_to_analyze = request.form.get("text", "")

    result = emotion_detector(text_to_analyze)

    # Check if the analysis failed (dominant_emotion is None)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Extract emotions
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    # Format the response as requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8005)
