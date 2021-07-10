import eel
import desktop
import pandas as pd
import pos_system

ITEM_MASTER_CSV_PATH="./master.csv" # カレントディレクトリの状態に要注意 ずれているとFileNotFoundErrorが出る

app_name="html"
end_point="index.html"
size=(700,600)

### メイン処理
# @eel.expose
# def moji(moji_moto):
#     result = moji_moto + "ぼぼぼ"
#     eel.view_moji_result(result)

# @eel.expose
# def suji(suji_moto):
#     result = int(suji_moto) + 10
#     eel.view_suji_result(result)

item_master = pos_system.register_by_csv(ITEM_MASTER_CSV_PATH)
order = pos_system.Order(item_master)

def main():
    global order
    order.__init__(item_master)
    # order_code = "001"
    # order_qty = 5
    # order.item_order_list[order_code] = int(order_qty)
    # print(order.item_order_list)
    eel.init('html')
    eel.start('index.html')

@eel.expose
def input_order(order_code:str, order_qty:str):
    # グローバル変数の宣言が必要
    global order

    # item_order_listに当該商品コードが存在しない場合は新たに作成する。ここは文字列型
    if order_code not in order.item_order_list:
        order.item_order_list[order_code] = int(order_qty)
    else:
        order.item_order_list[order_code] += int(order_qty)
    # print(order.item_order_list)
    text = order.view_sum()
    eel.view_sum(text)
 
if __name__ == "__main__":
    main()
    desktop.start(app_name,end_point,size)