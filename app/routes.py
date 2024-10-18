from flask import Blueprint, render_template, request, redirect, url_for
from app.services.finance_service import adicionar_receita, adicionar_despesa, obter_resumo_mensal
from datetime import datetime

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/add_income', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        data = datetime.strptime(request.form['data'], '%Y-%m-%d')
        adicionar_receita(descricao, valor, data)
        return redirect(url_for('main.index'))
    return render_template('add_income.html')


@main_bp.route('/dashboard')
def dashboard():
    mes = request.args.get('mes', datetime.today().month)
    ano = request.args.get('ano', datetime.today().year)
    receitas, despesas = obter_resumo_mensal(mes, ano)

    # Calculando valores para o gráfico
    total_receitas = sum([r.valor for r in receitas])
    total_despesas = sum([d.valor for d in despesas])

    return render_template('dashboard.html', receitas=total_receitas, despesas=total_despesas)
