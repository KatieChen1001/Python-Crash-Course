import requests
import re
from bs4 import BeautifulSoup
import time
import random


fakeUA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
url = 'https://www.amazon.com/Microsoft-3RA-00022-Surface-Ergonomic-Keyboard/product-reviews/B01MFCTRZM/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&reviewerType=all_reviews&pageNumber='
totalPages = 2

fakeheader = {}
fakeheader['User-agent'] = fakeUA

for page in range(1,totalPages): 
    r = requests.get(url+str(page), timeout=30, headers=fakeheader)
    r.raise_for_status
    r.encoding = r.apparent_encoding


    soup1 = BeautifulSoup(r.content,'html.parser')
    print(soup1)
    resTitle = soup1.find_all(attrs={"data-hook":"review-title"})
    resDate = soup1.find_all(attrs={"data-hook":"review-date"})
    resBody = soup1.find_all(attrs={"data-hook":"review-body"})
    print(resTitle)
    print(resDate)

    # for i in range(3, len(resTitle)):
        # print(">>Title: "+ resTitle[i].string)
        # print(">>Date: " + resDate[i-2].string)
        # print(">>Body: " + resBody[i-2].text)

    time.sleep(random.randint(5,9))
