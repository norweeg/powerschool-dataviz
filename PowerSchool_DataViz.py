from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngine, QtWebEngineWidgets, QtPrintSupport
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import pandas as pd
import os
import sys
from pathlib import Path
from PowerSchool_DataViz_UI import Ui_PowerSchool_DataViz
import PowerSchool_DataViz_Resources

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
            input_file=QtWidgets.QFileDialog().getOpenFileName(parent=self,directory=str(Path.home()),filter="CSV Files (*.csv)")
            self.__input_data=pd.read_csv(Path(input_file[0]),engine="python",squeeze=True,)
        except pd.errors.ParserError as e:
            return QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Critical,parent=self,text=str(e)).show()
        except pd.errors.EmptyDataError as e:
            return QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Critical,parent=self,text=str(e)).show()
        except pd.errors.DtypeWarning as e:
            return QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Warning,parent=self,text=str(e)).show()

        #self.__create_plot()
        self.__populate_table()

    def __populate_table(self):
        self.gui.Data_Table.clear()
        row_count,column_count=self.__input_data.shape
        self.gui.Data_Table.setColumnCount(column_count)
        self.gui.Data_Table.setRowCount(row_count)
        self.gui.Data_Table.setHorizontalHeaderLabels(self.__input_data.columns)
        for row in self.__input_data.itertuples():
            for column in range(column_count): 
                #first item in row is its index
                self.gui.Data_Table.setItem(row[0],column,QtWidgets.QTableWidgetItem(self.__input_data.iat[row[0],column]))
        self.gui.Data_Table.resizeColumnsToContents()
        self.gui.Data_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.update()
        return

    
    def __save_graph(self):
        filename=QtWidgets.QFileDialog().getSaveFileName(parent=self,directory=str(Path.home()))
        print(filename)

    def __print(self):
        QtPrintSupport.QPrintDialog(parent=self).open()

    def __about(self):
        return About_Window(self)

    def __populate_table(self):
        pass

    def __create_plot(self):
        self.__plot
        self.html=file_html(self.__plot, CDN)

class About_Window(QtWidgets.QMessageBox):
    def __init__(self,parent):
        global app
        name=app.applicationName()+"\n\n"
        description="A tool for viewing PowerSchool behavior incident data interactively & graphically\n\nCopyright (c) 2018 Brennen Raimer"
        super().__init__(parent=parent,text=name+description)
        file = QtCore.QFile(":/text/LICENSE")
        if file.open(QtCore.QFile.ReadOnly):
            license = str(file.readAll(), 'utf-8')
            file.close()
        self.setDetailedText(license)
        self.addButton(self.Ok)
        for button in self.buttons():
            if button.text()=="Show Details...":
                button.setText("Show License")
                button.clicked.connect(self.__toggle_text)
        self.update()
        self.show()

    def __toggle_text(self):
        self.update()
        for button in self.buttons():
            if button.text()=="OK":
                continue
            elif "Show License" in button.text():
                self.showbutton=button
                button.setText("Hide License")
            else:
                self.hidebutton=button
                button.setText("Show License")
        self.update


if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    app.setApplicationName("PowerSchool DataViz")
    window=PowerSchool_DataViz()
    sys.exit(app.exec_())