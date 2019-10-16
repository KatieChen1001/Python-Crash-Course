from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


html = urlopen('http://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1')
bs = BeautifulSoup(html.read(), 'html.parser')
my_table = bs.find('tr', {'id':'tr006817'})
print(my_table)
