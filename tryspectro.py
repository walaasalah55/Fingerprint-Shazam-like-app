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
