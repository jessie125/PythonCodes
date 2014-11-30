import os
import sys

print "NieChao, Hello World!"

x = 8
y = 4
z = x / y
print z

a = (x * x) / (y * y)
print a

a = 0.0129 * 100
print a

def secondsOfYear():
    d = 365
    h = 24
    m = 60
    s = 60
    t = d * h * m * s
    return t

a = secondsOfYear()
print a
print secondsOfYear()

def secondsOfYears(years, needPrint):
    d = 365
    h = 24
    m = 60
    s = 60
    t = years * d * h * m * s
    if needPrint:
        print t
    return t

print "-----------------------"
a = secondsOfYears(3, True)
a = secondsOfYears(3, False)




