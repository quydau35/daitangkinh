# db.py
from sqlalchemy import Boolean, Column, Integer, Text, DateTime, Numeric, create_engine
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_MAIN_URI = "sqlite:///./db/main.db"
SQLALCHEMY_PUNC_URI = "sqlite:///./db/dtk-punc.db"
SQLALCHEMY_VIET_URI = "sqlite:///./db/dtk-viet.db"
SQLALCHEMY_TRAN_URI = "sqlite:///./db/dtk-tran.db"
# SQLALCHEMY_DATABASE_URI = "postgresql://user:password@postgresserver/db"

main_engine = create_engine(
         SQLALCHEMY_MAIN_URI, connect_args={"check_same_thread": False}, echo=True
)
punc_engine = create_engine(
         SQLALCHEMY_PUNC_URI, connect_args={"check_same_thread": False}, echo=True
)
# viet_engine = create_engine(
#          SQLALCHEMY_VIET_URI, connect_args={"check_same_thread": False}, echo=True
# )
# tran_engine = create_engine(
#          SQLALCHEMY_TRAN_URI, connect_args={"check_same_thread": False}, echo=True
# )

Base = declarative_base()

# Định nghĩa tripitaka_title
class Title(Base):
    __tablename__ = 'tripitaka_title'
    id = Column('ID', Integer, primary_key = True, autoincrement=True)
    title_id = Column('TitleID', Text)
    no = Column('No', Text)
    book = Column('Book', Integer)
    word = Column('Word', Integer)
    han = Column('Han', Text)
    viet = Column('Viet', Text)
    Viet2 = Column('Viet2', Text)
    transliteration1 = Column('Transliteration1', Text)
    search1 = Column('Search1', Text)
    english = Column('English', Text)
    translator = Column('Translator', Text)
    transliteration2 = Column('Transliteration2', Text)
    search2 = Column('Search2', Text)
    stage = Column('Stage', Text)
    file_id = Column('FileID', Text)
    comment = Column('Comment', Text)
    date = Column('Date', DateTime)
    date_transliterated = Column('DateTransliterated', DateTime)
    date_translated = Column('DateTranslated', DateTime)
    date_revised = Column('DateRevised', DateTime)
    visible = Column('Visible', Integer)
    books = Column('Books', Integer)
    order_number = Column('OrderNum', Numeric)
    divider = Column('Divider', Integer)
    proofreading = Column('ProofReading', Integer)
    state = Column('State', Integer)

class Category(Base):
    __tablename__ = 'tripitaka_category'
    id = Column('ID', Integer, primary_key=True)
    category_id = Column('CategoryID', Text)
    han = Column('Han', Text)
    viet = Column('Viet', Text)
    english = Column('English', Text)

# Tạo table Todo
Base.metadata.create_all(bind=main_engine)
Base.metadata.create_all(bind=punc_engine)
# Base.metadata.create_all(bind=viet_engine)
# Base.metadata.create_all(bind=tran_engine)
