import random
class NavalBattle:
    """
    The NavalBattle class of sea battle game.

    Attributes:
      playing_field: Field for playing.
    """

    playing_field = None
    
    def __init__(self, smbl):
        """
        Initialises the player with symbol of shoting.

        :param smbl: Symbol of shoting.
        :return: None
        """

        if smbl == '~' or smbl == 'o':
            print('Такой символ использовать нельзя!')
        else:
            self.smbl = smbl

    def new_game():
        """
        Creating a playing field, placing ships randomly.

        :return: None
        """

        def vert_can_stay(x_begin, y_begin, ship, field):
            """
            Сhecking the ship can stand vertically in a certain place.

            :param x_begin: The x coordinate of cell from which ship is placed.
            :param y_begin: The y coordinate of cell from which ship is placed.
            :param ship: A list of ship lengths and number.
            :param field: A list of lists in which ships are placed.
            :return: bool
            """

            if y_begin == 0:
                start_y = y_begin
            else:
                start_y = y_begin - 1
            if y_begin + ship[0] + 1 == 11:
                end_y = 10
            else:
                end_y = y_begin + ship[0] + 1
            
            if x_begin == 0:
                start_x = x_begin
            else:
                start_x = x_begin - 1
            if x_begin + 2 == 11:
                end_x = 10
            else:
                end_x = x_begin + 2

            for y in range(start_y, end_y):
                if y < 0 or y > 9:
                    return False
                for x in range(start_x, end_x):
                    if x < 0 or x > 9:
                        return False
                    elif field[y][x] != 0:
                        return False
            
            return True
        
        def hor_can_stay(x_begin, y_begin, ship, field):
            """
            Сhecking the ship can stand horizontally in a certain place.

            :param x_begin: The x coordinate of cell from which ship is placed.
            :param y_begin: The y coordinate of cell from which ship is placed.
            :param ship: A list of ship lengths and number.
            :param field: A list of lists in which ships are placed.
            :return: bool
            """

            if x_begin == 0:
                start_x = x_begin
            else:
                start_x = x_begin - 1
            if x_begin + ship[0] + 1 == 11:
                end_x = 10
            else:
                end_x = x_begin + ship[0] + 1
            
            if y_begin == 0:
                start_y = y_begin
            else:
                start_y = y_begin - 1
            if y_begin + 2 == 11:
                end_y = 10
            else:
                end_y = y_begin + 2

            for x in range(start_x, end_x):
                if x < 0 or x > 9:
                    return False
                for y in range(start_y, end_y):
                    if y < 0 or y > 9:
                        return False
                    elif field[y][x] != 0:
                        return False
            
            return True

        flag = True
        while flag:

            new_field = [[0 for _ in range(10)] for _ in range(10)]
            size_ships = [[4, 1], [3, 2], [2, 3], [1, 4]]
            f = True

            for ship in size_ships:
                for _ in range(ship[1]):
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    pos = random.randint(0, 1)

                    if pos:
                        if vert_can_stay(x, y, ship, new_field):
                            for i in range(y, y + ship[0]):
                                new_field[i][x] = 1
                        else:
                            f = False
                            break
                    else:
                        if hor_can_stay(x, y, ship, new_field):
                            for i in range(x, x + ship[0]):
                                new_field[y][i] = 1
                        else:
                            f = False
                            break

                if f == False:
                    break
            else:
                flag = False
        
        NavalBattle.playing_field = new_field
            

    def shot(self, x, y):
        """
        Player's check shot hit or miss.

        :param x: The x coordinate of the shot.
        :param y: THe y coordinate of the shot.
        :return: None
        """

        x -= 1
        y -= 1
        field = NavalBattle.playing_field

        if field == None:
            print('игровое поле не заполнено')
        else:

            if field[y][x] == 'o' or field[y][x] == self.smbl:
                print('ошибка')
            else:
                if field[y][x] == 1:
                    print('попал')
                    field[y][x] = self.smbl
                    
                elif field[y][x] == 0:
                    print('мимо')
                    field[y][x] = 'o'
    
    @staticmethod
    def show():
        """
        Visualization of the playing field.

        :return: None
        """
        
        field = NavalBattle.playing_field
        show_field = [[0] * 10] * 10
        
        for y in range(len(field)):
            for x in range(len(field[y])):

                if field[y][x] == 0 or field[y][x] == 1:
                    show_field[y][x] = '~'
                else:
                    show_field[y][x] = field[y][x]
            
                print(show_field[y][x], end='')
            print('')
