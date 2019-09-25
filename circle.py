class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return self.radius * 2 *3.14


def main():
    circle1 = Circle(radius=1)
    print(f'半径が{circle1.radius}cmの円の面積は{circle1.area()}cm^2です。')
    print(f'半径が{circle1.radius}cmの円の円周は{circle1.perimeter()}cmです。')

    circle3 = Circle(radius=3)
    print(f'半径が{circle3.radius}cmの円の面積は{circle3.area()}cm^2です。')
    print(f'半径が{circle3.radius}cmの円の円周は{circle3.perimeter()}cmです。')



if __name__ == '__main__':
    main()
