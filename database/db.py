from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do banco
engine = create_engine('postgresql://user:password@localhost/finance_db')
Session = sessionmaker(bind=engine)
session = Session()

# Modelo base
Base = declarative_base()
