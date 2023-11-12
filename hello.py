import gtts
from playsound import playsound

tts = gtts.gTTS( '感嘆詞', lang='ja' )  ##  request google to get synthesis

tts.save( 'hello.mp3' )  ##  save audio

# playsound is relying on another python subprocess. Please use `pip install pygobject` if you want playsound to run more efficiently.
# playsound( 'hello.mp3' )  ##  play audio



