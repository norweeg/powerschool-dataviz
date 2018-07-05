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
        #make the QApplication running and handling the events in this window accessible to this object
        global app
        self.app=app
        #initialize the super class
        super().__init__(parent)
        #use compiled .ui file to build GUI
        self.gui=Ui_PowerSchool_DataViz()
        self.gui.setupUi(self)
        #connect menu items to the functions they should execute
        self.gui.actionNew_Window.triggered.connect(self.__new_window)
        self.gui.actionQuit.triggered.connect(self.app.closeAllWindows) #this is why we need global app
        self.gui.actionOpen.triggered.connect(self.__open_file)
        self.gui.actionSave_Graph_As.triggered.connect(self.__save_graph)
        self.gui.actionPrint.triggered.connect(self.__print)
        self.gui.actionAbout_PowerSchool_DataViz.triggered.connect(self.__about)
        self.gui.actionAbout_Qt.triggered.connect(self.app.aboutQt) #this about window is built into Qt
        #display the window
        self.show()

    #creates a new instance of this object
    def __new_window(self):
        return PowerSchool_DataViz(parent=self)

    #use built-in file dialog to pick CSV file and read it into pandas dataframe
    #use of file dialog with csv filter is presumed sufficient to avoid exceptions related to file permissions
    #and selecting files which are absolutely not csv files
    def __open_file(self):
        try:
            input_file=QtWidgets.QFileDialog().getOpenFileName(parent=self,directory=str(Path.home()),filter="CSV Files (*.csv)")
            self.__input_data=pd.read_csv(Path(input_file[0]),engine="python",squeeze=True,parse_dates=["IncidentDate","DateReported"],infer_datetime_format=True,header=0,dtype={"StudentNumber":"str"})
        except pd.errors.ParserError as e:
            return QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Critical,parent=self,text=str(e)).show()
        except pd.errors.EmptyDataError as e:
            return QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Critical,parent=self,text=str(e)).show()
        except pd.errors.DtypeWarning as e:
            return QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Warning,parent=self,text=str(e)).show()

        #self.__create_plot()
        self.__populate_table()

    #fill the table on the data tab for reference
    def __populate_table(self):
        #remove everything from the table.  If we opened a new file, it is new data.
        self.gui.Data_Table.clear()
        #get the size of table and set adjust the row and column count to match
        row_count,column_count=self.__input_data.shape
        self.gui.Data_Table.setColumnCount(column_count)
        self.gui.Data_Table.setRowCount(row_count)
        #fill in column headers
        self.gui.Data_Table.setHorizontalHeaderLabels(self.__input_data.columns)
        #iterate over the cells of data and enter them into the table
        for row in self.__input_data.itertuples():
            for column in range(column_count): 
                #first item in row is its index
                self.gui.Data_Table.setItem(row[0],column,QtWidgets.QTableWidgetItem(self.__input_data.astype(str).iat[row[0],column]))
        #as of the writing of this code, there is a bug in QtDesigner which always saves the visibility  of the horizontal and
        #vertical headers as "false", so I will manually set them here because I don't want to have to manually update the
        #designer .ui file before compiling it to python
        self.gui.Data_Table.horizontalHeader().setVisible(True)
        self.gui.Data_Table.verticalHeader().setVisible(True)
        #make the table easy to read and make it static.  No editing data.
        self.gui.Data_Table.resizeColumnsToContents()
        self.gui.Data_Table.resizeRowsToContents()
        self.gui.Data_Table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.update()

    def __save_graph(self):
        filename=QtWidgets.QFileDialog().getSaveFileName(parent=self,directory=str(Path.home()))
        print(filename)

    def __print(self):
        QtPrintSupport.QPrintDialog(parent=self).open()

    def __about(self):
        return About_Window(self)

    def __create_plot(self):
        self.__plot
        self.html=file_html(self.__plot, CDN)

#Trying to use as much built-in functionality as possible.  This was the best I could come up with for an "About" window
#that also displays the license unless I wanted to make my own
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