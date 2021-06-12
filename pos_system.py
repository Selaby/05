import datetime
import pandas as pd
import eel

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
        # print(text)
        with open(RECEIPT_FOLDER + "\\" + self.receipt_name, mode="a", encoding="utf-8_sig") as f:
            f.write(text+"\n")

    # def add_item_order(self,item_code):
    #     self.item_order_list.append(item_code)

    # 課題4 オーダーリストを辞書型にして個数も登録できるようにする
    # def add_item_order(self,order_code,total_qty):
    #     self.item_order_list[order_code] = total_qty

    # 課題2 ターミナルから商品コードを登録する
    def input_order(self,order_code,order_qty):
        while True:
            # order_code = input("商品コードを入力してください　登録を完了する場合は999を入力してください >> ")
            if int(order_code) != 999: # ここは整数型
                # 課題4 個数も登録する
                if str(order_code) not in self.item_order_list: # item_order_listに当該商品コードが存在しない場合は新たに作成する。ここは文字列型
                    # order_qty = input("個数を入力してください >> ")
                    self.item_order_list[order_code] = int(order_qty)
                    eel.register(f"商品コード:{key}")
                    eel.register(f"個数:{value:,}")
                else:
                    # order_qty = input("個数を入力してください >> ")
                    self.item_order_list[order_code] += int(order_qty)
                    eel.register(f"商品コード:{key}")
                    eel.register(f"個数:{value:,}")
            else:
                eel.register("商品登録を終了します\n")
                break

    # 課題4 辞書型にしたオーダーリストからkeyをもとに抽出
    def view_item_list(self):
        self.sum = 0
        self.write_receipt("-----商品登録リスト-----")
        eel.item_order_list("-----商品登録リスト-----")
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

                    eel.item_order_list(f"商品コード:{key}")
                    eel.item_order_list(f"商品名:{m.item_name}")
                    eel.item_order_list(f"価格:{m.price:,}")
                    eel.item_order_list(f"個数:{value:,}")
                    eel.item_order_list(f"小計:{m.price * int(value):,}\n")

        self.write_receipt(f"合計:{self.sum:,}\n-----商品登録リスト終了-----\n")
        eel.item_order_list(f"-----商品登録リスト終了-----\n")
        eel.sum(f"合計:{self.sum:,}")

    # 課題1 item_codeを入力することで、その商品の名前と価格を表示する
    # def view_name_and_price(self,item_code):
    #     for m in self.item_master:
    #         if item_code == m.item_code:
    #             print(f"商品コード:{m.item_code}")
    #             print(f"商品名:{m.item_name}")
    #             print(f"価格:{m.price}")
    #             return m.item_name,m.price

    # 課題6 預り金額を入力し、お釣りを計算する
    def payment(self,deposit):
        while True:
            # deposit = input("お預かり金額を入力してください >> ")
            change = int(deposit) - self.sum
            if change >= 0:
                self.write_receipt(f"{int(deposit):,}円お預かりいたします。\nお釣りは{change:,}円です。\nご利用ありがとうございました。")
                eel.deposit(deposit)
                eel.change(change)
                break
            else:
                self.write_receipt(f"{int(deposit):,}円お預かりいたします。\n\n【 残 高 不 足 】\nお支払いが不足しております。\nあと{abs(change):,}円足りません。\n")
                eel.change(f"【 残 高 不 足 】　あと{abs(change):,}円足りません。")

def main():
    item_master = register_by_csv(ITEM_MASTER_CSV_PATH)

    # オーダー登録
    order=Order(item_master)
    order.input_order(order_code,order_qty)

    # オーダー表示
    order.view_item_list()

    # 会計
    order.payment()

if __name__ == "__main__":
    main()