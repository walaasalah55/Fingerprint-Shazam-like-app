import matplotlib.pyplot as plt
import librosa 
import numpy as np
from pydub import AudioSegment
from tempfile import mktemp
from PIL import Image
import imagehash
import pylab

def mp3Converter(wave):     
      mp3_audio = AudioSegment.from_file( wave , format="mp3")[:60000]  # read mp3
      wname = mktemp('.wav')  # use temporary file
      mp3_audio.export(wname, format="wav")  # convert to wav
      wav,sfreq =librosa.load(wname)
      return wav,sfreq

#def mixer(song1: np.ndarray, song2: np.ndarray, dType: str = 'int16', w: float = 0.5) -> np.ndarray:
def mixer(song1, song2, w):    
      return (w*song1 + (1.0-w)*song2)





