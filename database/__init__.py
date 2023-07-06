from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connecting to database
SQLALCHEMY_DATABASE_URI = "sqlite://pay_test.db"
# connect_args={"check_same_thread": False - only for sqlite3
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})
# Session for database
SessionLocal = sessionmaker(bind=engine)

# General Class for data models
Base = declarative_base()

# Functionality Import
from database.userservice import *
from database.cardservice import *
from database.businesservice import *
from database.paymentservice import *
