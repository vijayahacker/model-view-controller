import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLayout, QStackedWidget, QHBoxLayout
from views import DashboardWidget, menuItem

# model
from models import *
from controllers import *

class MainApplication(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # views
        self.dview = DashboardWidget()
        self.mItem = menuItem()

        # model
        self.number = Mynumber()
        self.MenuItems = menuItems()

        # setting up Layouts
        layout = QHBoxLayout()
        self.setWindowTitle("Login")
        self.resize(655, 375)

        self.stackWidget = QStackedWidget()
        
        self.stackWidget.addWidget(self.dview)
        self.stackWidget.addWidget(self.mItem)

        self.stackWidget.setCurrentIndex(0)
        layout.addWidget(self.stackWidget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
                
        # controllers
        DashboardController(self.dview, self.number)
        MenuItemController(self.mItem, self.MenuItems)


    def showDashboard(self):
        self.stackWidget.setCurrentIndex(0)
    def showMenuItem(self):
        self.stackWidget.setCurrentIndex(1)
        
        

if __name__  == "__main__":
    app = QApplication(sys.argv)
    mainApp = MainApplication()
    mainApp.show()
    app.exec_()