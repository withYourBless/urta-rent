import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

import yaml

with open('config.yml') as f:
    db_config = yaml.safe_load(f)["dsn"]

load_dotenv()

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_config["user"]}:{os.getenv('PG_PASSWORD')}@{db_config["host"]}:{db_config["port"]}/{db_config["database"]}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# for sqlQuery
conn = psycopg2.connect(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
