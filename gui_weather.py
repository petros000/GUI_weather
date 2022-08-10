import sys

from PyQt5.QtCore import QTimer, QEventLoop
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QGraphicsView
from PyQt5 import uic, QtCore
from weather import Weather
import pyqtgraph as pg

class GUIWeather(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('form_qt.ui', self)

        self.city_name = self.findChild(QLineEdit, 'lineEdit')
        self.country_cod = self.findChild(QLineEdit, 'lineEdit_2')
        self.label_res = self.findChild(QLabel, 'label')
        self.graphicsView = self.findChild(QGraphicsView, 'graphicsView')

        self.graphics = pg.PlotWidget(self.graphicsView)
        self.graphics.setGeometry(QtCore.QRect(0, 0, 330, 230))

        self.button_current_weather = self.findChild(QPushButton, 'pushButton')
        self.button_forecast_weather = self.findChild(QPushButton, 'pushButton_3')
        self.button_online_weather = self.findChild(QPushButton, 'pushButton_2')

        self.button_current_weather.clicked.connect(self.get_current_weather)
        self.button_forecast_weather.clicked.connect(self.get_forecast_weather)

        self.button_online_weather.clicked.connect(self.get_online_weather)
        #self.button_online_weather.clicked.disconnect()

    def get_current_weather(self):
        weather = Weather(self.city_name.text(), self.country_cod.text())
        current_weather = weather.call_current_weather_data()
        self.label_res.setText(str(current_weather))
        print(current_weather)

    def get_forecast_weather(self):
        weather = Weather(self.city_name.text(), self.country_cod.text())
        date_time, date_temp = weather.call_5_day_3hour_forecast_data()

        self.graphics.clear()
        self.graphics.plot(date_temp)

    def sleep_qt(self, ms):
        loop = QEventLoop()
        QTimer.singleShot(ms, loop.quit)
        loop.exec()

    def get_online_weather(self):
        if self.button_online_weather.isChecked():
            self.button_online_weather.disconnect()
        while True:
            self.get_current_weather()
            self.sleep_qt(1_000)


def main():
    app = QApplication(sys.argv)
    window = GUIWeather()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

