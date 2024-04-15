class RomanNumber:
    """
    The RomanNumber class of roman numbers.
    """

    def __init__(self, value):
        """
        Initialises the roman number.

        :param value: Roman number.
        :return: None
        """

        if RomanNumber.is_roman(value):
            self.rom_value = value
        else:
            print('ошибка')
            self.rom_value = None
        
    def decimal_number(self):
        """
        Сonverts roman number to decimal.

        :return: Decimal number.
        """

        dec_num = 0
        roman_num_value = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        

        if self.rom_value != None:

            for num in range(len(self.rom_value)):
                if num != 0 and roman_num_value[self.rom_value[num]] > roman_num_value[self.rom_value[num - 1]]:
                    dec_num += roman_num_value[self.rom_value[num]] - 2 * roman_num_value[self.rom_value[num - 1]]
                else:
                    dec_num += roman_num_value[self.rom_value[num]]

            return dec_num
        
        return None
    
    def __str__(self):
        """
        Return string representation of an object (for users).

        :return: string object
        """

        return f'{self.rom_value}'
    
    def __repr__(self):
        """
        Return formal string representation of an object (for developers).

        :return: string object
        """
        
        return f'{self.rom_value}'

    @staticmethod
    def is_roman(value):
        """
        Сhecking whether the number is roman.

        :param value: Roman number.
        :return: bool
        """

        roman_num = 'IVXLCDM'
        if all(num in roman_num for num in value):
            if all(num * 4 not in value for num in roman_num) and 'VV' not in value and 'DD' not in value:
                return True
        return False
