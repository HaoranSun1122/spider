import math
from scipy import integrate
from sympy import *
import matplotlib.pyplot as pl
import numpy as np
from pynverse import inversefunc
import scipy.stats as st
from scipy.optimize import root

# from numpy import *

class Vehicle(object):
    # 增加一些属性，比如t0，tr，执行时间，
    # 添加一个方法，在tr时刻后速度保持不变，加速度为0
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

    def get_current_position(self, T):
        x = symbols('x')
        current_position = integrate(self.function_between_time_speed(x), (x, 0, T)).evalf()
        current_position = round(current_position, 1)
        print(current_position)

        if 0 < current_position < 200:
            Zone = 1
            print("Vehicle in recequencing zone")
        elif 200 < current_position < 400:
            Zone = 2
            print("Vehicle in control zone")
        else:
            print("out of zone")
        return current_position

    def use_to_compute_T0(self, T):
        compute_T0 = self.get_current_position(T)-200
        return compute_T0

    def get_T0(self):
        T0 = root(self.use_to_compute_T0, 0.3)
        T0 = T0.x.tolist()
        T0 = round(T0[0],2)
        return T0
    Tc = 0

    def use_to_compute_Tm(self, T):
        compute_Tm = self.get_current_position(T)-400
        return compute_Tm

    def get_Tm(self):
        Tm = root(self.use_to_compute_Tm, 0.3)
        Tm = Tm.x.tolist()
        Tm = round(Tm[0], 2)
        return Tm

    def compute_instantaneous_acceleration(self, T):
        instantaneous_acceleration = (self.function_between_time_speed(T +0.05) - self.function_between_time_speed(T)) / 0.05
        return instantaneous_acceleration

    def function_of_energy_consumption(self, T):
        # x = 0.5 * self.compute_instantaneous_acceleration(T) * self.compute_instantaneous_acceleration(T)
        print("function_of_energy_consumption is", self.compute_instantaneous_acceleration(T) * self.compute_instantaneous_acceleration(T))
        return abs(0.5 * self.compute_instantaneous_acceleration(T) * self.compute_instantaneous_acceleration(T))
        # 写需要积分的式子

    def get_energy_consumption(self):
        x = symbols('x')
        energy_consumption = integrate(self.function_of_energy_consumption(x), (x, self.get_T0(), self.get_Tm())).evalf()
        energy_consumption = round(energy_consumption, 1)
        print("energy_consumption1 is", energy_consumption)
        energy_consumption = (0.5 * self.acceleration * self.acceleration / (2 * 0.5)) * (self.get_Tm() - self.get_T0()) + energy_consumption
        energy_consumption = round(energy_consumption, 1)
        print("(self.get_Tm() - self.get_T0() is", (self.get_Tm() - self.get_T0()))
        print("energy_consumption is", energy_consumption)
        return energy_consumption

V1 = Vehicle("x", 20, -0.2)
# print(type(V1.get_current_position()))
# x = np.linspace(0, 50)
# y = []
# for i in range(0, len(x)):
#     y.append(V1.function_between_time_speed(x[i]))
# V1.get_current_position(50)
# V1.get_Tm()
# print(V1.get_Tm())
# V1.get_energy_consumption(50, y)
# V1.plot_time_speed()

# print(V1.compute_instantaneous_acceleration(9))
print(V1.get_energy_consumption())

