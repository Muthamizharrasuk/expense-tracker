from pydantic import BaseModel
from typing import Optional

class BudgetCreate(BaseModel):
    category : str
    limit : float
    month : str
    

class BudgetUpdate(BaseModel):
    limit : Optional[float] = None
    month : Optional[str] = None
    category : Optional[str] = None