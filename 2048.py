from PySide2 import QtWidgets
from PySide2.QtGui import QMovie

from logic import Game
from design.mirror_design import Ui_Form
from design.help_design import Ui_Help
from design.win_design import Ui_Win

x = Game()


class Window2048(QtWidgets.QWidget):
    """Класс описывающий основное окно игры"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.win_ = None
        self.help = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_help.clicked.connect(self.help_)
        self.ui.pushButton_start.clicked.connect(self.start_new_game)
        self.ui.pushButton_up.clicked.connect(self.turn_player)
        self.ui.pushButton_down.clicked.connect(self.turn_player)
        self.ui.pushButton_left.clicked.connect(self.turn_player)
        self.ui.pushButton_right.clicked.connect(self.turn_player)

    def display_output(self):
        """Метод обновляющий значения и фон виджетов основного окна"""
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

        for index, horizontal_layout in enumerate(self.ui.verticalLayout.children()):
            for index_ in range(horizontal_layout.count()):
                value_for_set = x.field[index][index_]
                item = horizontal_layout.itemAt(index_).widget()
                item.setText(str(value_for_set))
                item.setStyleSheet(color_le.get(value_for_set))

    def start_new_game(self):
        """Метод запускающий новую игру"""
        x.clear_fild()
        x.add_two()
        self.ui.lcdNumber.display(x.show_score())
        self.display_output()

    def turn_player(self):
        """Метод выполняющий ход игрока"""
        tern = {"UP": "w",
                "DOWN": "s",
                "LEFT": "a",
                "RIGHT": "d"}
        x.input_play(tern.get(self.sender().text()))
        self.display_output()
        if not x.check_add():
            x.clear_fild()
        if x.check_win():
            self.win()
            x.clear_fild()
        x.add_two()
        self.display_output()
        self.ui.lcdNumber.display(x.show_score())

    def help_(self):
        """Метод открывающий окно с подсказкой"""
        self.help = HelpApp()
        self.help.show()

    def win(self):
        """Метод открывающий окно с поздравлением и гифкой для победителя"""
        self.win_ = WinApp()
        self.win_.show()


class HelpApp(QtWidgets.QWidget):
    """Класс описывающий окно с подсказкой"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Help()
        self.ui.setupUi(self)


class WinApp(QtWidgets.QWidget):
    """Класс описывающий окно с поздравлением с победой"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Win()
        self.ui.setupUi(self)
        movie = QMovie("win.gif")
        self.ui.label.setMovie(movie)
        movie.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = Window2048()
    win.show()

    app.exec_()
