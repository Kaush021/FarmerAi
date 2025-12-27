from gtts import gTTS

def speak(text, filename="reply.mp3"):
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    return filename

