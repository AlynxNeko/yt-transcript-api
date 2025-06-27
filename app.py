from flask import Flask, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Transcript API is running."

@app.route("/transcript/<video_id>")
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify(transcript)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🚨 THIS IS WHAT YOU WERE MISSING
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway injects this
    app.run(host="0.0.0.0", port=port)
