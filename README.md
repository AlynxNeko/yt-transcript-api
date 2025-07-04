# 🎙️ YouTube Transcript API (Subproject)

A lightweight Flask API for retrieving YouTube video transcripts via [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/).

This project serves as a **backend submodule** required by the [YouTube to Document Converter](https://github.com/AlynxNeko/yt-transcriber) main app. It exposes a REST endpoint to fetch raw transcripts based on YouTube video IDs.

---

## 🚀 Features

- 🔍 Fetches transcript using only a video ID
- 📦 JSON output, ready for AI/GPT processing
- 🪶 Minimal dependencies, fast startup
- 🌐 Suitable for deployment on Vercel, Railway, or any basic PaaS

---

## 📡 Endpoints

### `GET /`

Health check

```bash
curl https://your-api.com/
```

Returns:
```
Transcript API is running.
```

---

### `GET /transcript/<video_id>`

Retrieve the transcript for a YouTube video

```
curl https://your-api.com/transcript/dQw4w9WgXcQ
```

Returns:

```
[
  { "text": "Never gonna give you up", "start": 3.52, "duration": 2.45 },
  ...
]
```

If the transcript is unavailable or an error occurs:

```
{ "error": "Transcripts are disabled for this video" }
```

---

## 🔧 Setup Instructions

1. Clone the repo
```bash
git clone https://github.com/your-org/yt-transcriber-api.git
cd yt-transcriber-api
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run locally
```bash
python app.py
```
Server will start on `http://localhost:5000`

---

## 🧪 Deployment Notes
- On platforms like Railway, it might not work because if blocked IP.
- The code uses `host="0.0.0.0"` to support external access.

---

## 🧱 Related Projects
- 🔗 Main App: [yt-transcriber](https://github.com/AlynxNeko/yt-transcriber)

---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## 🙋‍♂️ Author
AlynxNeko
[GitHub](https://github.com/AlynxNeko)