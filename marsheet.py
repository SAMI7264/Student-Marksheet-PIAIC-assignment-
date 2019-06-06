# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:35:00 2019

@author: Amna Siddiqui
"""

print("Mark sheet Assignment")
#Data of Candidate
name=input("Enter your Name : ")
Father_name=input("Enter your Father name : ")
Class=input("Enter your Class : ")
roll_num=("Enter your Seat Number : ")


eng=int(input("Enter English Marks :"))
math=int(input("Enter Math Marks :"))
chemistry=int(input("Enter Chemistry Marks :"))
physics=int(input("Enter Physics Marks :"))
urdu=int(input("Enter Urdu Marks :"))

# Print All Marks the User will give input
print("\n Name : ",name)
print("\n Father Name : ",Father_name)
print("\n Class : ",Class)
print("\n Seat No.: ",roll_num)
print("==============================================")
print("\n  Result :")
print("English Marks  is    \t:",eng)
print("Math Marks is        \t:",math)
print("Chemistry Marks is   \t:",chemistry)
print("Physics  Marks   is  \t:",physics)
print("Urdu Marks       is  \t:",urdu)

#now we will calculate Total marks and Average
total=eng+math+chemistry+physics+urdu
print(" \n Total Marks Obtained  \t:",total)
average=total/5
print("\n Student Avergae Marks \t:",average)

#Now We will use nested If else condtion to check Percentage of student 
if average >=88:
    print(" \t A Grade")
elif average >=75:
    print(" \t B Grade")
elif average>=60:
    print(" \t C Grade")
else :
    print("Fail ")