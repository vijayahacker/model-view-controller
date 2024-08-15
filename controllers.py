class DashboardController():
    def __init__(self, view, model):
        self.view = view
        self.model = model
        print("setting ui click", self.model.getNumber())
        self.view.dview.push_button.clicked.connect(self.handleClick)
        pass

    def handleClick(self):
        print("clicked")
        self.model.IncrementNumber()

class MenuItemController():
    def __init__(self, view, model):
        self.view = view
        self.model = model
        pass