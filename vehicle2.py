import math
from scipy import integrate
from sympy import *
import matplotlib.pyplot as pl
import numpy as np
from pynverse import inversefunc
import scipy.stats as st
from scipy.optimize import root

class Vehicle(object):
    # 增加一些属性，比如t0，tr，执行时间，
    # 添加一个方法，在tr时刻后速度保持不变，加速度为0
    def __init__(self, name: str, inital_speed: int, T_initial: int):
        self.name = name
        if inital_speed > 30:
            print("The speed is too high")
            raise ValueError
        if inital_speed < 0:
            print("The speed is too slow")
            raise ValueError
        else:
            self.inital_speed = inital_speed

        if T_initial < 0:
            print("The initial is error")
            raise ValueError
        else:
            self.T_initial = T_initial

    def get_VehicleName(self):
        return self.name

    def get_T_resequencing(self):
        T_resequencing = 200 / self.inital_speed + self.T_initial
        T_resequencing = round(T_resequencing, 2)
        print('T_resequencing is ', T_resequencing)
        return T_resequencing

    def get_Tm_Uniform_speed(self):
        Tm_Uniform_speed = 500 / self.inital_speed + self.T_initial
        float(Tm_Uniform_speed)
        Tm_Uniform_speed = round(Tm_Uniform_speed, 2)
        print('Tm_Uniform_speed is', Tm_Uniform_speed)
        return Tm_Uniform_speed

    # def get_T_during_resequencing(self):
    #     T_during_resequencing = 0
    #     # 变速所需时间
    #     return T_during_resequencing
    #
    # def get_acceleration(self):
    #     # 加速度
    #     acceleration = 0
    #     return acceleration

    def get_final_speed(self):
        final_speed = self.inital_speed + self.get_acceleration() * self.get_T_during_resequencing()
        return final_speed

    def get_Tm(self):
        Tm = self.T_initial + self.get_T_during_resequencing() + 200 / self.get_final_speed()
        return Tm

    # def function_of_energy_consumption_uniform_speed(self):
    #     return self.inital_speed * self.inital_speed * (self.get_Tm_Uniform_speed() - self.get_T_resequencing())
    #
    # def get_Energy_Consumption_Uniform_speed(self):
    #     x = symbols('x')
    #     Energy_Consumption_Uniform_speed = integrate(self.function_of_energy_consumption_uniform_speed(), (x, self.get_T_resequencing(), self.get_Tm_Uniform_speed())).evalf()
    #     Energy_Consumption_Uniform_speed = round(Energy_Consumption_Uniform_speed, 2)
    #     print("Energy_Consumption_Uniform_speed is", Energy_Consumption_Uniform_speed)
    #     return Energy_Consumption_Uniform_speed

# def energy_consumption(vehicle, List_Main, List_Ramp, List_All):
#     if List_Main[1].
#     return



Vehicle_Main_1 = Vehicle('Vehicle_Main_1', 20, 0)
Vehicle_Main_2 = Vehicle('Vehicle_Main_2', 25, 7)
Vehicle_Ramp_1 = Vehicle('Vehicle_Ramp_1', 23, 3)
Vehicle_Ramp_2 = Vehicle('Vehicle_Ramp_2', 22, 5)
Vehicle_Ramp_3 = Vehicle('Vehicle_Ramp_3', 22, 7)



# List_Main = []
# # 主干道车辆
# List_Ramp = []
# # 匝道车辆
List_All = []
# List_Main.append(Vehicle_Main_1)
# List_Main.append(Vehicle_Main_2)
# List_Ramp.append(Vehicle_Ramp_1)
# List_Ramp.append(Vehicle_Ramp_2)
# List_Ramp.append(Vehicle_Ramp_3)
#
#
# if List_Main[0].get_T_resequencing() < List_Ramp[0].get_T_resequencing():
#     List_All.append(List_Main[0])
#     List_Main.remove(List_Main[0])
# else:
#     List_All.append(List_Ramp[0])
#     List_Ramp.remove(List_Ramp[0])

List_All = []
List_All.append(Vehicle_Main_1)
List_All.append(Vehicle_Main_2)
List_All.append(Vehicle_Ramp_1)
List_All.append(Vehicle_Ramp_2)
List_All.append(Vehicle_Ramp_3)

for i in range(len(List_All)):
    print(List_All[i].get_Tm_Uniform_speed())

def partition(arr, low, high):
    i = (low - 1)  # Minimum element index
    pivot = arr[high].get_Tm_Uniform_speed()

    for j in range(low, high):
        # The current element is less than or equal to pivot
        if arr[j].get_Tm_Uniform_speed() <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> Sorted array
# low  --> Starting index
# high  --> End index

# sort function
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

n = len(List_All)
quickSort(List_All, 0, n - 1)


