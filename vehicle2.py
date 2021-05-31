from scipy import integrate
from sympy import *


class Vehicle(object):
    def __init__(self, name: str, inital_speed: int, T_initial: int):
        self.name = name
        # Speed limit
        if inital_speed > 30:
            print("The speed is too high")
            raise ValueError
        if inital_speed < 0:
            print("The speed is too slow")
            raise ValueError
        else:
            self.inital_speed = inital_speed
        # Entry time must not be less than 0
        if T_initial < 0:
            print("The initial is error")
            raise ValueError
        else:
            self.T_initial = T_initial

    def get_VehicleName(self):
        return self.name

    # The moment when the reordering starts
    def get_T_resequencing(self):
        T_resequencing = 200 / self.inital_speed + self.T_initial
        T_resequencing = round(T_resequencing, 2)
        print('T_resequencing is ', T_resequencing)
        return T_resequencing

    # The moment of reaching the meeting point at a constant speed
    def get_Tm_Uniform_speed(self):
        Tm_Uniform_speed = 500 / self.inital_speed + self.T_initial
        float(Tm_Uniform_speed)
        Tm_Uniform_speed = round(Tm_Uniform_speed, 2)
        return Tm_Uniform_speed

    # Optimal speed after sorting
    def get_final_speed(self):
        final_speed = self.inital_speed + self.get_acceleration() * self.get_T_during_resequencing()
        return final_speed

    # Time to reach the meeting point after sorting
    def get_Tm(self):
        Tm = self.T_initial + self.get_T_during_resequencing() + 200 / self.get_final_speed()
        return Tm


# Instantiate the class, assuming 5 cars
Vehicle_Main_1 = Vehicle('Vehicle_Main_1', 20, 0)
Vehicle_Main_2 = Vehicle('Vehicle_Main_2', 25, 7)
Vehicle_Ramp_1 = Vehicle('Vehicle_Ramp_1', 23, 3)
Vehicle_Ramp_2 = Vehicle('Vehicle_Ramp_2', 22, 5)
Vehicle_Ramp_3 = Vehicle('Vehicle_Ramp_3', 22, 7)


# List of all vehicles in
List_All = []
List_All.append(Vehicle_Main_1)
List_All.append(Vehicle_Main_2)
List_All.append(Vehicle_Ramp_1)
List_All.append(Vehicle_Ramp_2)
List_All.append(Vehicle_Ramp_3)

# Quick sort, according to the time of arrival at the meeting point
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

# Energy consumption at constant speed
def function_of_energy_consumption_uniform_speed(inital_speed, Tm_Uniform_speed, T_resequencing):
    return inital_speed * inital_speed * (Tm_Uniform_speed - T_resequencing)

def get_Energy_Consumption_Uniform_speed(inital_speed, Tm_Uniform_speed, T_resequencing):
    x = symbols('x')
    Energy_Consumption_Uniform_speed = integrate(function_of_energy_consumption_uniform_speed(inital_speed, Tm_Uniform_speed, T_resequencing), (x, T_resequencing, Tm_Uniform_speed)).evalf()
    Energy_Consumption_Uniform_speed = round(Energy_Consumption_Uniform_speed, 2)
    print("Energy_Consumption_Uniform_speed is", Energy_Consumption_Uniform_speed)
    return Energy_Consumption_Uniform_speed

# Calculation method of acceleration
def Calculate_acceleration(initial_speed, Target_time, Resequence_time):
    during_resequencing = 3
    distance = 300
    acceleration = (distance - initial_speed * during_resequencing - (initial_speed * (Target_time - Resequence_time - during_resequencing))) / (0.5 * during_resequencing *during_resequencing + during_resequencing * (Target_time - Resequence_time - during_resequencing))
    acceleration = round(acceleration, 2)
    return acceleration

# Energy consumption when acceleration changes
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

# Energy consumption of the second car in List_All，Include overtaking and non-overtaking
Energy_Consumption_1 = []

# Energy consumption without overtaking
Energy_Consumption_1.append(get_Energy_Consumption_Uniform_speed(List_All[1].inital_speed, List_All[1].get_Tm_Uniform_speed(), List_All[1].get_T_resequencing()))
print('Energy_Consumption_1', Energy_Consumption_1)

# Energy consumption in the case of overtaking the preceding vehicle
# Judge the energy consumption of the second car
# Calculate acceleration
acceleration_1 = []
acceleration = Calculate_acceleration(List_All[1].inital_speed, List_All[0].get_Tm_Uniform_speed(), List_All[1].get_T_resequencing())
acceleration_1.append(acceleration)
print(acceleration_1)
Energy_Consumption_1.append(get_Energy_Consumption(List_All[2].inital_speed, List_All[2].get_T_resequencing(), acceleration_1[0], List_All[0].get_Tm_Uniform_speed()))
print('Energy_Consumption_1', Energy_Consumption_1)

print('--------------------------------------')
# Energy consumption of the third car in List_All
Energy_Consumption_2 = []
# Energy consumption without change

Energy_Consumption_2.append(get_Energy_Consumption_Uniform_speed(List_All[1].inital_speed, List_All[1].get_Tm_Uniform_speed(), List_All[1].get_T_resequencing()))
print('Energy_Consumption_2', Energy_Consumption_2)
# Energy consumption in the case of overtaking the preceding vehicle
# # Judging the energy consumption of the second car
# # Acceleration
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
# List_All in the fourth car energy consumption
Energy_Consumption_3 = []
# Energy consumption without change
Energy_Consumption_3.append(get_Energy_Consumption_Uniform_speed(List_All[3].inital_speed, List_All[3].get_Tm_Uniform_speed(), List_All[3].get_T_resequencing()))
print('Energy_Consumption_3', Energy_Consumption_3)
# Energy consumption in the case of overtaking the preceding vehicle
# Judging the energy consumption of the second car
# Acceleration
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
# List_All the energy consumption of the fifth car in
Energy_Consumption_4 = []
# Energy consumption without change
Energy_Consumption_4.append(get_Energy_Consumption_Uniform_speed(List_All[4].inital_speed, List_All[4].get_Tm_Uniform_speed(), List_All[4].get_T_resequencing()))
print('Energy_Consumption_4', Energy_Consumption_4)
# Energy consumption in the case of overtaking the preceding vehicle
# Judging the energy consumption of the second car
# Acceleration
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
# Print the final result
print('----------------------------------')
print("After sorting:")
for i in range(n):
    print(i, ' Vehicle\'s name:', List_All[i].name,'      Time of arrive merge point:', List_All[i].get_Tm_Uniform_speed())