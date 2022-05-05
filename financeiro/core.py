from models import Ativos


op = Ativos()

lista_ativos = ['MGLU3','BIDI4','PETR4']
dados = []

for ativo in lista_ativos:
    dados.append(op.dados_acao(ativo))

print(len(dados))