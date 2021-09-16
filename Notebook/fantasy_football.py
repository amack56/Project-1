import pandas as pd
from pathlib import Path

def read_fantasy_data(start_year,end_year):
    years = range(start_year,end_year+1)
    dfs=[]
    for year in years:
        df = pd.read_csv(Path(f"../Data/RawData/{year}.csv"))
        