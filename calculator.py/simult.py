#program to display a multiple line to a variable
varn = ("exp1", "exp2", "exp3")
print(varn)

varn = ["exp1", "exp2", "exp3"]
print(varn)

varn = """
exp1
exp2
exp3
"""
print(varn)

varn = "exp1/nexp2/exp3"
print(varn)


x = 1 # initial value of x is 1
y = 2 #intiial value of y is 2

y, x = x, y # assigning the value of y to x and vice versa (and also x to y)

print(x) # final value is 2
print(y) # final value is 1