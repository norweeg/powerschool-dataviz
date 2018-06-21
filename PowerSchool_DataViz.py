from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngine, QtWebEngineWidgets
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import pandas
import os
import sys
from pathlib import Path
from PowerSchool_DataViz_Window import Ui_PowerSchool_DataViz_Window

class PowerSchool_DataViz_Window(QtWidgets.QMainWindow):
    def __init__(self):
        #initialize the super class
        super().__init__()
        Ui_PowerSchool_DataViz_Window().setupUi(self)
        self.show()


    def __open_file(self):
        dialog_box=QtWidgets.QFileDialog(self,directory=Path.home(),filter="CSV Files (*.csv)")
        try:
            self.__input_data=pandas.read_csv(dialog_box.getOpenFileName())
        except:
            return
        self.__create_plot()
        self.__populate_table()

    def __populate_table(self):
        pass

    def __create_plot(self):
        self.__plot
        self.html=file_html(self.__plot, CDN)





if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    app.setApplicationName("PowerSchool DataViz")
    window=PowerSchool_DataViz_Window()
    sys.exit(app.exec_())