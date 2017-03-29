#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "data points in enron_data: ", len(enron_data)
#print "features: ", enron_data[0]
poi = 0
salaried_employees = 0
email_addresses = 0
nan_total_payments = 0
for person in enron_data:
    if enron_data[person]["salary"] != "NaN":
        salaried_employees += 1
    if enron_data[person]["email_address"] != "NaN":
        email_addresses += 1
    if enron_data[person]["total_payments"] == "NaN":# and enron_data[person]["poi"] == True:
        nan_total_payments += 1
    if enron_data[person]["poi"] == True:
        poi += 1

print "salaried employees: ", salaried_employees
print "email addresses: ", email_addresses
print "NaN total payments for poi: ", nan_total_payments
print "poi", poi
print enron_data["SKILLING JEFFREY K"]