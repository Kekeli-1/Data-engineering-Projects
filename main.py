file_path = "../Data/campaign.csv"

import os 
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir,"..", "Data","campaign.csv")

data_list = []
with open(file_path,"r") as file:
    lines = file.readlines()
    headers = lines[0].strip().split("\t")
for line in lines:
    values = line.strip().split("\t")
    row = dict(zip(headers,values))
    data_list.append(row)
print(data_list)

from datetime import datetime

def valid_number(data):
    try:
        return float(data)
    except ValueError:
        return None
    
def valid_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None
    
clean_data = []
for row in data_list:
    impressions = valid_number(row["impressions"])
    clicks = valid_number(row["clicks"])
    conversions = valid_number(row["conversions"])
    cost = valid_number(row["cost"])
    revenue = valid_number(row["revenue"])
    date = valid_date(row["date"])

    if (row["campaign_name"] != "" and impressions is not None and clicks is not  
     None and conversions >= 0 and conversions is not None and cost is not None
     and revenue is not None and date is not None):
        row["impressions"] = impressions 
        row["clicks"] = clicks
        row["conversions"] = conversions 
        row["cost"] = cost 
        row["revenue"] = revenue
        row["date"] = date 
        clean_data.append(row)
print(clean_data)

import pandas as pd
import csv 
import os 
output_path = "../Output/cleaned_data.csv"

if clean_data:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path,"w", newline="") as file:
        write = csv.DictWriter(file,fieldnames=clean_data[0].keys())
        write.writeheader()
        write.writerows(clean_data)
    print("successfully loaded")
    df = pd.read_csv(output_path)
    print(df.head())
else:
    print("Not succesfull")

Total_revenue = df["revenue"].sum()
print(Total_revenue)

df["Total_revenue"] = df["revenue"].sum()


Total_cost = df["cost"].sum()
print(Total_cost)

df["Total_cost"] = df["cost"].sum()


df["ROI"] = df["revenue"] - df["cost"] / df["cost"]
print(df["ROI"])

Best_campaign = df.sort_values(by="ROI", ascending=False)
print(Best_campaign)

base_dir = os.path.dirname(__file__)
output_folder = os.path.join(base_dir,"..","Output")

os.makedirs(output_folder,exist_ok=True)
output_path = os.path.join(output_folder,"cleaned_data.csv")
with open(output_path,"w") as file:
    file.write(f"The total revenue: {Total_revenue}")
    file.write(f"The total cost: {Total_cost}" )
    file.write(f"The Best campaign: {Best_campaign}")

import pandas as pd 
df.to_csv("cleaned_data.csv", index= False)

from sqlalchemy import create_engine
import pandas as pd 
df = pd.read_csv("cleaned_data.csv")

engine = create_engine("postgresql://postgres:kekeli/Gh@localhost:5432/postgres")
df.to_sql("marketing_campaign", engine, if_exists="replace", index= False )
print("Data loaded successfully")

import requests 

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)
data = response.json()
print(data)

for user in data:
    print(user["name"])
    print(user["email"])

import pandas as pd 
df = pd.DataFrame(data)
df.to_csv('users.csv', index=False)
print("saved_successfully")

import schedule
import time 
def job():
    print('Pipeline running')
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

