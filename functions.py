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

def mixer(song1, song2, w):    
      return (w*song1 + (1.0-w)*song2)

def spectrogram ( wav, sfreq):
        Spectro_Path = 'songSpectrogram.png'
        pylab.axis('off')  # no axis
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])  # Remove the white edge
        #D = librosa.amplitude_to_db(np.abs(librosa.stft(self.outputSong)), ref=np.max)
        #librosa.display.specshow(D, y_axis='linear')
        #pylab.savefig(Spectro_Path, bbox_inches=None, pad_inches=0)
        #pylab.close()
        spectro=plt.specgram(wav, Fs=sfreq) 
        plt.savefig(Spectro_Path)
         
        
#def generateSpectrogram(path, audioData, samplingFreq):
 #   fig = plt.figure()
 #   spectro = plt.specgram(audioData, Fs=samplingFreq,
 #                          NFFT=128, noverlap=0)  # plot
  #  spectrogamFilePath = path[:-4]  # remove '.mp3' from the path
  #  fig.savefig(spectrogamFilePath)  # save the spectrogram        


def createspectroHash(Spectro):
      hashcode = imagehash.phash(Image.open(Spectro) ) #We will use Perceptual hashing 
      return(str(hashcode))

#features
def features(wav, sfreq): 
      
  melspectro = librosa.feature.melspectrogram(y=wav, sr=sfreq)
  # melSpectrogram = librosa.feature.melspectrogram(wav.astype('float64'), sr=sfreq)
  
  chroma_stft = librosa.feature.chroma_stft(y=wav, sr=sfreq)

  mfcc = librosa.feature.mfcc(wav.astype('float64'), sr=sfreq)
  
  return melspectro,chroma_stft,mfcc



def generatePerceptualHash(feature):
    feature1 = Image.fromarray(feature)  # convert the array to a PIL image
    featureHash = imagehash.phash( feature1, hash_size=16)
      #newimage=Image.fromarray(rolloff)
      #hash4=imagehash.phash(newimage)
    return str(featureHash)
    



