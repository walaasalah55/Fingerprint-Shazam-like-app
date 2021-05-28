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
import csv

paths=[]

dir="F:/Task4/data"
for filename in os.listdir(dir):   ################################### you need to be in the folder of songs
    if filename.endswith(".mp3"):
        paths.append(filename)
for i in paths:
        name_mp3= os.path.join(dir+"/",i)
        mp3_audio = AudioSegment.from_file(name_mp3, format="mp3")[:60000]  # read mp3
        sound=AudioSegment.from_mp3(f"{name_mp3}")
        wname = mktemp('.wav')  # use temporary file
        sound.export(wname, format="wav")  # convert to wav
        # Read the wav file (mono)
        wavsong,samplingFrequency =librosa.load(wname,duration=60)
        pylab.axis('off')  # no axis
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])  # Remove the white edge
        s = librosa.amplitude_to_db(np.abs(librosa.stft(wavsong)), ref=np.max)
        #print(s)
        librosa.display.specshow(s, y_axis='linear')
        #spectro=plt.specgram(wavsong, Fs=samplingFrequency) 
        #plt.savefig('spectrogram/'+os.path.splitext(i)[0]+'.png')
        #rmse = librosa.feature.rmse(y=wavsong)
        ##1
        melspectro = librosa.feature.melspectrogram(y=wavsong, sr=samplingFrequency)
        newimage=Image.fromarray(melspectro)
        hash1=imagehash.phash(newimage)
        ##2
        chroma_stft = librosa.feature.chroma_stft(y=wavsong, sr=samplingFrequency)
        newimage=Image.fromarray(chroma_stft)
        hash2=imagehash.phash(newimage)
        #a=np.mean(chroma_stft)
        #print(a)
        #print(hash1)
        ##3
        spec_cent = librosa.feature.spectral_centroid(y=wavsong, sr=samplingFrequency)
        newimage=Image.fromarray(spec_cent)
        hash3=imagehash.phash(newimage)
        ##4
        rolloff = librosa.feature.spectral_rolloff(y=wavsong, sr=samplingFrequency)
        newimage=Image.fromarray(rolloff)
        hash4=imagehash.phash(newimage)

        
header = 'filename: melspectrogram chroma_stft spectral_centroid spectral_rolloff'

#header += ' label'
header = header.split()
file = open('filedata.csv', 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)        

#to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
to_append = f'{filename} {hash1} {hash2} {hash3} {hash4}'    

#to_append += f' {"data/"}'
file = open('filedata.csv', 'a', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(to_append.split())    
#number=0
for filename in os.listdir("spectrogram"):   ###### you have to be in the folder of spectogram images
    if filename.endswith(".png"):
       
        hashcode = imagehash.phash(Image.open('spectrogram'+'/'+filename))
        #print(int(str(hashcode),16))
       # f = open('spectrogram/hashes/'+os.path.splitext(os.path.basename(filename))[0]+'.csv','w')
        #txt
       # f.write(str(hashcode))
        #f.close()
        #number +=1
#print(number)

        #Spectro_Path = 'spectrogram/'+os.path.splitext(os.path.basename(filename))[0]+'.png'
        #pylab.axis('off')  # no axis
        #pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])  # Remove the white edge
        #D = librosa.amplitude_to_db(np.abs(librosa.stft(wavsong)), ref=np.max)
        #librosa.display.specshow(D, y_axis='linear')
        #pylab.savefig(Spectro_Path, bbox_inches=None, pad_inches=0)
        #pylab.close()
