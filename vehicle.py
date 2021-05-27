import math
from scipy import integrate
from sympy import *
import matplotlib.pyplot as pl
import numpy as np

class Vehicle(object):
    # 增加一些属性，比如t0，tr，执行时间，
    def __init__(self, name: str, inital_speed: int, acceleration):
        self.name = name
        if inital_speed > 30:
            print("The speed is too high")
            raise ValueError
        if inital_speed < 0:
            print("The speed is too slow")
            raise ValueError
        else:
            self.inital_speed = inital_speed

        if acceleration > 0.5:
            print("The acceleration is too high")
            raise ValueError
        if acceleration < -0.5:
            print("The acceleration is too slow")
            raise ValueError
        else:
            self.acceleration = acceleration
    def get_VehicleName(self):
        return self.name

    def get_Safety_Constraints(self):
        Safety_Constraints = 1.8 * self.speed + 9
        return Safety_Constraints


    def function_between_time_speed(self, T):
        # x = np.linspace(0, 50)
        format_of_speed = self.acceleration * T + self.inital_speed + np.random.normal(scale=0.1)
        # print(format_of_speed)
        return format_of_speed

    def plot_time_speed(self):
        x = np.linspace(0, 50)
        y = []
        for i in range(0, len(x)):
            y.append(self.function_between_time_speed(x[i]))
        pl.plot(x, y)
        pl.show()

    def get_current_position(self, T, y):
        # current_position, err = quad(self.function_between_time_speed(T), 0, T)
        # print("Integral area:", current_position)
        # print(current_position)
        # x = np.linspace(0, 50, 1000)
        # current_position = self.function_between_time_speed(T)
        # pl.axis([np.min(x), np.max(x), 0, np.max(current_position)])
        # pl.fill_between(x, y1=current_position, y2=0, where=(x >= 0.7) & (x <= 4),  # 填充积分区域
        #                  facecolor='blue', alpha=0.2)

        # truth = integrate(self.function_between_time_speed(x), (x, 8, 30)).evalf()
        # print(truth)  # 真值
        n = 50  # 步长,就是将(a,b)区间分为多少个块
        # a = 50
        # b = 0
        h = 1

        current_position = 0
        # (self.function_between_time_speed(a + i * h) + self.function_between_time_speed(a + (i + 1) * h))
        for i in range(0, T - 1):
            current_position += 1 / 2 * h * (y[i] + y[i + 1])  # 梯形积分算法
        print(current_position)  # 梯形积分值

        if 0 < current_position < 200:
            Zone = 1
            print("Vehicle in recequencing zone")
        elif 200 < current_position < 400:
            Zone = 2
            print("Vehicle in control zone")
        else:
            print("out of zone")
        return current_position

    def get_T0(self):
        T0 = (-self.inital_speed + math.sqrt(self.inital_speed * self.inital_speed - 2 * self.acceleration * -200)) / self.acceleration
        print(T0)
        return T0
    Tc = 0
    def get_Tm(self):
        Tm = (-self.inital_speed + math.sqrt(self.inital_speed * self.inital_speed - 2 * self.acceleration * -400)) / self.acceleration
        print(Tm)
        return Tm
    # def function_of_energy_consumption(self):
    #     x = 0.5 * self.acceleration * self.acceleration
    #     print(x)
    #     return x
    #     # 写需要积分的式子
    #
    # # def get_energy_consumption(self):
    # # #     # 积分
    # #     # fArea, err = integrate.quad(Vehicle.function_of_energy_consumption(), Vehicle.get_T0(), Vehicle.get_Tm())
    # #     fArea, err = integrate.quad(self.function_of_energy_consumption(), self.get_T0(), self.get_Tm())
    # #     print("Integral area:", fArea)
    # #     return fArea
    #
    # x = integrate.quad(0.5 * self.acceleration * self.acceleration, get_T0(), get_Tm())
    #
    # # self.fArea, err = integrate.quad(function_of_energy_consumption(), get_T0(), get_Tm())
    # def function_of_energy_consumption(self):
    #     return 0.5 * self.acceleration * self.acceleration
    #
    # def get_energy_consumption(self):
    #     v, err = integrate.quad(self.function_of_energy_consumption(), 1, 2)
    #     print(v)
    #     return v


    # v, err = integrate.quad(function_of_energy_consumption(), 1, 2)
    # print(v)
    def get_energy_consumption(self):
        x = symbols('0.5 * self.acceleration * self.acceleration')
        print(integrate(x, (self.acceleration, 1, 2)))
        return integrate(x, (self.acceleration, 1, 2))






V1 = Vehicle("x", 20, -0.2)
# print(type(V1.get_current_position()))
x = np.linspace(0, 50)
y = []
for i in range(0, len(x)):
    y.append(V1.function_between_time_speed(x[i]))

# x = V1.function_between_time_speed()

V1.get_current_position(50 , y)
# V1.get_Tm()
# V1.get_T0()
# V1.get_energy_consumption()
V1.plot_time_speed()