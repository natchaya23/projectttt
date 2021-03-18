from typing import Optional, List
from pydantic import BaseModel, Field


class createAttractionModel(BaseModel):
    idlat: str = Field(min_length=17, max_length=17)
    idlong: str = Field(min_length=17, max_length=17)
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
