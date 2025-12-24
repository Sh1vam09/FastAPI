from pydantic import BaseModel, EmailStr


# we define specific classes because if we want to make something optional or having any constratint
# thn this help to not but constraints and all on the whole you can put it on one class
# commom features
class EmployeeBase(BaseModel):
    name: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


# users asking for data about employee
class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        orm_mode = True  # when the data is goint out it help pydantic to readdata directly from orm objects
        # it enables smooth transition to json
