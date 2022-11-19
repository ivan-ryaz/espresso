import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        db = sqlite3.connect('coffee.sqlite')
        self.setWindowTitle('Кофе')
        cursor = db.cursor()
        res = cursor.execute('SELECT * FROM coffes').fetchall()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setHorizontalHeaderLabels([i[0] for i in cursor.description])
        for i, u in enumerate(res):
            for j, k in enumerate(u):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(k)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())