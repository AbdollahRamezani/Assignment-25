import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from mainwindow import Ui_MainWindow 
from my_time import MyTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
        self.ui.btn_start_timer.clicked.connect(start_timer)
        self.ui.label_stopwatch.setText("0:0:0")
        self.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
                
    def show_stopwatch(self, time):
        print(f"{time.hour}:{time.minute}:{time.second}")
        self.ui.label_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")
        
       
         

class TimerThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 15, 0)    
    def run(self):
        while True:
            self.time.minus()
            self.signal_show.emit(self.time )
            time.sleep(1)      
        
class StopWatchThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)
        
    def run(self):
        while True:
            self.time.plus()
            self.signal_show.emit(self.time )
            time.sleep(1)  

    def reset(self):
        self.time.hour = 0
        self.time.minute = 0
        self.time.second = 0

def start_timer():
    thread_timer.start() 

def start_stopwatch():
    thread_stopwatch.start()            

def stop_stopwatch():
    thread_stopwatch.terminate()  #پایان دادن به ترد

def reset_stopwatch():
    thread_stopwatch.reset()

def show_number(time):
     label = MainWindow()
     label.show_stopwatch(time)

if __name__ == "__main__":        
    app = QApplication(sys.argv)    
    main_window = MainWindow()
    main_window.show()
    thread_stopwatch = StopWatchThread() 
    thread_timer = TimerThread()
    thread_stopwatch.signal_show.connect(show_number)

    app.exec()