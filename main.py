import sys
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.print_db()

    def print_db(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.setQuery(QSqlQuery("""SELECT coffee.id as 'ID',
        coffee.title as 'Название',
        coffee.roasting as 'Обжарка',
        beans.bean as 'Состояние',
        coffee.description as 'Вкус',
        coffee.price as 'Цена',
        coffee.volume as 'Объем (в мл)' FROM coffee
        INNER JOIN beans
        ON beans.id = coffee.bean
        """))
        self.table_db.setModel(model)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())