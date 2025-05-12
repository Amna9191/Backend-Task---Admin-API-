# Import necessary libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load Variables from .env file
load_dotenv()

# URL for database
DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

# Establish connection to database
engine = create_engine(DATABASE_URL)

# Create Session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Define base class for tables
Base = declarative_base()