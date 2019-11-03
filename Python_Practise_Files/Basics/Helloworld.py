""" This module is for variables """

# print("Hello World!!")
#
# # var1        # unsupported
#
# a = b = c = 1  # one value assigned to multiple variables (3 variables) in a single line
#
# print(a, b, c)
#
# print(a)
# print(b)
# print(c)
#
# print(id(a))  # id returns address of the given object
# print(id(b))
# print(id(c))
#
# var1, var2, var3 = "python", 12344, 99.9  # multiple values assigned to multiple variables (3 variables) in a single line
#
# print(var1)
# print(var2)
# print(var3)
#
# print(id(var1))  # id returns address of the given object
# print(id(var2))
# print(id(var3))
#
# x = 1;
# y = "Python";
# print(x);
# print(y)  # Multiple statements can be written in single line using semicolon but its not recommended by PEP 8
#
# str1 = """This is multiline string within three double quotes, python will treat it as a single string and assumes new line \n  when a new line begins.
# It will be printed as entered"""

# print(str1)

# str2 = " This is multiline string within double quotes," \
#        " python will treat it as a single string only if we give \ at the end of each line"
# print(str2)


str_3 = "Python"
print(str_3)          #Prints entire string to console

# print(str_3[0])       #Prints value at 0th index of str_1 i.e. P
# print(str_3[-6])       #Prints value at 0th index of str_1 i.e. P
# print(str_3[3])       #Prints value at 0th index of str_1 i.e. h
# print(str_3[-3])       #Prints value at 0th index of str_1 i.e. h
# print(str_3[5])       #Prints value at 0th index of str_1 i.e. P
# print(str_3[-1])       #Prints value at 0th index of str_1 i.e. n
#
# print(id(str_3))       #Prints the memory address assigned to str_3
# print(type(str_3))     #Prints the datatype of str_3

a = 10
print(a)
print(type(a))

# b = a
# print(b)
# print(type(b))



# b = 10
# print(id(a), id(b))
# print(a is b)         # It will print True as a & b are now holding same addresses
#
#
# b = "python"
# print(b)
# print(id(b))
# print(type(b))
#
# print(a is b)          # It will print False as a & b are now holding different addresses

name_1 = "Python Example"

print(name_1)                     #Python Example
print(name_1[1])                  #y
print(name_1[2])                  #t
print(name_1[1], name_1[-5])      #y, a
print(name_1[4], name_1[-2])      #o, l
print("Empty character is :%s ", name_1[6])




