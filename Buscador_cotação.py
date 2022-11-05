import requests

def pegar_cotacao(moeda):
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    req_dic = requisicao.json()
    cotacao_dolar = req_dic['USDBRL']['bid']
    cotacao_euro = req_dic['EURBRL']['bid']
    cotacao_btc = req_dic['BTCBRL']['bid']

    if moeda == 'USD':
        return cotacao_dolar
    elif moeda == 'EUR':
        return cotacao_euro
    elif moeda == 'BTC':
        return cotacao_btc

if __name__ == '__main__':
    print(pegar_cotacao('USD'))
    print(pegar_cotacao('EUR'))
    print(pegar_cotacao('BTC'))