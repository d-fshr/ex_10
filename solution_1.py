class Circle:
    """
    The Circle class represents circle.

    Attributes:
      pi: Value of Pi.
      all_circles: A list of all circles.
    """

    pi = 3.1415
    all_circles = []

    def __init__(self, rad=1):
        """
        Initialises the circle. Add circle in list of circles.

        :param rad: Radius of circle.
        :return: None
        """

        self.rad = rad
        Circle.all_circles.append(self)

    def area(self):
        """
        Calculate the square of circle.

        :return: square of circle
        """

        return Circle.pi * (self.rad) ** 2
    
    @staticmethod
    def total_area():
        """
        Calculate the summ square of circles.

        :return: summ square of circle
        """

        summ = 0
        for circ in Circle.all_circles:
            summ += circ.area()

        return summ
    
    def __str__(self):
        """
        Return string representation of an object (for users).

        :return: string object
        """

        return f'{self.rad}'
    
    def __repr__(self):
        """
        Return formal string representation of an object (for developers).

        :return: string object
        """
        
        return f'{self.rad}'
