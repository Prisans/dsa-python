# Q -> Swap two numbers without using temporary variables

# method 1 - 
# a=5
# b=6
# print("a :" ,a , "b :" ,b)
# a,b=b,a
# print("a :" ,a , "b :" ,b)

# method 2 - 

a = 5
b = 6

print("a :" ,a , "b : " ,b)
a = a+b
print("a :" , a)
b=a-b
a=a-b
print("a :" ,a , "b : " ,b)



