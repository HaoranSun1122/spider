

class Vehicle(object):
    # 增加一些属性，比如t0，tr，执行时间，
    def __init__(self, name:str, speed:int, acceleration, distance:int):
        self.name = name

        if speed > 30:
            print("The speed is too high")
            raise ValueError
        if speed < 0:
            print("The speed is too slow")
            raise ValueError
        else:
            self.speed = speed

        if acceleration > 3.924:
            print("The acceleration is too high")
            raise ValueError
        if acceleration < -3.924:
            print("The acceleration is too slow")
            raise ValueError
        else:
            self.acceleration = acceleration

        if distance > 500:
            print("Vehicle not enter the resequencing zone")
            raise ValueError
        if distance < 0:
            print("Vehicle run out the control zone ")
            raise ValueError
        else:
            self.distance = distance
        self.TimeArriveM = self.get_TimeArriveM()


    def get_TimeArriveM(self):
        T = self.distance/self.speed
        return T

    def get_VehicleName(self):
        return self.name

    def get_Safety_Constraints(self):
        Safety_Constraints = 1.8 * self.speed + 9
        return Safety_Constraints


ListM = []
ListM.append(Vehicle('VehicleMain1', 50, 200))
ListM.append(Vehicle('VehicleMain2', 50, 250))
ListM.append(Vehicle('VehicleMain3', 30, 300))
ListM.append(Vehicle('VehicleMerge1', 40, 200))
ListM.append(Vehicle('VehicleMerge2', 40, 300))


def partition(arr, low, high):
    i = (low - 1)  # Minimum element index
    pivot = arr[high].TimeArriveM

    for j in range(low, high):
        # The current element is less than or equal to pivot
        if arr[j].TimeArriveM <= pivot:
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

n = len(ListM)
quickSort(ListM, 0, n - 1)


# result of the sorting
print("After sorting:")
for i in range(n):
    print(i, ' Vehicle\'s name:', ListM[i].name,'      Time of arrive merge point:', ListM[i].TimeArriveM)


# consider the safety time Safe time interval
for i in range(0, len(ListM) - 1):
    if ListM[i + 1].TimeArriveM - ListM[i].TimeArriveM < 3:
        ListM[i + 1].TimeArriveM = ListM[i].TimeArriveM + 3
print('-----------')
print('After safety time control:')
for i in range(n):
    print(i, ' Vehicle\'s name:', ListM[i].name, '      Time of arrive merge point:', ListM[i].TimeArriveM)


