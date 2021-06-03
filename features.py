import matplotlib.pyplot as plt
import librosa 
from pydub import AudioSegment
from tempfile import mktemp
import sklearn
import librosa.display
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
import os
import glob
from scipy import signal
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PIL import Image
from pathlib import Path
import imagehash
import pylab
import imagehash
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("hases")
n=0
m=0
l=1
v=0

paths=[]
featureMixHash = []
songs_name=[]
featurename=['melspectrogram', 'chroma_stft','mfcc','spectral_centroid']    

dir="F:/DSP/Task4/data"
for filename in os.listdir(dir):   ####################### you need to be in the folder of songs
    if filename.endswith(".mp3"):
        paths.append(filename)
        songs_name.append(os.path.splitext(filename)[0])
for t in featurename:
    m+=1
    sheet.write(0,m,t)
for o in songs_name:
       v+=1
       sheet.write(v,0,o)        
for i in paths:
        name_mp3= os.path.join(dir+"/",i)
        mp3_audio = AudioSegment.from_file(name_mp3, format="mp3")[:60000]  # read mp3
        sound=AudioSegment.from_mp3(f"{name_mp3}")
        wname = mktemp('.wav')  # use temporary file
        sound.export(wname, format="wav")  # convert to wav
        # Read the wav file (mono)
        wav,sfreq =librosa.load(wname,duration=60)
        pylab.axis('off')  # no axis
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])  # Remove the white edge
        s = librosa.amplitude_to_db(np.abs(librosa.stft(wav)), ref=np.max)
        librosa.display.specshow(s, y_axis='linear')
        #spectro=plt.specgram(wavsong, Fs=samplingFrequency) 
        #plt.savefig('spectrogram/'+os.path.splitext(i)[0]+'.png')
     
        melspectro = librosa.feature.melspectrogram(y=wav, sr=sfreq)
        # melSpectrogram = librosa.feature.melspectrogram(wav.astype('float64'), sr=sfreq)
        hash1=str(imagehash.phash( Image.fromarray(melspectro), hash_size=16))
            
        chroma_stft = librosa.feature.chroma_stft(y=wav, sr=sfreq)
        hash2=str(imagehash.phash( Image.fromarray(chroma_stft), hash_size=16))
            
        mfcc = librosa.feature.mfcc(wav.astype('float64'), sr=sfreq)
        hash3=str(imagehash.phash( Image.fromarray(mfcc), hash_size=16))
            
        spec_cent = librosa.feature.spectral_centroid(y=wav, sr=sfreq)
        hash4=str(imagehash.phash( Image.fromarray(spec_cent), hash_size=16))
            
        #rolloff = librosa.feature.spectral_rolloff(y=wav, sr=sfreq)
        #features=[melspectro, chroma_stft,mfcc,spec_cent]    
        Hashs=[hash1,hash2,hash3,hash4]
        #for feature in features:
            #featureMixHash.append (str(imagehash.phash( Image.fromarray(feature), hash_size=16)))
            
        for k in Hashs:
            n+=1
            sheet.write(l,n,k)
        n=0
        l+=1
        featureMixHash.clear()
workbook.save("database.xls")
   
       