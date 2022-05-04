import httpx
from secrets import chave




class Ativos:
    chave = chave


    def url_acao(self):
        return 'https://api.hgbrasil.com/finance/stock_price'

    def url_moeda(self):
        return 'https://api.hgbrasil.com/finance/quotations'


    def params(self,info):
        params = {'key':self.chave,'symbol':info}
        return params
           
    
    def dados_acao(self,acao):
        request = httpx.get(self.url_acao(),params=self.params(acao))
        resultado = request.json()
        nome = (resultado['results'][acao]['company_name'])
        preco = round(float(resultado['results'][acao]['price']),2)
        return {nome:preco}

    def dados_moeda(self,moeda):
        requisicao = httpx.get(self.url_moeda(),params = self.params(moeda))
        resultado = requisicao.json()
        nome = (resultado['results']['currencies'][moeda]['name'])
        preco = round(float(resultado['results']['currencies'][moeda]['sell']),2)
        return {nome:preco}

    

    


op = Ativos()

lista_ativos = ['MGLU3','BIDI4','PETR4']
dados = []

for ativo in lista_ativos:
    dados.append(op.dados_acao(ativo))

print(dados)