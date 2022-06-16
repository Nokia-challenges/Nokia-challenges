from pathlib import Path
from typing import List
import timeit
from openpyxl import Workbook
import requests
from utils import compose_url
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows 
from openpyxl import workbook


from standings import League

leagues: List[League] = [
    League(id=4328, name="Premier League"),
    League(id=4331, name="Bundesliga"),
    League(id=4332, name="Serie A"),
    League(id=4334, name="Ligue 1"),
    League(id=4335, name="La Liga"),
    League(id=4344, name="Primeira Liga"),
    League(id=4337, name="Eredivisie"),
    League(id=4330, name="Scottish Premier League"),
    League(id=4621, name="Austrian Bundesliga"),
    League(id=4338, name="Belgian First Division A"),
    League(id=4675, name="Swiss Super League"),
    League(id=4340, name="Danish Superliga"),
    League(id=4422, name="Polish Ekstraklasa"),
    League(id=4631, name="Czech First League"),
    League(id=4336, name="Greek Superleague"),
    League(id=4671, name="Serbian Super Liga"),
    League(id=4629, name="Croatian First Football League"),
    League(id=4691, name="Romanian Liga I"),
    League(id=4690, name="Hungarian NB I"),
    League(id=4356, name="Australian A League"),
]

path = Path.cwd() / "Standings.xlsx"
url="https://www.thesportsdb.com/Sport/Soccer"

def f1(i):
     for i in range (20):
        url=compose_url(str(leagues[i].id),"2021-2022")
        r=requests.get(url)
        r=r.json()["table"]
        return r

def f2(r):
     
    mp={}
    c=0
    for item in r:
        for item2 in item:
            if c==0:
                mp[item2]=list()
            mp[item2].append(item[item2])
        c=c+1
    return mp


def run():
    start = timeit.default_timer()
    print(f"Execution time: {timeit.default_timer() - start}")
    wb=Workbook()
    for i in range(20):
        df=pd.DataFrame(f2(f1(i)))
       # wb.active()
        ws=wb.create_sheet(str(i))

        for i in dataframe_to_rows(df,index=True, header=True):
            ws.append(i)
        wb.save("pandas_openpyxl.xlsx")


    


if __name__ == "__main__":
    run()
