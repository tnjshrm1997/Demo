import speech_recognition as spr
import librosa
import wave



from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("source/kl.wav" ,"wav") 
chunk_length_ms = 1000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Convert chunks to raw audio data which you can then feed to HTTP stream
for i, chunk in enumerate(chunks):
    raw_audio_data = chunk.raw_data
raw_audio = AudioSegment.from_file(raw_audio_data,format="raw",frame_rate=44100,channels=2,sample_width=2)

audio_segment.export(raw_audio ,format = "flac")

r = spr.Recognizer()

audio = 'kl.flac'

with spr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

    text = r.recognize_google(audio)
    print (text)
    
