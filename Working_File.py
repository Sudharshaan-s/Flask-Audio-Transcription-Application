from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from pydub import AudioSegment
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            
            # Check the file extension and convert if necessary
            if file.filename.endswith(".mp3"):
                audio = AudioSegment.from_mp3(file)
                wav_io = io.BytesIO()
                audio.export(wav_io, format="wav")
                wav_io.seek(0)
                audio_file = sr.AudioFile(wav_io)
            else:
                audio_file = sr.AudioFile(file)
                
            with audio_file as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)