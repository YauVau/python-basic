def my_func (s_1, s_2, s_3):
    tmp_array = [s_1, s_2, s_3]
    tmp_array.sort()
    return tmp_array[1] + tmp_array[2]
print (my_func(int(input("number 1: ")), int(input("number 2: ")), int(input("number 3: "))))