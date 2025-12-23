from fastapi import FastAPI,HTTPException
from model_val import Employee
from typing import List


#fast api->web framework for building api
#data validation->pydantic
#web framework-> starlette
#web server->uvicorn

#so web app is is made by web framework live on a web server and then the web app is interacted by the user and data is validate

#to run we do uvicorn file_name:app --reload      we do --reload as if we change any line of code we will not need to restart the server  {app=FastAPI()}


#this is just a empty list that is a temporary database 
#Every employee we add will be stored here
employee_db:List[Employee]=[]

app=FastAPI()

#read all employee (get operation)

#response_model-> your data will be in this format 
@app.get('/employees',response_model=List[Employee])
def get_employee():
    return employee_db

#read specific employees
#URL has /{emp_id} → means we can pass an ID like /employees/2
@app.get('/employees/{emp_id}',response_model=Employee)
def get_employee(emp_id:int):
    for index,employee in enumerate(employee_db):
        if employee.id==emp_id:
            return employee_db[index]
    raise HTTPException(status_code=404,detail='Employee not found')

#add an employee 
#The function takes new_employee as input and check whether it already exist or not 
#it also get validated through the response_model 
@app.post('/employees',response_model=Employee)
def add_employee(new_employee:Employee):
    for emp in employee_db:
        if emp.id==new_employee.id:
            raise HTTPException(status_code=400,detail='already there')
    employee_db.append(new_employee) 
    return new_employee

#update ->PUT
#URL takes an ID (emp_id), and we also send new data (updated_employee)
#if exist we update the data of the employee
@app.put('/update_emp/{emp_id}',response_model=Employee)
def update_emp(emp_id:int ,updated_employee:Employee):
    for index,employee in enumerate(employee_db):
        if emp_id==employee.id:
            employee_db[index]=updated_employee
            return updated_employee
    raise HTTPException(status_code=404,detail="employee does not exist")

# delete
#we look for the id and if found we remove it 
@app.delete('/delete_emp/{emp_id}')
def delete_emp(emp_id:int):
    for index,employee in enumerate(employee_db):
        if emp_id==employee.id:
            del employee_db[index]
            return {'message':'employee delted successfully'}
    raise HTTPException(status_code=404,detail="employee does not exist")
   

#get-> to retrieve the data
#post-> to send the data
#put-> to update existing data
#delete-> to delte the existing data