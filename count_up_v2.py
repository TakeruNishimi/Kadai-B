class MyCounterV2:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value = self.value + self.step


def main():
    counter1 = MyCounterV2(value=5, step=1)
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter2 = MyCounterV2(value=0, step=3)
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)


if __name__ == '__main__':
    main()
