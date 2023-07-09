from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BaseEntity(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
