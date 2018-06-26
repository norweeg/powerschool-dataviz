from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngine, QtWebEngineWidgets, QtPrintSupport
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import pandas
import os
import sys
from pathlib import Path
from PowerSchool_DataViz_UI import Ui_PowerSchool_DataViz
import PowerSchool_DataViz_Resources

class AboutWindow(QtWidgets.QMessageBox):
    def __init__(self,parent=None,description="",license="",title=""):
        super().__init__(parent=parent,text=description)
        self.setStandardButtons(self.Ok)
        #self.setWindowTitle(title)
        #self.setIcon=parent.windowIcon()
        #self.setText(description)
        self.setDetailedText(license)
        #find and override default text/behavior of automatically created "details" button
        for button in self.buttons():
            if self.buttonRole(button)==self.ActionRole:
                #self.removeButton(button)
                #self.removeButton(self.details_button)
                self.new_button=QtWidgets.QPushButton(parent=self,text="Show License")
                self.new_button.clicked.connect(self.__toggle_license)
                self.addButton(self.new_button,self.ActionRole)
        self.show()

    def __toggle_license(self):
        license_textbox=self.children()[3]
        if license_textbox.isVisible():
            license_textbox.hide()
            self.new_button.setText("Show License")
        else:
            license_textbox.show()
            self.new_button.setText("Hide License")





class PowerSchool_DataViz(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        global app
        self.app=app
        #initialize the super class
        super().__init__(parent)
        self.gui=Ui_PowerSchool_DataViz()
        self.gui.setupUi(self)
        self.gui.actionNew_Window.triggered.connect(self.__new_window)
        self.gui.actionQuit.triggered.connect(self.app.closeAllWindows)
        self.gui.actionOpen.triggered.connect(self.__open_file)
        self.gui.actionSave_Graph_As.triggered.connect(self.__save_graph)
        self.gui.actionPrint.triggered.connect(self.__print)
        self.gui.actionAbout_PowerSchool_DataViz.triggered.connect(self.__about)
        self.gui.actionAbout_Qt.triggered.connect(self.app.aboutQt)
        self.show()


    def __new_window(self):
        return PowerSchool_DataViz(parent=self)

    def __open_file(self):
        try:
            self.__input_data=pandas.read_csv(QtWidgets.QFileDialog().getOpenFileName(parent=self,directory=str(Path.home()),filter="CSV Files (*.csv)"))
        except:
            return
        #self.__create_plot()
        #self.__populate_table()
    
    def __save_graph(self):
        filename=QtWidgets.QFileDialog().getSaveFileName(parent=self,directory=str(Path.home()))
        print(filename)

    def __print(self):
        QtPrintSupport.QPrintDialog(parent=self).open()

    def __about(self):
        name=self.app.applicationName()+"\n\n"
        description="A tool for viewing PowerSchool behavior incident data interactively & graphically\n\nCopyright (c) 2018 Brennen Raimer"
        file = QtCore.QFile(":/text/LICENSE")
        if file.open(QtCore.QFile.ReadOnly):
            license = str(file.readAll(), 'utf-8')
            file.close()
        return AboutWindow(parent=self,description=description,license=license,title=name)

    def __populate_table(self):
        pass

    def __create_plot(self):
        self.__plot
        self.html=file_html(self.__plot, CDN)





if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    app.setApplicationName("PowerSchool DataViz")
    window=PowerSchool_DataViz()
    sys.exit(app.exec_())