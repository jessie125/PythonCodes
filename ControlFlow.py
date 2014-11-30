import os
import sys

print "Study control flow!"


def max(a, b):
    if a > b:
        return a
    else:
        return b

x = 10
y = 15
z = max(x, y)
print z


def grade(num):
    if num >= 81 and num <= 100:
        return "Grade A"
    if num >= 61 and num <= 80:
        return "Grade B"
    if num >= 41 and num <= 60:
        return "Grade C"
    if num >= 21 and num <= 40:
        return "Grade D"
    if num >= 0 and num <= 20:
        return "Grade E"

b = grade(80)
print b
print grade(0)

print "-------------------------------"

def grade2(num):
    if num >= 81 and num <= 100:
        return "Grade A"
    elif num >= 61 and num <= 80:
        return "Grade B"
    elif num >= 41 and num <= 60:
        return "Grade C"
    elif num >= 21 and num <= 40:
        return "Grade D"
    else:
        return "Grade E"


print grade2(0)

print "-------------------------------"


def max2(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
        

print max2(5, 6, 7)

    
