from notion_client import Client
from pprint import pprint
import json
import pandas as pd

NOTION_TOKEN = input("Notion Token: \n")
NOTION_DB_ID = input("Database ID: \n")
client = Client(auth=NOTION_TOKEN)

from myModules import database, exporter

df_dict = database.get_agirlik_takibi_db_info(client, NOTION_DB_ID)
print("""
TEST 1 PASSED: Read dataset from DB
----------------------------
""")

exporter.export_json(df_dict, "./exported-files/agirlik_takibi.json")
print("""
TEST 2 PASSED: Export dataset as a JSON
--------------------------------
""")

# JSON verisini dosyadan oku
with open("./exported-files/agirlik_takibi.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)
df['created time'] = pd.to_datetime(df['created time'])
df.to_parquet("./exported-files/agirlik_takibi.parquet")
print(df.info())
print(df.head())