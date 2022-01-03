# -*- coding: utf-8 -*-
"""lab3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ot9gYXWbXtsIJ2R2Ds8fZjI4qUSqBoi-

1. Write a Python program to find those numbers which 
are divisible by 7 and multiple of 5, between 7and 
270 (both included)
"""

l=[]
for x in range(7, 270):
    if (x%7==0) and (x%5==0):
        l.append(str(x))
print (l)

"""2. Write a Python program to count the number of even 
and odd numbers from a series of numbers ex(1,5)
Input last number of series: 5
Output odd: 3
Output even: 2
"""

#numbers = [1, 2, 3, 4, 5]
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print(count_even)
print(count_odd)

"""3. Write a Python program to display numbers from (-10 
,0)
"""

i = -10
while(i<=0):
    print(i)
    i += 1

"""4. Write a Python program to find factorial any number 
Input: 4
Output: 24
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input(" "))
print(factorial(n))

"""5. Write a Python program to find cube of range of 
numbers ex :6 find cube to each number from 1 to 6
"""

num = int(input(" "))
cb = num*num*num
print(cb)

"""6. Given a number N. Print N lines that describes iti 
game.
Input N: 3
Output
1 2 3 iti
5 6 7 iti
9 10 11 iti
"""

n = int(input(" "))
for i in range(1,4*n+1):
  if i%4==0:
    print("iti\n")
  else:
     print(i)

"""7. Write a Python program to count the sum of digits in 
a number
Input:123
Output:
"""

n = int(input(" "))
count = 0
 
while(n > 0):
    a = n % 10
    count=count + a
    n = n // 10
 
print(count)

"""8. Write a Python program to reverse any number 
Input: 123
Output: 321
"""

n = int(input(" "))
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print(rev)

"""

10. Write a program to check an integer is a palindrome 
or not. An integer is a palindrome when it reads the same 
forward as backward
Input: 123
Output: no
Input: 111
Output: ye
"""

num=int(input(" "))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("yes")
else:
    print("No")

