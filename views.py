from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

class DashboardWidget(QWidget):

    def __init__(self):
        super().__init__()

        # Initialize UI elements (using QtWidgets instead of QtGui)
        self.label = QLabel("s", self)
        self.label.setGeometry(150, 60 , 130, 35)

        self.push_button = QPushButton("dashboard msg print", self)
        self.push_button.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(0, 0, 127);")
    
        self.push_button.setGeometry(150, 160, 161, 71)

        # Set overall widget style (optional)
        self.setStyleSheet("background-color: #628ecb; border: none;")

    def updateLable(self, newValue):
        self.label.setText(newValue)



# menu item
class menuItem(QWidget):
    def __init__(self):
        super().__init__()

        self.lable = QLabel("menu", self)
        self.lable.setGeometry(150, 60 , 130, 35)

    def AddMenus(self, MenuList):
        i=0
        for item in MenuList:
            self.lable = QLabel(item, self)
            self.lable.setGeometry(150, (35 + 3 *i) , 130, 35)
            i+=1
        pass