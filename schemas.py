from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    id: Any
    username: str
    password: str
    email: str
    test: str


class ReadUsers(BaseModel):
    id: Any
    username: str
    password: str
    email: str
    test: str
    class Config:
        from_attributes = True


class AppData(BaseModel):
    id: Any
    user_id: int
    data: str
    test: str


class ReadAppData(BaseModel):
    id: Any
    user_id: int
    data: str
    test: str
    class Config:
        from_attributes = True


class Class(BaseModel):
    id: int
    test: str


class ReadClass(BaseModel):
    id: int
    test: str
    class Config:
        from_attributes = True


