# Create string
x="Ashish"
print(x)

# type of object
print(type(x))

#  Add two string values it work as concatination
x1="Hell0"
x2=x1+" "+x
print(x2)


# Iterate property of string
x2="Hello Ashsish"
for b in range(len(x2)):
    print(x2[b])

# To print in one line
#  So here instead of printong inside for loop we print iutside loop so it will print final output 
# Because here x2[n] here n is position of value sotred inside string it is array of characyer so in loop it only print what will be value of loop
x3=''
for b in range(len(x2)):
    x3=x3+" "+x2[b]
print(x3)   

#  To print in pattern 
x3=''
for b in range(len(x2)):
    x3=x3+x2[b]
    print(x3+str(len(x3)))


# use slicing to print
# Here we write [:c+1] because it starts from 0 to c and forst time c value will be zero
# so it will work as start form 0 and go till 0 so it will print nothibng thats why we used :c+1
x="Hello Ashish"
for c in range(len(x)):
    print(x[:c+1]+" "+str(len(x[:c+1])))

print(len(x))  

# Tp reverse these thing

x="Hello Ashish"
for c in range(len(x)):
    print(x[c:]+" "+str(len(x[c:])))

# To print string reverse
x="Hello"
print(x[-4])

# To print overall string reverse we provide stp only with - and start stop not provide so it will take it as strat to end or just provide : so it wil take wholle string index
print(x[::-1])

print(x[:])

# start from 1 end to 5 and take 2 step  
print(x[1:5:2])

# Immutable string cant be chnage index vlaue
x="Hello"
x[1]="a" # here we get error  'str' object does not support item assignment because str in uimmutable i cna t chage in place


