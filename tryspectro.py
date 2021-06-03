def spectrogram (self):
        Spectro_Path = 'songSpectrogram.png'
        pylab.axis('off')  # no axis
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])  # Remove the white edge
        #D = librosa.amplitude_to_db(np.abs(librosa.stft(self.outputSong)), ref=np.max)
        #librosa.display.specshow(D, y_axis='linear')
        #pylab.savefig(Spectro_Path, bbox_inches=None, pad_inches=0)
        #pylab.close()
        spectro=plt.specgram(wavsong, Fs=samplingFrequency) 
        plt.savefig(Spectro_Path)
        self.SongHash = self.hashing(Spectro_Path) 
        #self.features()

def hashing(self,filename):
      hashcode = imagehash.phash(Image.open(filename) ) #We will use Perceptual hashing 
      return(str(hashcode))

def features (self): 
      
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
  
    
      #spectral centroid 
      #pylab.axis('off')  
      #pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
      #SavePath = 'HASH_centroid.png'
      #featured1= librosa.feature.spectral_centroid(y=self.outputSong, sr=self.samplingFrequency1)
      #librosa.display.specshow(featured1.T,sr=self.samplingFrequency1 )
      #pylab.savefig(SavePath, bbox_inches=None, pad_inches=0)
      #pylab.close()

      #self.centroidHash= self.hashing('HASH_centroid.png')
      #self.rolloffHash= self.hashing('HASH_rolloff.png')
      #print(self.SongHash,self.centroidHash )



        #a=np.mean(chroma_stft)
        #print(a)
        #print(hash1)
        ##4
        #rolloff = librosa.feature.spectral_rolloff(y=wavsong, sr=samplingFrequency)
        #newimage=Image.fromarray(rolloff)
        #hash4=imagehash.phash(newimage)



        
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