# result of the sorting
print("After sorting:")
for i in range(n):
    print(i, ' Vehicle\'s name:', List_All[i].name,'      Time of arrive merge point:', List_All[i].get_Tm_Uniform_speed())

for i in range(len(List_All)):
    print(List_All[i].get_Tm_Uniform_speed())

# 匀速情况下能量消耗
def function_of_energy_consumption_uniform_speed(inital_speed, Tm_Uniform_speed, T_resequencing):
    return inital_speed * inital_speed * (Tm_Uniform_speed - T_resequencing)

def get_Energy_Consumption_Uniform_speed(inital_speed, Tm_Uniform_speed, T_resequencing):
    x = symbols('x')
    Energy_Consumption_Uniform_speed = integrate(function_of_energy_consumption_uniform_speed(inital_speed, Tm_Uniform_speed, T_resequencing), (x, T_resequencing, Tm_Uniform_speed)).evalf()
    Energy_Consumption_Uniform_speed = round(Energy_Consumption_Uniform_speed, 2)
    print("Energy_Consumption_Uniform_speed is", Energy_Consumption_Uniform_speed)
    return Energy_Consumption_Uniform_speed

# 计算加速度方法
def Calculate_acceleration(initial_speed, Target_time, Resequence_time):
    during_resequencing = 3
    distance = 300
    acceleration = (distance - initial_speed * during_resequencing - (initial_speed * (Target_time - Resequence_time - during_resequencing))) / (0.5 * during_resequencing *during_resequencing + during_resequencing * (Target_time - Resequence_time - during_resequencing))
    acceleration = round(acceleration, 2)
    return acceleration


def function_of_energy_consumption(initial_speed, Resequence_time, acceleration):
    during_resequencing = 3
    Control_Zone_Distance = 300 - (initial_speed * during_resequencing + 0.5 * acceleration * during_resequencing * during_resequencing)
    Control_Zone_speed = initial_speed + acceleration * Resequence_time
    Control_Zone_Time = Control_Zone_Distance / Control_Zone_speed
    return initial_speed * initial_speed * during_resequencing + 0.5 * acceleration * acceleration * during_resequencing + Control_Zone_Time * Control_Zone_speed * Control_Zone_speed

def get_Energy_Consumption(initial_speed, Resequence_time, acceleration, Target_time):
    x = symbols('x')
    Energy_Consumption = integrate(function_of_energy_consumption(initial_speed, Resequence_time, acceleration), (x, Resequence_time, Target_time)).evalf()
    Energy_Consumption = round(Energy_Consumption, 2)
    print("Energy_Consumption", Energy_Consumption)
    return Energy_Consumption


print('--------------------------------------')

# List_All内的第二辆车能量消耗
Energy_Consumption_1 = []

# 不变的情况下能量消耗
Energy_Consumption_1.append(get_Energy_Consumption_Uniform_speed(List_All[1].inital_speed, List_All[1].get_Tm_Uniform_speed(), List_All[1].get_T_resequencing()))
print('Energy_Consumption_1', Energy_Consumption_1)

# 超越前车情况下能量消耗
# 对第2辆车进行判断能量消耗
# 加速度
acceleration_1 = []
acceleration = Calculate_acceleration(List_All[1].inital_speed, List_All[0].get_Tm_Uniform_speed(), List_All[1].get_T_resequencing())
acceleration_1.append(acceleration)
print(acceleration_1)
Energy_Consumption_1.append(get_Energy_Consumption(List_All[2].inital_speed, List_All[2].get_T_resequencing(), acceleration_1[0], List_All[0].get_Tm_Uniform_speed()))
print('Energy_Consumption_1', Energy_Consumption_1)

print('--------------------------------------')
# List_All内的第三辆车能量消耗
Energy_Consumption_2 = []
# 不变的情况下能量消耗

Energy_Consumption_2.append(get_Energy_Consumption_Uniform_speed(List_All[1].inital_speed, List_All[1].get_Tm_Uniform_speed(), List_All[1].get_T_resequencing()))
print('Energy_Consumption_2', Energy_Consumption_2)
# 超越前车情况下能量消耗
# 对第2辆车进行判断能量消耗
# 加速度
acceleration_2 = []
acceleration = Calculate_acceleration(List_All[2].inital_speed, List_All[0].get_Tm_Uniform_speed(), List_All[2].get_T_resequencing())
acceleration_2.append(acceleration)
print(acceleration_2)
Energy_Consumption_2.append(get_Energy_Consumption(List_All[2].inital_speed, List_All[2].get_T_resequencing(), acceleration_2[0], List_All[0].get_Tm_Uniform_speed()))
print(Energy_Consumption_2)

acceleration = Calculate_acceleration(List_All[2].inital_speed, List_All[1].get_Tm_Uniform_speed(), List_All[2].get_T_resequencing())
acceleration_2.append(acceleration)
print(acceleration_2)
Energy_Consumption_2.append(get_Energy_Consumption(List_All[2].inital_speed, List_All[2].get_T_resequencing(), acceleration_2[1], List_All[1].get_Tm_Uniform_speed()))
print(Energy_Consumption_2)

