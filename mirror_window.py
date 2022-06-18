from mirror_design import Ui_Form
from main import Game, Field
from PySide2 import QtWidgets, QtCore

x = Field()


class MirrorWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.t = TestThread()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_help.clicked.connect(self.help)
        self.ui.pushButton_start.clicked.connect(self.start_game)
        self.ui.pushButton_up.clicked.connect(self.turn_players)
        self.ui.pushButton_down.clicked.connect(self.turn_players)
        self.ui.pushButton_left.clicked.connect(self.turn_players)
        self.ui.pushButton_right.clicked.connect(self.turn_players)

    def display_output(self):
        self.ui.le00.setText(str(x.field[0][0]))
        self.ui.le01.setText(str(x.field[0][1]))
        self.ui.le02.setText(str(x.field[0][2]))
        self.ui.le03.setText(str(x.field[0][3]))
        self.ui.le10.setText(str(x.field[1][0]))
        self.ui.le11.setText(str(x.field[1][1]))
        self.ui.le12.setText(str(x.field[1][2]))
        self.ui.le13.setText(str(x.field[1][3]))
        self.ui.le20.setText(str(x.field[2][0]))
        self.ui.le21.setText(str(x.field[2][1]))
        self.ui.le22.setText(str(x.field[2][2]))
        self.ui.le23.setText(str(x.field[2][3]))
        self.ui.le30.setText(str(x.field[3][0]))
        self.ui.le31.setText(str(x.field[3][1]))
        self.ui.le32.setText(str(x.field[3][2]))
        self.ui.le33.setText(str(x.field[3][3]))

    def help(self):
        print('Помоги себе сам')

    def start_game(self):
        x = Field()
        self.display_output()

    def turn_players(self):
        tern = {"UP": "w",
                "DOWN": "s",
                "LEFT": "a",
                "RIGHT": "d"}
        x.input_play(tern.get(self.sender().text()))
        self.display_output()
        x.add_two()
        self.display_output()
        self.ui.lcdNumber.display(x.show_score())


# class TestThread(QtCore.QThread):
#     def run(self):
#         x = Field()
#         self.display_output()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MirrorWindow()
    win.show()

    app.exec_()