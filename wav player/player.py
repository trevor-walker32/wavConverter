import pydub
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("Summers.wav", format="wav")
play(sound)