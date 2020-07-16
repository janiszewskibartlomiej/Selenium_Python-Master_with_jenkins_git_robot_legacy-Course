# Programming Solutions
# Interchange variable values using 3rd Variable

#  Take input number from User 
 
input_num_a = int(input("Please enter your first number --- > "))
input_num_b = int(input("Please enter your second number --- > "))
 
# We are using 3rd variable
c =  input_num_a
input_num_a = input_num_b
input_num_b = c
 
# After change first value is
print("After changing value, first value is =  " + str(input_num_a))
 
 
# After change second value is
print("After changing value, second value is =  " + str(input_num_b))


# Interchange variable values without using 3rd Variable



#  Take input number from User
 
input_num_a = int(input("Please enter your first number --- > "))
input_num_b = int(input("Please enter your second number --- > "))
 
# We are not using 3rd variable
 
input_num_a = input_num_a + input_num_b
input_num_b = input_num_a- input_num_b
input_num_a = input_num_a- input_num_b
 
# After change first value is
print("After changing value, first value is =  " + str(input_num_a))
 
 
# After change second value is
print("After changing value, second value is =  " + str(input_num_b))


Print * Rectangle

#  Print * Rectangle
 
for i in range(1,6):
    for j in range(1, 6):
        print("*",end='')    #  By default line ended with new line, here we define, nothing to be added at the end of line
    print()
Print * Rectangle with hollow inside

#  Print * Rectangle
 
for i in range(1,6):
    for j in range(1, 6):
        if(i==1 or i==5):
            print("*",end='')    #  By default line ended with new line, here we define, nothing to be added at the end of line
        else:
            if(j==1 or j==5):
                print("*", end='')
            else:
                print(" ", end='')
    print()




# Print table of given number but only display number where multiple is not divisible of 3, 5, 7

#  Take input number from User
 
input_num = int(input("Please enter your number --- > "))
 
# Print table of given number but only display number where multiple is not divisible of 3, 5, 7
 
for i in range(1,11):
    num = input_num * i
 
    if(num%3!=0 and num%5!=0 and num%7!=0):
        print(num)


# Practical Programming - 4 : Write program to find factorial of a number

#  Take input from User and generate factorial result
z=1
x=int(input("Please enter your number :  - "))
while(x>0):
    z=z*x
    x=x-1
print("Factorial result is : " + str(z))
 


# Practical Programming - 5 : Write program to Generate Fibonacci series

#  Take input from User and generate fabonnaci series
 
x=int(input("Please enter your number :  - "))
 
#  Define initial 2 values
a=0
b=1
print(a)
print(b)
while((a+b) < x):
     b=a+b
     a=b-a
     print(b)


# Practical Programming - 6 : Write program to check Number is Prime or Not

#  Take input from User and Check number is Prime number or not
 
x=int(input("Please enter your number :  - "))
 
z=0
for i in range (2,x):
    if(x%i==0):
        print("Its not a Prime number")
        z=1
        break
    i=i+1
if(z==0):
    print("This is Prime number")
