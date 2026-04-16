import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size:150px;"
                                      "color: hsl(356, 56%, 45%);"
                                       )

        self.setStyleSheet("background-color:black;")

        #Setting the font id so that it can be used for the font of the label
        fonts_id = QFontDatabase.addApplicationFont("/Users/family/Library/Fonts/DS-DIGIT.TTF")

        font_family = QFontDatabase.applicationFontFamilies(fonts_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        #Updates the time every second
        self.timer.start(1000)
        self.update_time()
    def update_time(self):
        #the toString method is a format specifier that assigns the hours, minutes, seconds and if wanted the AM of PM
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())