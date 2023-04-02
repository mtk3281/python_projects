from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
from PyQt5 import QtGui
from PyQt5.uic import loadUi
import sys

class Main(QMainWindow):
    def __init__(self):
        super(Main , self).__init__()
        loadUi('main.ui',self)

        self.current_path = None
        self.font_size = 11
        self.setWindowIcon(QtGui.QIcon("icon.png"))
    
        self.action_New_File.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.save_as)
        self.actionQuit.triggered.connect(self.quit)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionDark_Mode.triggered.connect(self.Dark_mode)
        self.actionLight_Mode.triggered.connect(self.Light_mode)
        self.actionIncrease_Font_Size.triggered.connect(self.increase_font)
        self.actionDecrease_Font_Size.triggered.connect(self.decrease_font)


    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled - PyNote")
        self.current_path = None

    def open(self):
        myfile = QFileDialog.getOpenFileName(self,'open file',"C:/users","text files (*.txt)") 
        self.setWindowTitle(myfile[0]+" - PyNote")
        self.current_path = myfile[0]

        content = open(myfile[0],"r")
        text = content.read()
        self.textEdit.setText(text)
        
    def save(self):
        if (self.current_path == None):
            self.save_as()
        else:
            values  = self.textEdit.toPlainText()
            with open(self.current_path,"w") as content:
                content.write(values)

    def save_as(self):
        path = QFileDialog.getSaveFileName(self,"save file","C:/users","text files (*.txt)")
        values  = self.textEdit.toPlainText()
        with open(path[0],"w") as content:
                content.write(values)
        self.setWindowTitle(path[0]+" - PyNote")
        
    def quit(self):
        self.close()

    def undo(self):
        self.textEdit.undo()

    def redo(self):
        self.textEdit.redo()

    def cut(self):
        self.textEdit.cut()
  
    def copy(self):
        self.textEdit.copy()

    def paste(self):
        self.textEdit.paste()

    def Dark_mode(self):
        self.setStyleSheet(''' 
                                QWidget{
                                    background-color: rgb(33,33,33);
                                    color:#FFFFFF;
                                      }
                                QTextEdit{
                                    background-color:rgb(46,46,46);
                                        }
                                QMenuBar::item:selected{
                                    color:#000000;
                                    }
                                QMenu::item:selected{
                                    color:black;
                                    background-color:#C5D7FF;
                                    }
                                QLineEdit {
                                    border: 0px;
                                    padding-left: 1px;
                                    background-color: transparent;
                                           }
''')    

    def Light_mode(self):
        self.setStyleSheet("")
       
    def increase_font(self):
        self.font_size += 0.5
        self.textEdit.setFontPointSize(self.font_size)

    def decrease_font(self):
        self.font_size -= 0.5
        self.textEdit.setFontPointSize(self.font_size)

if __name__== '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()