
class vector2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print(self):
        print((self.x,self.y))

    def __repr__(self):
        return f'x={self.x},y={self.y}'

    def __add__(self, vector2):
        return vector2d(self.x+vector2.x, self.y+vector2.y)




def main():
    vector2d1 = vector2d(5, 5)
    vector2d2 = vector2d(8,4)
    print(vector2d1)
    print(vector2d1+vector2d2)
    vector2d1.print()


if __name__ == '__main__':
    main()