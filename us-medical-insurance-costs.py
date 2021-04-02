#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# # Background
#    US Medical Costs are for a section of the US public are provided on a CSV file called 'insurance.csv'. The file contains information such as age, sex, BMI, # of children, whether or not they are a smoker, what region they live in (broken down to: Northeast, Northwest, Southeast, Southwest), and their costs. The goal of the project is two-fold: 1.) Showcase a mastery in Python basics and 2.)Develop one's own answers to questions. 

# # Project Scope
#     My goal in this exercise with the data provided is to answer the following questions:
#     1.) Which age demographic (broken down below) has the lowest insurance cost?
#     2.) What is the average BMI within each region?
#     
#     Graph the results as we go along to demonstrate mastery in a Python module (Numpy and Seaborn).
#     
#  Age ranges for demographics: 18 - 24, 25 - 34, 35 - 44, 45 - 54, 55 and older

# # Predictions
#     The lowest average insurance cost for an age demographic will be the 25 - 34 year age range
#     The average BMI for each region: 
#                     Southwest: 25.2
#                     Southeast: 29.0
#                     Northwest: 23.9
#                     Northeast: 26.5

# In[1]:


# import the modules we need
import csv


# In[2]:


# Generate lists based on the categories within the dataset to parse through later

with open('insurance.csv') as insurance:
    insurance_dict = {}
    
    csvreader = csv.reader(insurance, delimiter = ',')
    fieldnames = next(csvreader)
    age = []
    sex = []
    bmi = []
    num_children = []
    smoker_status = []
    region = []
    charges = []
    
    for i in csvreader:
        age.append(i[0])
        sex.append(i[1])
        bmi.append(i[2])
        num_children.append(i[3])
        smoker_status.append(i[4])
        region.append(i[5])
        charges.append(i[6])
#test one to make sure I have the information extracted
#print(len(age))
#returns 1338
unique_keys = list(range(0,1337,1))
#print(unique_keys)


# Now that we have the information we need to start looking into our data, I'm going to break down and the age groups into a dictionary, using the len we had from age to generate a unique dictionary key. 

# In[10]:


# Build the dictionary


def build_medical_dictionary(unique_keys, age, sex, bmi, num_children, smoker_status, region, charges):
    medical_ins_data = {}
    for i in unique_keys:
        medical_ins_data[unique_keys[i]] = {"Age": age[i],
                                           "Sex": sex[i],
                                           "BMI": bmi[i],
                                           "Number of Children": num_children[i],
                                           "Smoker Status": smoker_status[i],
                                           "Region": region[i],
                                           "Charges": charges[i]}
    return medical_ins_data

medical_data = build_medical_dictionary(unique_keys, age, sex, bmi, num_children, smoker_status, region, charges)

# Check to make sure I did this right....
print(medical_data)


# Now that we have our data organized better into a dictionary, we can tackle the demographic - cost relationship. We will define our demographic data, split the costs into lists, and anaylze the average cost based on demographic. 

# In[11]:


# Defining the demographics cost: 

eighteen_to_twenty_four = 0
twenty_five_to_thirty_four = 0
thirty_five_to_forty_four = 0
forty_five_to_fifty_four = 0
fifty_five_and_older = 0

def charge_splitter(medical_data):
    cost = medical_ins_data["Cost"[i]]
    for i in medical_data['Age'[i]] in medical_data['Cost'[i]]:
        if 18 >= age <= 24:
            eighteen_to_twenty_four += cost
        elif 25 >= age <= 34:
            twenty_five_to_thirty_four += cost
        elif 35 >= age <= 44:
            thirty_five_to_forty_four += cost
        elif 45 >= age <= 45:
            forty_five_to_fifty_four += cost
        else:
            fifty_five_and_older += cost
    return cost      

print(eighteen_to_twenty_four)
print(twenty_five_to_thirty_four)
print(thirty_five_to_forty_four)
print(forty_five_to_fifty_four)
print(fifty_five_and_older)


# In[ ]:




