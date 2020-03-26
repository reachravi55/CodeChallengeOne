user_input_lst = [int(i) for i in input().split()]
user_input_number = int(input())
var_string = [str(i) for i in user_input_lst]
var_join = int("".join(var_string))
var_join += user_input_number
output = [int(x) for x in str(var_join)]
print(output)
