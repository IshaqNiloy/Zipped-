class BuiltIns():
    def __init__(self, my_list):
        self.my_list = my_list

    def find_average(self):
       #'*' is an unpacking operator
        another_my_list = list(zip(*my_list))

        for lst in another_my_list:
            print(sum(lst)/len(lst)) 

if __name__ == '__main__':
    nx = input().split()
    n = int(nx[0])
    x = int(nx[1])
    my_list = []
    for _ in range(x):
        temp_list = input().split()
        my_list.append([float(i) for i in temp_list])

    my_object = BuiltIns(my_list)
    my_object.find_average()

