from PySide2 import QtWidgets, QtCore

from logic import Game
from mirror_design import Ui_Form
x = Game()


class MirrorWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_help.clicked.connect(self.help)
        self.ui.pushButton_start.clicked.connect(self.start_new_game)
        self.ui.pushButton_up.clicked.connect(self.turn_player)
        self.ui.pushButton_down.clicked.connect(self.turn_player)
        self.ui.pushButton_left.clicked.connect(self.turn_player)
        self.ui.pushButton_right.clicked.connect(self.turn_player)

    def display_output(self):
        color_le = {2: 'background-color: LemonChiffon',
                    4: 'background-color: PapayaWhip',
                    8: 'background-color: PeachPuff',
                    16: 'background-color: LightSalmon',
                    32: 'background-color: Salmon',
                    64: 'background-color: DarkSalmon',
                    128: 'background-color: Coral',
                    256: 'background-color: Tomato',
                    512: 'background-color: Crimson',
                    1024: 'background-color: FireBrick',
                    2048: 'background-color: DarkRed'}

        self.ui.le00.setText(str(x.field[0][0]))
        self.ui.le00.setStyleSheet(color_le.get(x.field[0][0]))
        self.ui.le01.setText(str(x.field[0][1]))
        self.ui.le01.setStyleSheet(color_le.get(x.field[0][1]))
        self.ui.le02.setText(str(x.field[0][2]))
        self.ui.le02.setStyleSheet(color_le.get(x.field[0][2]))
        self.ui.le03.setText(str(x.field[0][3]))
        self.ui.le03.setStyleSheet(color_le.get(x.field[0][3]))
        self.ui.le10.setText(str(x.field[1][0]))
        self.ui.le10.setStyleSheet(color_le.get(x.field[1][0]))
        self.ui.le11.setText(str(x.field[1][1]))
        self.ui.le11.setStyleSheet(color_le.get(x.field[1][1]))
        self.ui.le12.setText(str(x.field[1][2]))
        self.ui.le12.setStyleSheet(color_le.get(x.field[1][2]))
        self.ui.le13.setText(str(x.field[1][3]))
        self.ui.le13.setStyleSheet(color_le.get(x.field[1][3]))
        self.ui.le20.setText(str(x.field[2][0]))
        self.ui.le20.setStyleSheet(color_le.get(x.field[2][0]))
        self.ui.le21.setText(str(x.field[2][1]))
        self.ui.le21.setStyleSheet(color_le.get(x.field[2][1]))
        self.ui.le22.setText(str(x.field[2][2]))
        self.ui.le22.setStyleSheet(color_le.get(x.field[2][2]))
        self.ui.le23.setText(str(x.field[2][3]))
        self.ui.le23.setStyleSheet(color_le.get(x.field[2][3]))
        self.ui.le30.setText(str(x.field[3][0]))
        self.ui.le30.setStyleSheet(color_le.get(x.field[3][0]))
        self.ui.le31.setText(str(x.field[3][1]))
        self.ui.le31.setStyleSheet(color_le.get(x.field[3][1]))
        self.ui.le32.setText(str(x.field[3][2]))
        self.ui.le32.setStyleSheet(color_le.get(x.field[3][2]))
        self.ui.le33.setText(str(x.field[3][3]))
        self.ui.le33.setStyleSheet(color_le.get(x.field[3][3]))

    @QtCore.Slot()
    def help(self):
        print('Помоги себе сам')

    @QtCore.Slot()
    def start_new_game(self):
        x.clear_fild()
        x.add_two()
        self.ui.lcdNumber.display(x.show_score())
        self.display_output()

    @QtCore.Slot()
    def turn_player(self):
        tern = {"UP": "w",
                "DOWN": "s",
                "LEFT": "a",
                "RIGHT": "d"}
        x.input_play(tern.get(self.sender().text()))
        self.display_output()
        x.add_two()
        self.display_output()
        self.ui.lcdNumber.display(x.show_score())


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MirrorWindow()
    win.show()

    app.exec_()
