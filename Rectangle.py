import math
class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width =width

    def area(self):
        area = self.height*self.width
        print('縦が{}、横が{}の長方形の面積は{:.2f}です。'.format(self.height,self.width,area))

    def diagonal(self):
        diagonal =round(math.sqrt((self.height**2) + (self.width**2)),2)
        print(f'縦が{self.height}、横が{self.width}の長方形のまわりのは{diagonal}です。')


def main():
    rectangle1 = Rectangle(height=5, width=6)
    rectangle1.area()
    rectangle1.diagonal()

    rectangle2 = Rectangle(height=3, width=3)
    rectangle2.area()
    rectangle2.diagonal()


if __name__ == '__main__':
    main()