import datetime
import pandas as pd

ITEM_MASTER_CSV_PATH="./master.csv" # カレントディレクトリの状態に要注意 ずれているとFileNotFoundErrorが出る
RECEIPT_FOLDER="./receipt"

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price

    def get_price(self):
        return self.price

### オーダークラス
class Order:
    # def __init__(self,item_master):
    #     self.item_order_list=[]
    #     self.item_master=item_master

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
        print(text)
        with open(RECEIPT_FOLDER + "\\" + self.receipt_name, mode="a", encoding="utf-8_sig") as f:
            f.write(text+"\n")

    # def add_item_order(self,item_code):
    #     self.item_order_list.append(item_code)

    # 課題4 オーダーリストを辞書型にして個数も登録できるようにする
    # def add_item_order(self,order_code,total_qty):
    #     self.item_order_list[order_code] = total_qty

    # 課題2 ターミナルから商品コードを登録する
    def input_order(self):
        while True:
            order_code = input("商品コードを入力してください　登録を完了する場合は999を入力してください >> ")
            if int(order_code) != 999: # ここは整数型
                # 課題4 個数も登録する
                if str(order_code) not in self.item_order_list: # item_order_listに当該商品コードが存在しない場合は新たに作成する。ここは文字列型
                    order_qty = input("個数を入力してください >> ")
                    self.item_order_list[order_code] = int(order_qty)
                else:
                    order_qty = input("個数を入力してください >> ")
                    self.item_order_list[order_code] += int(order_qty)
            else:
                print("商品登録を終了します\n")
                break

    # 課題4 辞書型にしたオーダーリストからkeyをもとに抽出
    def view_item_list(self):
        self.sum = 0
        self.write_receipt("-----商品登録リスト-----")
        for key in self.item_order_list.keys():
            for m in self.item_master:
                if key == m.item_code:
                    value = self.item_order_list[key]
                    self.sum += m.price * int(value)
                    self.write_receipt(f"商品コード:{key}")
                    self.write_receipt(f"商品名:{m.item_name}")
                    self.write_receipt(f"価格:{m.price:,}")
                    self.write_receipt(f"個数:{value:,}")
                    self.write_receipt(f"小計:{m.price * int(value):,}\n")
        self.write_receipt(f"合計:{self.sum:,}\n-----商品登録リスト終了-----\n")

    # 課題1 item_codeを入力することで、その商品の名前と価格を表示する
    # def view_name_and_price(self,item_code):
    #     for m in self.item_master:
    #         if item_code == m.item_code:
    #             print(f"商品コード:{m.item_code}")
    #             print(f"商品名:{m.item_name}")
    #             print(f"価格:{m.price}")
    #             return m.item_name,m.price

    # 課題6 預り金額を入力し、お釣りを計算する
    def payment(self):
        while True:
            deposit = input("お預かり金額を入力してください >> ")
            change = int(deposit) - self.sum
            if change >= 0:
                self.write_receipt(f"{int(deposit):,}円お預かりいたします。\nお釣りは{change:,}円です。\nご利用ありがとうございました。")
                break
            else:
                self.write_receipt(f"{int(deposit):,}円お預かりいたします。\n\n【 残 高 不 足 】\nお支払いが不足しております。\nあと{abs(change):,}円足りません。\n")

# 課題3 csvから商品マスタを登録する
def register_by_csv(csv_path):
    item_master=[]
    item_master_df = pd.read_csv(csv_path, encoding="utf-8", dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
    for item_code,item_name,price in zip(item_master_df["item_code"],item_master_df["item_name"],item_master_df["price"]):
        item_master.append(Item(item_code,item_name,price))
    return item_master

### メイン処理
def main():
    # マスタ登録
    # item_master=[]
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))

    # 課題3 csvから商品マスタを登録する
    item_master = register_by_csv(ITEM_MASTER_CSV_PATH)
    # item_master = pd.read_csv("./master.csv", encoding="utf-8")

    # オーダー登録
    order=Order(item_master)
    order.input_order()

    # 課題2 ターミナルから商品コードを登録する
    # order_code = input("商品コードを入力してください >> ")
    # # 課題4 個数も登録する
    # order_qty = input("個数を入力してください >> ")
    # order.add_item_order(order_code,order_qty)
    # order.add_item_order("001")
    # order.add_item_order("002")
    # order.add_item_order("003")

    # オーダー表示
    order.view_item_list()

    # 商品情報表示
    # order.view_name_and_price(order_code)

    # 会計
    order.payment()

if __name__ == "__main__":
    main()