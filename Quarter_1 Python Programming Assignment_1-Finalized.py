#!/usr/bin/env python
# coding: utf-8

# #                           Python Programming Assignment 1
# 
# #                                                  Quarter 1
# 
# #              AI-101 Fundamentals of Programming using Python

# ### Name: Kashan Qazi
# 
# ### Roll No: AIC006023
# 
# ### center: Sindh Boy Scouts Association
# 
# ### Day/Time: Sunday - 6:45 PM to 9:45 PM
# 
# ### Instructor Name: Sir. Muhammad Qasim
# 
# ### Batch 1

# # 1. Calculate Area of a Cirle:

# In[1]:


a = float(input("Enter the Radius Of Circle: "))
print("Area of cirlce is : ", 3.141592654 * a * a)


# # 2. Check Number either positive, negative or zero:

# In[2]:


b = int(input("Enter the Number: "))
if b < 0:
    print("Negative Number Entered")
elif b > 0:
    print("Positive Number Entered")
else:
    print("Zero Number Entered")


# In[3]:


b = int(input("Enter the Number: "))
if b < 0:
    print("Negative Number Entered")
elif b > 0:
    print("Positive Number Entered")
else:
    print("Zero Number Entered")


# In[4]:


b = int(input("Enter the Number: "))
if b < 0:
    print("Negative Number Entered")
elif b > 0:
    print("Positive Number Entered")
else:
    print("Zero Number Entered")


# # 3. Divisibility Check of two numbers:

# In[5]:


c = int(input("Enter Numerator: "))
d = int(input("Enter Denominator: "))
if c % d  == 0:
    print("Number", c , "is Completely Divisible by", d)
else:
     print("Number", c , "is not Completely Divisible by", d)


# In[6]:


c = int(input("Enter Numerator: "))
d = int(input("Enter Denominator: "))
if c % d  == 0:
    print("Number", c , "is Completely Divisible by", d)
else:
     print("Number", c , "is not Completely Divisible by", d)


# # 4. Days Calculator:

# In[7]:


from datetime import datetime
date_format = "%d/%m/%Y"
e = input("Enter a date in (dd/mm/yy) Format: ")
f = input("Enter a date in (dd/mm/yy) Format: ")
a = datetime.strptime( e , date_format)
b = datetime.strptime( f , date_format)
delta = b - a
print ("There are", delta.days, "days in Between", e , "and" , f)


# In[8]:


from datetime import datetime
date_format = "%d/%m/%Y"
e = input("Enter a date in (dd/mm/yy) Format: ")
f = input("Enter a date in (dd/mm/yy) Format: ")
a = datetime.strptime( e , date_format)
b = datetime.strptime( f , date_format)
delta = b - a
print ("There are", delta.days, "days in Between", e , "and" , f)


# # 5. Calculate volume of Sphere:

# In[9]:


a = int(input("Enter the Radius of Sphere: "))
print("Volume of the Sphere with radius" , a , "is:", 4 / 3 * 3.141592654 * a * a * a)


# # 6. Copy String N Times:

# In[10]:


e = str(input("Enter string: "))
b = int(input("How many Copies of String you need: "))
if b > 0:
    print(b,"Copies of", e , "are :" , b * e)        
else:
    print("you Entered Invalid number of Copies:")


# # 7. Checking If Number is Even or Odd:

# In[11]:


a = int(input("Enter Number: "))
if a % 2 == 0:
    print(a, "is Even")
else:
    print(a, "is Odd")


# In[12]:


a = int(input("Enter Number: "))
if a % 2 == 0:
    print(a, "is Even")
else:
    print(a, "is Odd")


# # 8. Vowel Tester:

# In[13]:


f = input("Enter Character: ")
c = f.lower()
if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" :
    print(f, "is Vowel")
else:
    print(f, "is not Vowel")


# In[14]:


f = input("Enter Character: ")
c = f.lower()
if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" :
    print(f, "is Vowel")
else:
    print(f, "is not Vowel")


# In[15]:


f = input("Enter Character: ")
c = f.lower()
if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" :
    print(f, "is Vowel")
else:
    print(f, "is not Vowel")


# # 9. Triangle Area:

# In[16]:


a = int(input("Enter Magnitude of Triangle Base:"))
b = int(input("Enter Magnitude of Triangle Height:"))
print("Area of a Triangle with Height",b,"and Base",a," :", a * b / 2)


# # 10. Calculate Interest:

# In[18]:


