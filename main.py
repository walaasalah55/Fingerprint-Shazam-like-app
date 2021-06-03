from PyQt5 import QtWidgets, QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog 
from MainWindow import Ui_MainWindow
from functools import partial 
import logging
import sys
import os
import librosa 
from tempfile import mktemp
import imagehash
import librosa.display
import numpy as np
from functions import* 
import pandas as pd
import xlwt

logging.basicConfig(filename="steps.log", 
                    format='(%(asctime)s) | %(message)s', 
                    filemode='w') 
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.audFiles = [None, None]
        self.audRates = [None, None]
        self.testHash = None
        self.audMix = None
        self.name=[]
        self.feature1=[]
        self.feature2=[]
        self.feature3=[]
        #self.spectrogram = spectrogram()._spectrogram  # Spectrogram Extraction function
        #self.extractFeatures = spectrogram().spectralFeatures  # Feature Extraction function
        self.songnames = [self.ui.audioname1, self.ui.audioname2]
        self.Buttons= [self.ui.audio1 , self.ui.audio2]
        for Button in self.Buttons:
            Button.clicked.connect(partial(self.loadFile, Button.property("indx")))
        self.ui.search.clicked.connect(self.extract)
        
        Data=pd.read_excel("database.xls")
        for i in range(7):
            self.name.append(Data.iloc[i, 0])
            self.feature1.append(Data.iloc[i, 1]) 
            self.feature2.append(Data.iloc[i, 2]) 
            self.feature3.append(Data.iloc[i, 3]) 
   
    def loadFile(self,indx):
      self.path, self.format= QFileDialog.getOpenFileName( None, 'choose the Audio' , os.getenv('HOME') ,"mp3(*.mp3)" ) 
      audName = self.path.split('/')[-1]
      if self.path == "":
            pass
      else:
           songwav,samplefreq=mp3Converter(self.path)      
           self.audFiles[indx-1] = songwav
           self.audRates[indx-1] = samplefreq
           print(samplefreq)
           self.songnames[indx-1].setText(audName)
           #print("file1 read ")
           logger.info(f"uplood Audio {indx-1}: {audName} ")
   
    def extract(self):
        #print("Slider Value is %s"%self.ui.slider.value())
        if (self.audFiles[0] is not None) and (self.audFiles[1] is not None):
            logger.info("loaded two songs ")
            w = self.ui.slider.value()/100
            self.audMix =mixer(self.audFiles[0], self.audFiles[1], w)
            logger.info("Slider Value is %s"%self.ui.slider.value())
            #print(self.audMix)
        else:
            logger.info("loaded only one song")
            if self.audFiles[0] is not None : self.audMix = self.audFiles[0]
            if self.audFiles[1] is not None: self.audMix = self.audFiles[1]
            
        if self.audMix is not None:
            self.featureMixHash = []  # Holds the features extracted from Mix  
            #self.featureMixHash=  [...]
            logger.info("starting Extraction")
            self.spectro = spectrogram(self.audMix, self.audRates[0])
            #self.testHash = createspectroHash(self.spectro)
            #print(self.testHash)
            for feature in features(self.audMix, self.audRates[0]):
                self.featureMixHash.append(generatePerceptualHash(feature))
            logger.info(f"Hashes extracted successfully")    
            print(self.featureMixHash) 
            self.compareHash()

    def compareHash(self):   
        self.result = [] 

        for i in range(len(self.name)):
              #for j in range(3) :
                  melspectro_index = ( 1-(imagehash.hex_to_hash(self.featureMixHash[0])- imagehash.hex_to_hash(self.feature1[i]) ) / 256.0 )
                  chroma_stft_index= ( 1-(imagehash.hex_to_hash(self.featureMixHash[1])- imagehash.hex_to_hash(self.feature2[i]) ) / 256.0 )
                  mfcc_index= ( 1-(imagehash.hex_to_hash(self.featureMixHash[2])- imagehash.hex_to_hash(self.feature3[i]) ) / 256.0 )
                  self.result.append( [os.path.basename(self.name[i]),(melspectro_index + chroma_stft_index + mfcc_index ) / 3])
        
        self.result.sort(key=lambda x: x[1], reverse=True)
        print(self.result)
        self.constuctTable()

    def constuctTable(self):

        for row in range(len(self.result)):
                self.ui.resultstable.setItem(row, 0, QtWidgets.QTableWidgetItem(self.result[row][0]))
                self.ui.resultstable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(round(self.result[row][1]*100, 2))+"%"))    
            
        #self.ui.resultstable.clear()
        self.result.clear() 
   

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
      main()