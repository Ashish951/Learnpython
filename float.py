#Python Float 
# To show hex value of float
x=0.1
print(x.hex())
1+2==3

# to pront float value
n=1.5+2.3
print(n)

print(type(n))

# creating more floats through assignment

n1=5.4
print(n2)

# Addition
n2=n+n1
print(n2)

# Subtraction
n3=n2-n1
print(n3)

# Round the result
print(round(n3))

# we are getting multipal values in flpat value is inability to store floating values certain point exactly
print(round(12.456,2))

# multiplicaiton
n4=round(n3,3)
n5=n4*n2
print(n4)

n=1386.49999999999999999999999998*1386.5*6.72222222*float('inf')
print(n)

# Division
# float value divide with fload resiult always will be flaot value
n5=3.678828383+2.7348583447
print(n5)
n6=round(n5,1)

n6=n5/n6
print(n6)

# some badass examples of float calculation
# if we do multiplication of beyong 64 bit precion it will think it is infionite nuymbver bnut it is not and later if we do any 
# any calculaiton using infinite number we always get infinite numbers
# to resolve these issue we use decinaml library or numpy there we get actual precion and fro finance ddata it is always needed proper preciion

n7=1.0
n8=1.0

for x in range (1, 6666):
    n7=n7*x*n5
    n8=n8*x*n6
    print(x*n5)
    print(x*n6)
    print(n7)
    print(n8)
    print(n7-n6)


# cponverting number into floa and string also

n=float(5)
n=float('3')
print(n)

# float method to store value in numberator and denominator format

x=0.5
print(x.as_integer_ratio())
