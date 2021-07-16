import eel
import desktop
import pandas as pd
import pos_system

app_name="html"
end_point="index.html"
size=(700,600)

### メイン処理

item_master = pos_system.register_by_csv(pos_system.ITEM_MASTER_CSV_PATH)
order = pos_system.Order(item_master)

def main():
    global order
    order.__init__(item_master)
    eel.init('html')
    eel.start('index.html')

@eel.expose
def input_order(order_code:str, order_qty:str):

    # グローバル変数の宣言が必要
    global order

    if order_code not in order.item_order_list:
        # master.csvをDataFrameに変換後、item_code列を抜き出してSeriesに変換し、リストに変換
        master_verify_df = pd.read_csv(pos_system.ITEM_MASTER_CSV_PATH, encoding="utf-8", dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
        item_code_list = master_verify_df['item_code'].to_list()
        # order_codeがマスターに含まれていなければエラーを返す
        if order_code not in item_code_list:
            eel.alertJs(f"商品コード 『 {order_code} 』 は商品マスターに登録されていません")
        # item_order_listに当該商品コードが存在しない場合は新たに作成する
        else:
            order.item_order_list[order_code] = int(order_qty)
    else:
        order.item_order_list[order_code] += int(order_qty)

    cart = order.view_cart()
    sum = order.view_sum()

    eel.view_cart(cart)
    eel.view_sum(sum)

@eel.expose
def settle(deposit:str):
    change = order.payment(deposit)
    eel.alertJs(f"お釣りは{change}円です")

if __name__ == "__main__":
    main()
    desktop.start(app_name,end_point,size)