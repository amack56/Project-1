import pandas as pd
from pathlib import Path
import numpy as np

def read_fantasy_data(start_year,end_year):
    years = range(start_year,end_year+1)
    dfs=[]
    for year in years:
        if year != 2020:
            df = pd.read_csv(Path(f"../Data/RawData/{year}.csv"))
            df["Year"]= year
            df = df[["Year","Player","Tm","Pos","FantasyPoints"]]
            df = df.set_index("Year")
            dfs.append(df)
        
        else:
            df = pd.read_csv(Path(f"../Data/RawData/{year}.csv"), header=1)
            df["Year"]= year
            df = df[["Year","Player","Tm","FantPos","PPR"]]
            df = df.rename(columns={"FantPos": "Pos", "PPR" : "FantasyPoints"})
            for ind in df.index:
                df['Player'][ind] = df['Player'][ind].split(sep="\\")[0].replace("*", "").replace("+", "").strip()
            df = df.set_index("Year")
            dfs.append(df)
    return pd.concat(dfs)

def read_rushing_yds(start_year, end_year):
    years = range(start_year,end_year+1)
    dfs=[]
    for year in years:
        if year != 2020:
            df = pd.read_csv(Path(f"../Data/RawData/{year}.csv"))
            df["Year"]= year
            df = df[["Year","Player","Tm","Pos","RushingYds","FantasyPoints"]]
            df = df.set_index("Year")
            dfs.append(df)
        else:
            df = pd.read_csv(Path(f"../Data/RawData/2020.csv"), header=1)
            df["Year"]= "2020"
            df = df[["Year","Player","Tm","FantPos","RushingYds","PPR"]]
            df = df.rename(columns={"FantPos": "Pos", "PPR" : "FantasyPoints"})
            df = df.set_index("Year")
            dfs.append(df)
        dfs.reset_index()
    return pd.concat(dfs)