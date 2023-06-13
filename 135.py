class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        self.__x = x
        self.__y = y
 
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())
# print(pt._x, pt._y)


# pt = Point
# print('pt = ', pt)
# print('pt.__dict__ = ', pt.__dict__)

# print()
# print()

# pt2 = Point()
# print('pt2 = ', pt2)
# print('pt2.__dict__ = ', pt2.__dict__)

# print()
# print()

# pt2.set_coords(1, 2)
# print('pt2.__dict__  2= ', pt2.__dict__)

# print()
# print()

# setattr(pt2, 'color22', 'blue')
# print('pt2.__dict__ 3= ', pt2.__dict__)
