class RomanNumber:

    def __init__(self, value):
        """
        Initialises the roman number.

        :param value: Roman number.
        :return: None
        """
        
        if RomanNumber.is_int(value):
            self.int_value = value
            self.rom_value = self.roman_number()
        elif type(value) == str and RomanNumber.is_roman(value):
            self.rom_value = value
            self.int_value = self.decimal_number()
        else:
            print('ошибка')
            self.rom_value = None
            self.int_value = None
    
    def __add__(self, other):
        """
        Defining the addition method.

        :param other: Another number.
        :return: RomanNumber object
        """

        if self.int_value != None and other.int_value != None:

            dec_num = self.int_value + other.int_value
            return RomanNumber(dec_num)
    
    def __sub__(self, other):
        """
        Defining the difference method.

        :param other: Another number.
        :return: RomanNumber object
        """

        if self.int_value != None and other.int_value != None:

            dec_num = self.int_value - other.int_value
            return RomanNumber(dec_num)
    
    def __mul__(self, other):
        """
        Defining the multiplication method.

        :param other: Another number.
        :return: RomanNumber object
        """

        if self.int_value != None and other.int_value != None:

            dec_num = self.int_value * other.int_value
            return RomanNumber(dec_num)
    
    def __truediv__(self, other):
        """
        Defining true division method.

        :param other: Another number.
        :return: RomanNumber object
        """

        if self.int_value != None and other.int_value != None:

            dec_num = self.int_value / other.int_value
            if int(dec_num) == dec_num:
                dec_num = int(dec_num)
            return RomanNumber(dec_num)
        
    def __floordiv__(self, other):
        """
        Defining floor division method.

        :param other: Another number.
        :return: RomanNumber object
        """

        if self.int_value != None and other.int_value != None:

            dec_num = self.int_value // other.int_value
            return RomanNumber(dec_num)
        
    def __mod__(self, other):
        """
        Defining the remainder of the division method.

        :param other: Another number.
        :return: RomanNumber object
        """

        if self.int_value != None and other.int_value != None:

            dec_num = self.int_value % other.int_value
            return RomanNumber(dec_num)
    
    def __pow__(self, other):
        """
        Defining the exponentiation method.

        :param other: Another number.
        :return: RomanNumber object
        """

        if self.int_value != None and other.int_value != None:

            dec_num = self.int_value ** other.int_value
            return RomanNumber(dec_num)
        
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
    
    def roman_number(self):
        """
        Сonverts decimal number to roman.

        :return: Roman number.
        """

        rom_num = ''
        int_num = self.int_value
        dec_num_value = [
            [1000, 'M'],
            [900, 'CM'],
            [500, 'D'],
            [400, 'CD'],
            [100, 'C'],
            [90, 'XC'],
            [50, 'L'],
            [40, 'XL'], 
            [10, 'X'],
            [9, 'IX'],
            [5, 'V'],
            [4, 'IV'],
            [1, 'I']
        ]

        if self.int_value != None:

            for num_value in dec_num_value:
                while int_num >= num_value[0]:
                    int_num -= num_value[0]
                    rom_num += num_value[1]
                
            return rom_num
            
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
            if all(num * 4 not in value for num in roman_num) and 'VV' not in value  and 'DD' not in value:
                return True
        return False
    
    @staticmethod
    def is_int(value):
        """
        Сhecking whether the number is decimal.

        :param value: Decimal number.
        :return: bool
        """

        return type(value) == int and 0 < value < 4000