a = int(input("Please Enter Principle Amount: "))
b = float(input("Please Enter rate of interest in %: "))
c = int(input("Enter Number of years for Investment: "))
e = 0
f = a * b
while e < c:
    f += f * b 
    e += 1
print("After",c,"years your principal amount",a,"over an interest rate of",b,"% will be",f)


# # 11. Euclidean Distance:

# In[19]:


import math
a = int(input("Enter Co-ordinate for X1: "))
b = int(input("Enter Co-ordinate for X2: "))
c = int(input("Enter Co-ordinate for Y1: "))
d = int(input("Enter Co-ordinate for Y2: "))
g = (a - b)*(a - b) + (c - d)*(c - d)
e = math.sqrt(g)
print("Distance Between Points (", a , "," , c , ") and (" ,b, "," , d , ") is: ",e)


# # 12. Feet to Centimeter Converter:

# In[20]:


a = float(input("Enter Height in Feet: "))
print("There are", a * 30.48,"cm","in",a,"ft" )


# # 13. BMI Calculator:

# In[21]:


a = float(input("Enter Your Height in CM: "))
b = float(input("Enter Your Weight in KG: "))
c = a * 0.01
print("Your BMI is: ", b / (c * c))


# # 14. Sum of N Positive Integers:

# In[25]:


a = int(input("Enter value of n: "))
i = 1
total = 0
while i <= a:
    total += a
    i += 1 
    
print(total)


# # 15. Digits Sum of Numbers:

# In[26]:


a = str(input("Enter a Number: "))
b = 0 
for x in a:
    b += int(x)
print("Sum of", '+'.join(map(str,a)) ,"is: ",b)


# # 16. Decimal To Binary Converter:

# In[27]:


a = int(input("Enter a Decimal number: "))
e = bin(a)
print("Binary Reperesentation of",a,"is: ", e[2:])


# In[28]:


a = int(input("Enter a Decimal number: "))
e = bin(a)
print("Binary Reperesentation of",a,"is: ", e[2:])


# # 17. Binary To Decimal Converter:

# In[29]:


a = input("Enter a Binary number: ")
e = int(a,2)
print("Decimal Reperesentation of",a,"is: ",e)


# In[30]:


a = input("Enter a Binary number: ")
e = int(a,2)
print("Decimal Reperesentation of",a,"is: ",e)


# # 18. Vowel and Consonants Counter:

# In[31]:


a = input("Enter Text: ")
c = a.lower()
d = 0
f = 0
for x in c:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        d += 1
    else:
        f += 1
print("Vowels: ",d)
print("Consonants: ",f)


# # 19. Palindrome Tester:

# In[32]:


a = input("Enter Text: ")
if a == a[::-1]:
    print("Text",a,"is Palindrome. ")
else:
    print("Text ",a,"is Not Palindrome. ")


# In[33]:


a = input("Enter Text: ")
if a == a[::-1]:
    print("Text",a,"is Palindrome. ")
else:
    print("Text ",a,"is Not Palindrome. ")


# # 20. Count Alphabets,Numbers and Special Characters:

# In[34]:


a = input("Enter Text: ")
e = 0
d = 0
c = 0
f = 0
for x in a:
    if int(ord(x)) >= 65 and int(ord(x)) <= 122:
        e += 1
    elif int(ord(x)) >= 48 and int(ord(x)) <= 57:
        d += 1
    elif x == " ":
        f += 1
    else:
        c += 1
print("Alphabets:          ",e)
print("Numbers:            ",d)
print("Special Characters: ",c)
print("Space:              ",f)


# # 21. Pattern 1:

# In[35]:


f = 1
i = 0
while i <= 9:
    d = '*'
    print(d * f)
    f += 1
    i += 1


# In[36]:


f = 9
i = 0
while i <= 9:
    d = '*'
    print(d * f)
    f -= 1
    i += 1


# In[37]:


f1 = 1
i1 = 0
f2 = 4
i2 = 0
while i1 <= 4:
    d = '*'
    print(d * f1)
    f1 += 1
    i1 += 1
while i2 < 4:
    d = '*'
    print(d * f2)
    f2 -= 1
    i2 += 1


# # 22. Pattern 2:

# In[38]:


i = 6
d = 0
for x in range(1,i):
    for y in range(1, x + 1):
        print (y , end = " ")
    print(" ")
for r in range(4,d,-1):
    for c in range(1, r + 1):
        print (c , end = " ")
    print(" ")


# # 23. Pattern 3:

# In[39]:


for i in range(10):
    for f in range(i):
        print(i, end = ' ')
    print(" ")

