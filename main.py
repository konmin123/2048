import random


class Game:
    @staticmethod
    def start():
        x = Field()
        while x.chek_add():
            x.add_two()
            x.print_field()
            x.input_play(input())
            x.print_field()
            if x.chek_win():
                print('Поздравляю!!!')
                break



class Field:
    def __init__(self):
        self.field = [[2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4]]

    def print_field(self):
        for line in self.field:
            print(line)
        print("-" * 10)

    def chek_add(self) -> bool:
        for line in self.field:
            if 0 in line:
                return True
        else:
            return False

    def chek_win(self) -> bool:
        for line in self.field:
            if 128 in line:
                return True
        else:
            return False

    def add_two(self):
        list_of_moves = []
        for index_list, list_ in enumerate(self.field):
            for index_value, value in enumerate(list_):
                if value == 0:
                    list_of_moves.append([index_list, index_value])
        target_for_add = list_of_moves[random.randint(0, len(list_of_moves)-1)]
        self.field[target_for_add[0]][target_for_add[1]] = 2
        return self.field

    def tern_left(self):
        new_list = [[], [], [], []]
        for index_list, list_ in enumerate(self.field):
            for index_value, value in enumerate(list_):
                new_list[(len(self.field)-1)-index_value].append(value)
        self.field = new_list

    def merge_left(self):
        self.sort_for_merge()
        for index_list in range(4):
            for index_value in range(3):
                if self.field[index_list][index_value] == 0:
                    break
                if self.field[index_list][index_value] == self.field[index_list][index_value + 1]:
                    self.field[index_list][index_value] *= 2
                    self.field[index_list].pop(index_value + 1)
                    self.field[index_list].append(0)

    def merge_right(self):
        self.tern_left()
        self.tern_left()
        self.merge_left()
        self.tern_left()
        self.tern_left()

    def merge_up(self):
        self.tern_left()
        self.merge_left()
        self.tern_left()
        self.tern_left()
        self.tern_left()

    def merge_down(self):
        self.tern_left()
        self.tern_left()
        self.tern_left()
        self.merge_left()
        self.tern_left()

    def sort_for_merge(self):
        new_list = [[], [], [], []]
        for index_list, list_ in enumerate(self.field):
            count = 0
            for index_value, value in enumerate(list_):
                if value == 0:
                    new_list[index_list].append(0)
                else:
                    new_list[index_list].insert(count, value)
                    count += 1
        self.field = new_list

    def player_move(self, side):
        if side == 1:
            ...
        else:
            for i in range(4 - side):
                print(i)

    def input_play(self, input_):
        if input_ == 'w' or 'W':
            self.merge_up()
        if input_ == 's' or 'S':
            self.merge_down()
        if input_ == 'a' or 'A':
            self.merge_left()
        if input_ == 'd' or 'D':
            self.merge_right()


if __name__ == '__main__':
    x = Field()
    x.print_field()
    x.merge_down()
    x.print_field()
