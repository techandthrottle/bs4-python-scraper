import bs4 as bs
import requests
import eel

eel.init('ui')

def get_stock_index(key):
    source = requests.get('https://finance.yahoo.com/quote/'+ key +'/?p='+ key + '')
    soup = bs.BeautifulSoup(source.text, 'lxml')
    stock_index = soup.find_all('div',{'class' : 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span')
    return stock_index.text

def get_stock_name(key):
    source = requests.get('https://finance.yahoo.com/quote/'+ key +'/?p='+ key + '')
    soup = bs.BeautifulSoup(source.text, 'lxml')
    stock_name = soup.find_all('div', {'class' : 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'})[0].find('h1')
    return stock_name.text

@eel.expose
def get_data(keyword):
    key = keyword
    stock_index = str(get_stock_index(key))
    stock_name = str(get_stock_name(key))
    return str(stock_name + ' Price index was ' + stock_index)


eel.start('index.html', size=(800,400))
