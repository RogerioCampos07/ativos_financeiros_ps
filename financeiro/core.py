from models import Ativos

lista_ativos = ['MGLU3','BIDI4','PETR4']
#ativo = str(input('Digite a ação para consulta: ')).upper()
#moeda = str(input('Digite a moeda para consulta: ')).upper()

def consulta_lista_ativos(list):
    op = Ativos()
    dados = []
    for ativo in lista_ativos:
        dados.append(op.dados_acao(ativo))
    print(dados)


def consulta_ativo(ativo):
    op = Ativos()
    print(op.dados_acao(ativo))


def consulta_preco_moeda(moeda):
    op = Ativos()
    print(op.dados_moeda(moeda))

