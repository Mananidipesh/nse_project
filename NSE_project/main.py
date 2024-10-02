from get_html import get_html
from selectolax.parser import HTMLParser
import pandas as pd


parsed_html = get_html('https://www.nseindia.com/market-data/live-equity-market')
html = parsed_html.css('tbody')

all_data = []
for tbody in html:
    for row in tbody.css('tr'):
        nse_dic = {}
        columns = row.css('td')  
        if len(columns) >= 5:  
            nse_dic['name'] = columns[0].text()  
            nse_dic['open'] = columns[1].text()  
            nse_dic['high'] = columns[2].text()  
            nse_dic['low'] = columns[3].text()
            nse_dic['prev.close'] = columns[4].text()
            nse_dic['L.T.P'] = columns[5].text()
            nse_dic['chng'] = columns[7].text()
            nse_dic['per.chng'] = columns[8].text()
            nse_dic['volume'] = columns[9].text()
            nse_dic['value'] = columns[10].text()
            nse_dic['52W H'] = columns[11].text()
            nse_dic['52W L'] = columns[12].text()
            nse_dic['30D per.chng'] = columns[13].text()
            # nse_dic['']
            all_data.append(nse_dic)

print(all_data)

data = pd.DataFrame(all_data)
data.to_csv('nse_data2.csv')








