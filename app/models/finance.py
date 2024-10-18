from sqlalchemy import Column, Integer, String, Float, Date
from database.db import Base


class Receita(Base):
    __tablename__ = 'receitas'
    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    valor = Column(Float)
    data = Column(Date)


class Despesa(Base):
    __tablename__ = 'despesas'
    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    valor = Column(Float)
    data = Column(Date)
