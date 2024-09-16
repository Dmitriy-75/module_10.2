from threading import Thread
from time import sleep

class   Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        num_enemy = 100
        print(f'{self.name}, на нас напали ходоки')
        i = 1
        while num_enemy != 0:
            sleep(1)
            num_enemy -= self.power
            print(f'{self.name} сражается {i} день (дня), осталось {num_enemy}  ходоков.')
            i += 1
        print(f'{self.name} одержал победу спустя {i-1} дней (дня) !')


first_knight = Knight('Бриенна Тарт', 10)
second_knight = Knight("Клиган", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились - трындец Белым ходокам!')
