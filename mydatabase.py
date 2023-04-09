import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mylist = [
    {"FIRST_NAME" : "Steven", "LAST_NAME" : "King", "EMAIL" : "SKING", "PHONE_NUMBER" : "515.123.4567", "HIRE_DATE" : "1987-06-17", "JOB_ID" : "AD_PRES", "SALARY" : "24000.00", "COMMISSION_PCT" : "0.00", "MANAGER_ID" : "0", "DEPARTMENT_ID" : "90"},
    {"FIRST_NAME" : "Neena", "LAST_NAME" : "Kochhar", "EMAIL" : "NKOCHHAR", "PHONE_NUMBER" : "515.123.4568", "HIRE_DATE" : "1987-06-17", "JOB_ID" : "AD_VP", "SALARY" : "17000.00", "COMMISSION_PCT" : "0.00", "MANAGER_ID" : "1", "DEPARTMENT_ID" : "90"},
    {"FIRST_NAME" : "Lex", "LAST_NAME" : "De Haan", "EMAIL" : "LDEHAAN", "PHONE_NUMBER" : "515.123.4597", "HIRE_DATE" : "1987-06-17", "JOB_ID" : "AD_VP", "SALARY" : "17000.00", "COMMISSION_PCT" : "0.00", "MANAGER_ID" : "1", "DEPARTMENT_ID" : "60"},
    {"FIRST_NAME" : "Alexander", "LAST_NAME" : "Hunold", "EMAIL" : "AHUNOLD", "PHONE_NUMBER" : "515.123.4564", "HIRE_DATE" : "1987-06-17", "JOB_ID" : "IT_PROG", "SALARY" : "6000.00", "COMMISSION_PCT" : "0.00", "MANAGER_ID" : "1", "DEPARTMENT_ID" : "60"}
]

x = mycol.insert_many(mylist)
for n in x:
    print(x)