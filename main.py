from PyQt5 import QtWidgets, QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog 
from MainWindow import Ui_MainWindow
from functools import partial 
import logging
import sys
import os
import matplotlib.pyplot as plt
import librosa 
from pydub import AudioSegment
from tempfile import mktemp
#import sklearn
import librosa.display
import numpy as np
from functions import mp3Converter, mixer


logging.basicConfig(filename="file.log", 
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
        self.featureMixHash = []  # Holds the features extracted from Mix
        self.results = []
        #self.spectrogram = spectrogram()._spectrogram  # Spectrogram Extraction function
        #self.extractFeatures = spectrogram().spectralFeatures  # Feature Extraction function
       
        self.songnames = [self.ui.audioname1, self.ui.audioname2]
        self.Buttons= [self.ui.audio1 , self.ui.audio2]

       
        for btn in self.Buttons:
            btn.clicked.connect(partial(self.loadFile, btn.property("indx")))

        #self.ui.audio1.clicked.connect(lambda : self.mp3Converter(0) )
        #self.ui.audio2.clicked.connect(lambda : self.mp3Converter(1) )
        #self.ui.slider.sliderReleased.connect(lambda : self.mixer())
        self.ui.search.clicked.connect(self.extract)
       
        #self.ui.slider.valueChanged.connect(self.mixer)
     
    def loadFile(self,indx):
      self.path, self.format= QFileDialog.getOpenFileName( None, 'choose the Audio' , os.getenv('HOME') ,"mp3(*.mp3)" ) 
      audName = self.path.split('/')[-1]
      if self.path == "":
            pass
      else:
           songwav,samplefreq=mp3Converter(self.path)      
           self.audFiles[indx-1] = songwav
           self.audRates[indx-1] = samplefreq
           self.songnames[indx-1].setText(audName)
           #self.songnames[indx-1].setText(os.path.splitext(os.path.basename(self.path))[0])
           #self.OpenAgain_flag1  =  True
           print("file1 read ")
           logger.info(f"uplood Audio {indx-1}: {audName} ")
   
    def extract(self):
       
        print("Slider Value is %s"%self.ui.slider.value())
        logger.debug("starting searching process")

        if (self.audFiles[0] is not None) and (self.audFiles[1] is not None):
            logger.debug("loaded two different songs ")
            #w: weight (percentage) of song1
            w = self.ui.slider.value()/100
            self.audMix =mixer(self.audFiles[0], self.audFiles[1], w)
            #self.outputSong = self.wavsong1 * w + self.wavsong2 * (1-sliderRatio)
            print(w)
            print(self.audMix)
        else:
            logger.debug("loaded only one song")
            if self.audFiles[0] is not None : self.audMix = self.audFiles[0]
            if self.audFiles[1] is not None: self.audMix = self.audFiles[1]
            
        if self.audMix is not None:
            logger.debug("starting Extraction")

          ###warnnn:lesa hagrb fe dol

            #self.spectro = self.spectrogram(self.audMix, self.audRates[0])[-1]
            #self.testHash = createPerceptualHash(self.spectro)

            #for feature in self.extractFeatures(self.audMix, self.spectro, self.audRates[0]):
             #   self.featureMixHash.append(createPerceptualHash(feature))

            #self.__compareHash()


    
  
  
    logger.info(f"no thing till now:(")

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
      main()