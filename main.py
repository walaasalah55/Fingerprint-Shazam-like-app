from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog 
from MainWindow import Ui_MainWindow
from functools import partial
import librosa 
import logging
import sys
import os
import matplotlib.pyplot as plot
import librosa 
from pydub import AudioSegment
from tempfile import mktemp
#import sklearn
import librosa.display
import numpy as np
from PIL import Image
import imagehash
import pylab


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
        self.Buttons= [self.ui.audio1 , self.ui.audio2 , self.ui.search]
     
        #self.Buttons[1].setDisabled(True) 
        #self.Buttons[2].setDisabled(True) 
        #self.OpenAgain_flag1  = False 
        #self.OpenAgain_flag2 = False 

        self.ui.audio1.clicked.connect(lambda : self.mp3Converter(0) )
        self.ui.audio2.clicked.connect(lambda : self.mp3Converter(1) )
        #self.ui.slider.sliderReleased.connect(lambda : self.mixer())
        #self.ui.Search.clicked.connect(lambda : self.compare()  )
       
        #self.ui.horizontalSlider.valueChanged.connect(self.mixer)
     
    def mp3Converter(self,ID):
      self.path, self.format= QFileDialog.getOpenFileName( None, 'choose the signal', os.getenv('HOME') ,"mp3(*.mp3)" ) 
      audName = self.path.split('/')[-1]
      if self.path == "":
            pass
          
      mp3_audio = AudioSegment.from_file( self.path , format="mp3")[:60000]  # read mp3
      wname = mktemp('.wav')  # use temporary file
      mp3_audio.export(wname, format="wav")  # convert to wav
      #warnnn
      self.ui.audioname[ID+1].setText(os.path.splitext(os.path.basename(self.path))[0])
        #self.Buttons[1].setDisabled(False) 
      self.wavsong[ID+1],self.samplingFrequency[ID+1] =librosa.load(wname)
      #self.OpenAgain_flag1  =  True
      print("file1 read ")
      logger.info(f"uplood Audio {ID + 1}: {audName} ")
   
     
     # self.ui.tableWidget.clearContents()


   
    
    
    logger.info(f"no thing till now:(")

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
      main()