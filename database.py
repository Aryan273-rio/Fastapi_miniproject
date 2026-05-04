import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

password = "Rio@270324"
safe_password = urllib.parse.quote_plus(password)
db_url = f"postgresql://postgres:{safe_password}@localhost:5432/aryan"

engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)