print('--------------------------------------')
# List_All内的第四辆车能量消耗
Energy_Consumption_3 = []
# 不变的情况下能量消耗
Energy_Consumption_3.append(get_Energy_Consumption_Uniform_speed(List_All[3].inital_speed, List_All[3].get_Tm_Uniform_speed(), List_All[3].get_T_resequencing()))
print('Energy_Consumption_3', Energy_Consumption_3)
# 超越前车情况下能量消耗
# 对第2辆车进行判断能量消耗
# 加速度
acceleration_3 = []
acceleration = Calculate_acceleration(List_All[3].inital_speed, List_All[0].get_Tm_Uniform_speed(), List_All[3].get_T_resequencing())
acceleration_3.append(acceleration)
print(acceleration_3)
Energy_Consumption_3.append(get_Energy_Consumption(List_All[3].inital_speed, List_All[3].get_T_resequencing(), acceleration_3[0], List_All[0].get_Tm_Uniform_speed()))
print(Energy_Consumption_3)

acceleration = Calculate_acceleration(List_All[3].inital_speed, List_All[1].get_Tm_Uniform_speed(), List_All[3].get_T_resequencing())
acceleration_3.append(acceleration)
print(acceleration_3)
Energy_Consumption_3.append(get_Energy_Consumption(List_All[3].inital_speed, List_All[3].get_T_resequencing(), acceleration_3[1], List_All[1].get_Tm_Uniform_speed()))
print(Energy_Consumption_3)

acceleration = Calculate_acceleration(List_All[3].inital_speed, List_All[2].get_Tm_Uniform_speed(), List_All[3].get_T_resequencing())
acceleration_3.append(acceleration)
print(acceleration_3)
Energy_Consumption_3.append(get_Energy_Consumption(List_All[3].inital_speed, List_All[3].get_T_resequencing(), acceleration_3[2], List_All[2].get_Tm_Uniform_speed()))
print(Energy_Consumption_3)

print('--------------------------------------')
# List_All内的第五辆车能量消耗
Energy_Consumption_4 = []
# 不变的情况下能量消耗
Energy_Consumption_4.append(get_Energy_Consumption_Uniform_speed(List_All[4].inital_speed, List_All[4].get_Tm_Uniform_speed(), List_All[4].get_T_resequencing()))
print('Energy_Consumption_4', Energy_Consumption_4)
# 超越前车情况下能量消耗
# 对第2辆车进行判断能量消耗
# 加速度
acceleration_4 = []
acceleration = Calculate_acceleration(List_All[4].inital_speed, List_All[0].get_Tm_Uniform_speed(), List_All[4].get_T_resequencing())
acceleration_4.append(acceleration)
print(acceleration_4)
Energy_Consumption_4.append(get_Energy_Consumption(List_All[4].inital_speed, List_All[4].get_T_resequencing(), acceleration_4[0], List_All[0].get_Tm_Uniform_speed()))
print(Energy_Consumption_4)

acceleration = Calculate_acceleration(List_All[4].inital_speed, List_All[1].get_Tm_Uniform_speed(), List_All[4].get_T_resequencing())
acceleration_4.append(acceleration)
print(acceleration_4)
Energy_Consumption_4.append(get_Energy_Consumption(List_All[4].inital_speed, List_All[4].get_T_resequencing(), acceleration_4[1], List_All[1].get_Tm_Uniform_speed()))
print(Energy_Consumption_4)

acceleration = Calculate_acceleration(List_All[4].inital_speed, List_All[2].get_Tm_Uniform_speed(), List_All[4].get_T_resequencing())
acceleration_4.append(acceleration)
print(acceleration_4)
Energy_Consumption_4.append(get_Energy_Consumption(List_All[4].inital_speed, List_All[4].get_T_resequencing(), acceleration_4[2], List_All[2].get_Tm_Uniform_speed()))
print(Energy_Consumption_4)

acceleration = Calculate_acceleration(List_All[4].inital_speed, List_All[3].get_Tm_Uniform_speed(), List_All[4].get_T_resequencing())
acceleration_4.append(acceleration)
print(acceleration_4)
Energy_Consumption_4.append(get_Energy_Consumption(List_All[4].inital_speed, List_All[4].get_T_resequencing(), acceleration_4[3], List_All[3].get_Tm_Uniform_speed()))
print(Energy_Consumption_4)

print('----------------------------------')
print("After sorting:")
for i in range(n):
    print(i, ' Vehicle\'s name:', List_All[i].name,'      Time of arrive merge point:', List_All[i].get_Tm_Uniform_speed())

for i in range(len(List_All)):
    print(List_All[i].get_Tm_Uniform_speed())