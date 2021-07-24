import os
import datetime
import pandas as pd

EMPLOYEE_MASTER_CSV_PATH="./employee_master.csv" # カレントディレクトリの状態に要注意 ずれているとFileNotFoundErrorが出る
ITEM_MASTER_CSV_PATH="./item_master.csv" # カレントディレクトリの状態に要注意 ずれているとFileNotFoundErrorが出る
RECEIPT_FOLDER="./receipt"

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price

    def get_price(self):
        return self.price

### オーダークラス
class Order:
    # 課題4 オーダーリストを辞書型にして個数も登録できるようにする
    def __init__(self,item_master):
        self.item_master = item_master
        self.item_order_list = {}
        self.set_datetime() # これがないと動かない
    
    def set_datetime(self):
        self.datetime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.receipt_name = f"receipt_{self.datetime}.log"

    # 課題7 日付時刻をファイル名としたテキストファイルに出力し、Print関数も同時に動作させる
    def write_receipt(self,text):
        # print(text)
        with open(os.path.join(RECEIPT_FOLDER, self.receipt_name), mode="a", encoding="utf-8_sig") as f:
            f.write(text+"\n")

    # 買い物カゴの情報を表示
    def view_cart(self):
        self.sum = 0
        cart = ""
        # self.write_receipt("-----商品登録リスト-----")

        for key in self.item_order_list.keys():
            for m in self.item_master:
                if key == m.item_code:
                    value = self.item_order_list[key]
                    self.sum += m.price * int(value)
                    # self.write_receipt(f"商品コード:{key}")
                    # self.write_receipt(f"商品名:{m.item_name}")
                    # self.write_receipt(f"価格:{m.price:,}")
                    # self.write_receipt(f"個数:{value:,}")
                    # self.write_receipt(f"小計:{m.price * int(value):,}\n")

                    cart += f"商品コード:{key}\n"
                    cart += f"商品名:{m.item_name}\n"
                    cart += f"価格:{m.price:,}\n"
                    cart += f"個数:{value:,}\n"
                    cart += f"小計:{m.price * int(value):,}\n\n"
        # self.write_receipt(f"合計:{self.sum:,}\n-----商品登録リスト終了-----\n")

        return cart

    # 合計金額を表示
    def view_sum(self):
        self.sum = 0
        for key in self.item_order_list.keys():
            for m in self.item_master:
                if key == m.item_code:
                    value = self.item_order_list[key]
                    self.sum += m.price * int(value)        
        return(f"￥{self.sum:,}")

    # 課題6 預り金額を入力し、お釣りを計算する
    def payment(self, deposit):
        change = int(deposit) - self.sum
        return change

# 課題3 csvから商品マスターを登録する
def register_item_by_csv(ITEM_MASTER_CSV_PATH):
    item_master = []
    # マスターが存在しない場合はエラーを返す
    if not os.path.exists(ITEM_MASTER_CSV_PATH):
        return None
    item_master_df = pd.read_csv(ITEM_MASTER_CSV_PATH, encoding="utf-8", dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
    for item_code,item_name,price in zip(item_master_df["item_code"],item_master_df["item_name"],item_master_df["price"]):
        item_master.append(Item(item_code,item_name,price))
    return item_master

### メイン処理
# def main():
    # 課題3 csvから商品マスタを登録する
    # item_master = register_by_csv(ITEM_MASTER_CSV_PATH)
    # item_master = pd.read_csv("./master.csv", encoding="utf-8")

    # オーダー登録
    # order = Order(item_master)
    # order.input_order()

    # オーダー表示
    # order.view_item_list()

    # 会計
    # order.payment()

# if __name__ == "__main__":
#     main()