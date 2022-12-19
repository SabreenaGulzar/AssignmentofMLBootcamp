#!/usr/bin/env python
# coding: utf-8

# # WAP to accept two numbers from the user and display their sum

# In[2]:


num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(num1 + num2)


# # WAP to accept radius of a Circle from the user and calculate area and circumference

# In[109]:


Radius = float(input("Enter the radius of a circle:"))
area_ofCircle = (3.14*Radius**2)
circum_ofCircle = (2*3.14*Radius)
print("Area of the circle = {0}, Circumference of the circle = {1}".format(area_ofCircle, circum_ofCircle))


# # WAP to accept roll number , grade and percentage as input from the user and display it back

# In[13]:


rollNum = int(input("Enter roll number: "))
Grade = input("Enter Grade: ")
percentage = float(input("Enter Percentage: "))
print("\n Roll Number is: ", rollNum)
print(" Grade is: ", Grade)
print(" Percentage is: ", percentage)


# # Write a program that asks the user to enter his/her name and age. Print out a message , displaying the user’s name along with the year in which they will turn 100 years old

# In[35]:


name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = str(100 - age)
age100year= "20" + year
print("\n Your name is: {0} \n you will turn 100 in: {1}".format(name, age100year))


# # Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# In[39]:


_1stName = input("Enter your first name: ")
_2ndName = input("Enter your last name: ")
rev1 = _1stName[::-1]
rev2 = _2ndName[::-1]
print(rev1, rev2)
 


# # WAP to accept an integer from the user and check whether it is an even or odd

# In[42]:


num = int(input("Enter the integer: "))
if num%2 == 0:
    print("Number is Even.")
else:
    print("Number is Odd.")


# # WAP to accept a character from the user and check whether it is a capital letter or small letter. Assume user will input only alphabets

# In[118]:


alpha = input("Enter alphabets:-> ")
if "A"<=alpha[0]<="Z" :
    print("Entered alphabet: {} is capital letter".format(alpha))
else:
    print("Entered alphabet: {} is small letter".format(alpha))


# # WAP to accept a character from the user and check whether it is a capital letter or small letter or a digit or some special symbol

# In[78]:


char = input("Enter the character: ")
symbols=['@','#','$','%','&','*',"~","!","^","(",")","_","-"]

if char.isdigit():
    print("Digit")
elif char in symbols:
    print("Symbol")
elif char.isupper():
    print("Capital")
else:
    print("Small")



# # WAP to accept 3 integers from the user and without using any logical operator and cascading of relational operators , find out the greatest number amongst them

# In[84]:


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
nest = [num1, num2, num3]
greatestnum = max(nest)
print("Greates number among the three numbers is", greatestnum)


# # Write a program to accept a string from the user and display it vertically but don’t display the vowels in it.

# In[18]:


word = input("Enter the string: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
i = 0
while len(word) > i:
    if word[i] in vowels:
        pass
    else:
        print(word[i])
    i += 1


# In[ ]:





# In[ ]:




