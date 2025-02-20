# Q -> Find the largest of three numbers.


#method 1
# a,b,c = 34,32,44

# max_num = max(a,b,c)
# print(max_num)

# method 2


def largest_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

number = largest_num(32,33,55)
print(number)



