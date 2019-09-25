class MyCounterV3:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value = self.value + self.step

    def count_down(self):
        self.value =self.value - self.step


def main():
    counter1 = MyCounterV3(value=1, step=2)
    print(counter1.value)  # 1

    counter1.count_up()
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter1.count_down()
    print(counter1.value)

    counter2 = MyCounterV3(value=10, step=4)
    print(counter2.value)

    counter2.count_down()
    print(counter2.value)

    counter2.count_down()
    print(counter2.value)


if __name__ == '__main__':
    main()
