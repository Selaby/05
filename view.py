import eel
import desktop
import pandas as pd
import pos_system
from pos_system import *

app_name="html"
end_point="index.html"
size=(700,600)

def register_by_csv(csv_path):
    item_master=[]
    item_master_df = pd.read_csv(csv_path, encoding="utf-8", dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
    for item_code,item_name,price in zip(item_master_df["item_code"],item_master_df["item_name"],item_master_df["price"]):
        item_master.append(Item(item_code,item_name,price))
    return item_master

### メイン処理
@ eel.expose
def pos_system():
    pos_system.main()