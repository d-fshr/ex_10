class NavalBattle:
    """
    The NavalBattle class of sea battle game.

    Attributes:
      playing_field: Field for playing.
    """

    playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                     [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
    
    
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

    def shot(self, x, y):
        """
        Player's check shot hit or miss.

        :param x: The x coordinate of the shot.
        :param y: THe y coordinate of the shot.
        :return: None
        """

        x -= 1
        y -= 1
        
        if NavalBattle.playing_field[y][x] == 1:
            print('попал')
            NavalBattle.playing_field[y][x] = self.smbl
            
        elif NavalBattle.playing_field[y][x] == 0:
            print('мимо')
            NavalBattle.playing_field[y][x] = 'o'
    
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
