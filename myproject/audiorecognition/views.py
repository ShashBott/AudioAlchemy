from django.shortcuts import render
import speech_recognition as sr

# Create your views here.
def transcribe_audio(request):
    if request.method == 'POST':
        if 'audio_file' in request.FILES:
            # Handle audio file upload
            audio_file = request.FILES['audio_file']
            recognizer = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
                
        elif 'use_microphone' in request.POST:
            # Handle speech from microphone
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak something...")
                audio_data = recognizer.listen(source)
                text = recognizer.recognize_google(audio_data)
        else:
            # Handle invalid request
            return render(request, 'audiorecognition/error.html', {'message': 'Invalid request'})

        return render(request, 'audiorecognition/result.html', {'text': text})
    else:
        return render(request, 'audiorecognition/upload.html')