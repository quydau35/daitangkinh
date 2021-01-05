from datetime import date, datetime, time, timedelta
from pydantic import BaseModel

# class Title(BaseModel):
#     ID : int
#     TitleID: str
#     No : str
#     Book: int
#     Word: int
#     Han: str
#     Viet: str
#     Viet2: str
#     Transliteration1: str
#     Search1: str
#     English: str
#     Translator: str
#     Transliteration2: str
#     Search2: str
#     Stage: str
#     FileID: str
#     Comment: str
#     Datetime: datetime
#     DateTransliterated: datetime
#     DateTranslated: datetime
#     DateRevised: datetime
#     Visible: int
#     Books: int
#     OrderNum: int
#     Divider: int
#     Proofreading: int
#     State: int

class TitleOut(BaseModel):
    id: int
    title_id: str
    no: str
    book: str
    han: str
    viet: str
    viet2: str
    transliteration1: str
    english: str
    translator: str
    transliteration2: str
    search1: str
    search2: str


# Definition of data passed to API using Pydantic Addition of Validation and
# Documentation functions
class TodoIn(BaseModel):
    title: str
    done: bool

