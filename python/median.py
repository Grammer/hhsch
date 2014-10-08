first_arr = []
second_arr = []
arr_num = int(input("Enter the length of an array: "))
for i in range(0, arr_num):
    first_arr.append(int(raw_input("Enter the numbers to first array :")))
for i in range(0, arr_num):
    second_arr.append(int(raw_input("Enter the numbers to second array :")))
final_arr = sorted(first_arr + second_arr)
print final_arr
median = (final_arr[len(final_arr)/2 - 1] + final_arr[len(final_arr)/2])/2
print median
