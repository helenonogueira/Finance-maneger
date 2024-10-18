from app.models.finance import Despesa, Receita
from database.db import session


def adicionar_receita(descricao, valor, data):
    receita = Receita(descricao=descricao, valor=valor, data=data)
    session.add(receita)
    session.commit()


def adicionar_despesa(descricao, valor, data):
    despesa = Despesa(descricao=descricao, valor=valor, data=data)
    session.add(despesa)
    session.commit()


def obter_resumo_mensal(mes, ano):
    receitas = session.query(Receita).filter_by(mes=mes, ano=ano).all()
    despesas = session.query(Despesa).filter_by(mes=mes, ano=ano).all()
    return receitas, despesas
