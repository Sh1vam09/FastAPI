from pydantic import BaseModel,Field,StrictInt
from typing import Optional

class Employee(BaseModel):
    id:int = Field(...,gt=0)  #...->means that anything which is required
    name:str = Field(...,min_length=3,max_length=30)
    dept:str =Field(...,min_length=3,max_length=15)
    age:Optional[StrictInt] =Field(default=None,gt=18) #if i give "35" it will still accept it by doing type conversion
    #if i dont want that to be happen then i can use Strictint 