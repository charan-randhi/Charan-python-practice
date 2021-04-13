#!/usr/bin/env python
# coding: utf-8

# ITP,NPV,EDA,STATS,ML 
# 
# 1.Proctor violation exceeds 5 attempts test will be terminated.
# 
# 2.The test will run in a proctored mode and you will not be allowed to go out of the test window. Failing to adhere to this will result in auto-submission of the test
# 
# 3.Once the ‘Start Test’ button is clicked the test timer will start
# 
# 4.The test can only be taken in the fullscreen mode. Disabling the fullscreen will pause the test but not the timer
# 
# 5.All the responses are automatically updated to the server at the time of test submission
# 
# 6.Please kindly off all the update notifications pop-ups during the test duration, if something pops up it consider a full-screen violation.
# 
# 7.Please kindly have proper internet connectivity while taking the test with at least upload speed/download speed more than 1 Mbps.
# 
# 8.Copy-paste within the test window is permitted, if not able to do and the cell is markdown kindly double tap on the cell once the cell is raw convert can copy-paste, external content copy-paste is not permitted/allowed.
# 
# 9.ESC can't be used/work during the exam time.
# 
# 10.Right click over a keypad/mouse should/can not be used.
# 
# 11. Please maintain an internet speed of least 1 Mbps if possible higher than 5 mbps of upload speed before starting test.
#  

# # Section A : 2 Mark Questions : 2 * 3 = 6 Marks

# ### 1. Write a code snippet to concatenate firstname and lastname and display the output, (where both are of string datatype)

# In[61]:


a='charles'
b='darwin'
print(a+b)


# ### 2. Write a code snippet to replace ‘hai’ into ‘hello’ in the given list.
# lis=['hai','world',43,56]

# In[62]:


lis=['hai','world',43,56]
lis[0]='hello'
lis


# ### 3. Write a code snippet to add “alpha”:26 to the existing dictionary.
# dic={'Eddy':13,'Maria':44,'Jas':21}

# In[4]:


dic={'Eddy':13,'Maria':44,'Jas':21}
dic.update({'alpha':26})
dic


# # SECTION B – 3 mark questions  3*8 = 24 marks

# ### 4. Write a program to print only the even numbers till 11.
# 
#    
# 
# 
# 

# In[63]:


for i in range(0,11,2):
    print(i)


# ### 5. Write a program to print “Python” for multiples of three instead of the number, “Coding” for the multiples of five, “Python Coding” for multiples of both three and five (range is from 1 to 26).

# In[64]:


for i in range(1,26):
    if (i%3==0 and i%5==0):
        print(i,"python coding")
    elif i%3==0:
        print(i,'python')
    elif i%5==0:
        print(i,'coding')


# ### 6. Write a program to display “hello world” 5 times without changing the given while condition (while count<=10).

# In[65]:


a='hello world'
count=1
while count<=10:
    print(a)
    count=count+2


# ### 7. Write a program to find the factors of 24?

# In[66]:


num=24
factors=[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)
print(factors)


# ### 8. Write a program to i) extract name elements alone, ii) multiply the number element by 6.07, iii) check whether  the name element is carbon (use map). 
# d=[{'name':'hydrogen','number':1,'weight':1.0},{'name':'carbon','number':2,'weight':4.002}]

# In[67]:


d=[{'name':'hydrogen','number':1,'weight':1.0},{'name':'carbon','number':2,'weight':4.002}]
print(d[0]['name'],d[1]['name'])
print(d[0]['number']*6.07,d[1]['number']*6.07)
d1=list(map(lambda d:d['name']=='carbon',d))
d1


# ### 9. Write a Program to print inverted half pyramid using an asterisk (star) (get the row count from the user).

# In[68]:


rows=int(input("enter number of rows: "))
for i in range(rows):
    print(' * ' *(rows-i))


# ### 10. Write a Python Program to swap the first and last elements in the list
# 1.	Get the input count of "number of elements in a list" 
# 2.	Get the input of the elements one by one and create a list
# 3.	Create a  program to swap the first and last elements in the list
# 4.	Display the results of the list before and after
# 

# In[69]:


a=int(input("no.of elements needed:"))
l1=[]
for i in range(0,a):
    b=int(input("enter elements : "))
    l1.append(b)
print("list before swapping is : ", l1)
c=l1[0]
l1[0]=l1[a-1]
l1[a-1]=c
print("the list after swapping is ",l1)
    


# ### 11. Write a program that accepts a string from the user and calculate the number of digits and letters present in the string.
# 

# In[70]:


user=input("enter any string ")
d=0
l=0
for i in user:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass
print("letters ",l)
print("digits ",d)


# In[ ]:




