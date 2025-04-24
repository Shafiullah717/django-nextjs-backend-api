from ninja import Schema
from datetime import datetime
from pydantic import EmailStr

class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email : EmailStr

class WaitlistEntryListSchema(Schema):
    #List -> DATA
    # WaitlistEntryOut
    id : int
    email : EmailStr 

class WaitlistEntryDetailSchema(Schema):
    # GET -> DATA
    # WaitlistEntryOut 
    id : int
    email : EmailStr
    updated : datetime
    timestamp : datetime 
