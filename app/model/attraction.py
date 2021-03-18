from typing import Optional, List
from pydantic import BaseModel, Field


class createAttractionModel(BaseModel):
    id: str = Field(min_length=5, max_length=5)
    idlat: str = Field(min_length=18, max_length=18)
    idlong: str = Field(min_length=18, max_length=18)
    picture_url: str
    name_attraction: str
    country: str
    state: str
    zone: str
    seasons: str
    Type: str


class updateAttractionModel(BaseModel):
    name_attraction: Optional[str]
    country: Optional[str]
    state: Optional[str]
    zone: Optional[str]
    seasons: Optional[str]
    Type: Optional[str]
