import sys
from PyQt5 import QtWidgets

from form import Ui_MainWindow
from items import Item, pip_list, pip_install, pip_uninstall

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
    
        self.btn_add_item.clicked.connect(self.add_item)
        self.btn_remove_item.clicked.connect(self.del_item)
        self.listWidget.selectionModel().currentChanged.connect(self.update_item_about)
        self.refresh_listWidget()

    def refresh_listWidget(self):
        self.listWidget.clear()
        items = pip_list()
        self.listWidget.addItems([item.title for item in items])

    def update_item_about(self, item):
        item = Item(self.listWidget.itemFromIndex(item).text())
        item.get_about()
        self.textBrowser.setText(str(item.about))

    def add_item(self):
        title, yes = QtWidgets.QInputDialog.getText(self, "Какой модуль установить?", "pip install")
        if yes:
            payload = pip_install(title)
            warningWindow = QtWidgets.QErrorMessage(self)
            warningWindow.showMessage(payload)
            self.refresh_listWidget()

    def del_item(self, title):
        i = self.listWidget.selectionModel().currentIndex()
        title = self.listWidget.itemFromIndex(i).text()
        payload = pip_uninstall(title) # TODO
        warningWindow = QtWidgets.QErrorMessage(self)
        warningWindow.showMessage(payload)
        self.refresh_listWidget()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()