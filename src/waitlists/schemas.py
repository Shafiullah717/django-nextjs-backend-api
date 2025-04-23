from ninja import Schema
from datetime import datetime
from pydantic import EmailStr

class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email : EmailStr

class WaitlistEntryDetailSchema(Schema):
    # GET -> DATA
    # WaitlistEntryOut 
    email : EmailStr
    timestamp : datetime 
