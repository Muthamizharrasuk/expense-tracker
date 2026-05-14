from datetime import date as DataType
from pydantic import BaseModel, Field
from typing import Optional

class ExpenseCreate(BaseModel):
    amount : float
    category : str
    date: DataType = Field(default_factory=DataType.today)
    description: Optional[str] = ""

class ExpenseUpdate(BaseModel):
    amount : Optional[float] = None
    category : Optional[str] = None
    date : Optional[DataType] = None    
    description : Optional[str] = None
