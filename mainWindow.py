from PyQt5 import QtWidgets, uic
import sys



class Ui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        uic.loadUi('UI/mainWindow.ui', self)

        a = 10
        self.pushButtonTestIt.clicked.connect(lambda: self.sumVal(self.lineEditFirstNumber.text(), self.lineEditSecondNumber.text()))
        self.setWindowTitle("Desird Test Case")
        self.show()


    def sumVal(self, firstNum, secondNum):
        try:
            firstNum, secondNum = int(firstNum), int(secondNum)
            if (firstNum >= 0 and firstNum <= 100) and (secondNum >= 0 and secondNum <= 100):
                num = firstNum + secondNum
                print(num)
                self.labelFailOrSuccess.clear()
                numStr = str(num)
                self.labelFailOrSuccess.setText(numStr)
                self.labelinfo.clear()
                return  numStr
            else:
                mess = "Lütfen sayıların 0 - 100 arası olduğuna\ndikkat edin!"
                """self.message("Warning", message=mess,
                                   buttonStatusOk=True)"""
                self.labelinfo.setText(mess)
        except:
            mess = "Sayı dışında karakter algılandı: {}, {}".format(firstNum, secondNum)
            """self.message("Warning", message=mess,
                               buttonStatusOk=True)"""
            self.labelinfo.setText(mess)


    def message(self, mType, message, buttonStatusOk=False, buttonStatusYes=False, buttonStatusNo=False,
                buttonOpen=False, buttonCancel=False):
        messageBox = QtWidgets.QMessageBox()
        # <------ Information / Warning / Question / Critical ------>
        if mType == "Information":
            messageBox.setIcon(QtWidgets.QMessageBox.Information)
        elif mType == "Warning":
            messageBox.setIcon(QtWidgets.QMessageBox.Warning)
        elif mType == "Question":
            messageBox.setIcon(QtWidgets.QMessageBox.Question)
        elif mType == "Critical":
            messageBox.setIcon(QtWidgets.QMessageBox.Critical)

        messageBox.setText(message)
        messageBox.setWindowTitle(mType)
        if not buttonStatusOk == False:
            messageBox.addButton(QtWidgets.QMessageBox.Ok)
        if not buttonStatusYes == False:
            messageBox.addButton(QtWidgets.QMessageBox.Yes)
        if not buttonStatusNo == False:
            messageBox.addButton(QtWidgets.QMessageBox.No)
        if not buttonOpen == False:
            messageBox.addButton(QtWidgets.QPushButton("Open"), QtWidgets.QMessageBox.YesRole)
        if not buttonCancel == False:
            messageBox.addButton(QtWidgets.QPushButton("Cancel"), QtWidgets.QMessageBox.NoRole)

        retval = messageBox.exec_()
        return retval

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()