import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd



start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 12, 31)
delta = datetime.timedelta(days=1)
l = []
while start_date <= end_date:
    # print(start_date.strftime("%b"))
    day = start_date.strftime("%d")
    month = start_date.strftime("%b")
    year =start_date.strftime("%Y")
    start_date += delta
    a = (day+"-"+month+"-"+year)
    url = f'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=1&Tx_Market=0&DateFrom={a}&DateTo={a}&Fr_Date={a}&To_Date={a}&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=Agra&Tx_MarketHead=--Select--'
    response  = requests.get(url).text
    soup = BeautifulSoup(response , 'html.parser')
    table = soup.find("table" , class_ = "tableagmark_new")
    
    for t in table.find_all("tr"):
      m = []
      for a in t.find_all("td"):
        # print(a.text.strip())
        m.append(a.text.strip())
      l.append(m)
    
df = pd.DataFrame(l[1:],columns = ['Sl. no.','District Name', 'Market Name','Commodity','Variety','Grade','Min Price (Rs./Quintal)','Max Price (Rs./Quintal)','Modal Price (Rs./Quintal)','Price Date'])
df = df.dropna(subset = ["District Name"], inplace=False)
df = df.reset_index(drop=True)
display(df.head())
