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


def createPerceptualHash(arrayData: "np.ndarray") -> str:
    """
    Creates a perceptual hash of the given data
    :param arrayData: an array contains the data to be hashed
    :return: a string describe the hashed array (could be converted to hex using hex_to_hash())
    """
    dataInstance = Image.fromarray(arrayData)
    return imagehash.phash(dataInstance, hash_size=16).__str__()

 #def createPerceptualHash(Spectro):
 #     hashcode = imagehash.phash(Image.open(Spectro) ) #We will use Perceptual hashing 
 #     return(str(hashcode))

#features
def features (wav, sfreq): 
      
        melspectro = librosa.feature.melspectrogram(y=wav, sr=sfreq)
        newimage=Image.fromarray(melspectro)
        hash1=imagehash.phash(newimage)
        ##2
        chroma_stft = librosa.feature.chroma_stft(y=wav, sr=sfreq)
        newimage=Image.fromarray(chroma_stft)
        hash2=imagehash.phash(newimage)
        #a=np.mean(chroma_stft)
        #print(a)
        #print(hash1)
        ##3
        spec_cent = librosa.feature.spectral_centroid(y=wav, sr=sfreq)
        newimage=Image.fromarray(spec_cent)
        hash3=imagehash.phash(newimage)
        ##4
        rolloff = librosa.feature.spectral_rolloff(y=wav, sr=sfreq)
        newimage=Image.fromarray(rolloff)
        hash4=imagehash.phash(newimage)
        return str(hash1),hash2,hash3,hash4
        
#def generateFeatures(audioData, samplingFreq):  # TODO: ADD MORE FEATURES
 #   mfcc = librosa.feature.mfcc(
  #      audioData.astype('float64'), sr=samplingFreq)  # generate the mfcc spectral feature
  #  return mfcc      

#def generatePerceptualHash(mfcc):
 #   mfcc = Image.fromarray(mfcc)  # convert the array to a PIL image
 #   mfccHash = imagehash.phash(mfcc)  # generate perceptual hash
 #   return mfccHash



