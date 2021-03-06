import os
import eel
import desktop
import pandas as pd
import pos_system

app_name="html"
end_point="index.html"
size=(700,600)

### メイン処理

if not os.path.exists(pos_system.EMPLOYEE_MASTER_CSV_PATH):
    eel.alertJs("従業員マスターが存在しません。終了します")
item_master = pos_system.register_item_by_csv(pos_system.ITEM_MASTER_CSV_PATH)
if not item_master:
    eel.alertJs("商品マスターが存在しません。終了します")
order = pos_system.Order(item_master)

def main():
    global order
    order.__init__(item_master)
    eel.init('html')
    eel.start('index.html')

@eel.expose
def input_pic(employee_code:str):
    global pic_code, pic_name_modified

    # employee_master.csvをDataFrameに変換、employee_code列を抜き出してSeriesに変換後、リストに変換
    employee_master_df = pd.read_csv(pos_system.EMPLOYEE_MASTER_CSV_PATH, encoding="utf-8")
    employee_master_list = employee_master_df['employee_code'].to_list()
    # employee_codeがマスターに含まれていなければエラーを返す
    if employee_code not in employee_master_list:
        eel.alertJs(f"従業員コード 『 {employee_code} 』 は従業員マスターに登録されていません")
    # マスターに存在する場合はログインする
    else:
        employee_master_df = pd.read_csv(pos_system.EMPLOYEE_MASTER_CSV_PATH, encoding="utf-8")
        pic_code = employee_code
        eel.alertlogin(f"従業員コード 『 {pic_code} 』 でログインしました")
        pic_name = employee_master_df.loc[employee_master_df["employee_code"] == pic_code, "employee_name"]
        pic_name_modified = pic_name.iloc[-1]
        eel.view_pic(f"担当者コード：{pic_code}\n担当者：{pic_name_modified}")

@eel.expose
def input_order(order_code:str, order_qty:str):

    # グローバル変数の宣言が必要
    global order

    if order_code not in order.item_order_list:
        # item_master.csvをDataFrameに変換後、item_code列を抜き出してSeriesに変換し、リストに変換
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

    refresh()

# 買い物カゴと合計金額を更新
@eel.expose
def refresh():
    global cart, sum
    cart = order.view_cart()
    sum = order.view_sum()

    eel.view_cart(cart)
    eel.view_sum(sum)

@eel.expose
def settle(deposit:str):
    if not deposit:
        message = "お支払金額を入力してください"
    else:
        change = order.payment(deposit)
        if change >= 0:
            message = f"お釣りは{change}円です。\nご利用ありがとうございました。"
            order.write_receipt(f"担当者コード：{pic_code}　担当者名：{pic_name_modified}\n")
            order.write_receipt(cart)
            order.write_receipt(f"合計金額：{sum}")
            order.write_receipt(f"お預り金額：￥{int(deposit):,}") # depositはGUIからstr型で入力されているので要変換
            order.write_receipt(f"お釣り：￥{change:,}")
            order.__init__(item_master)
            refresh()
            eel.clear_text()
        else:
            message = f"【 残 高 不 足 】\nお支払いが不足しております。\nあと{abs(change):,}円足りません。"
    eel.alertJs(message)

if __name__ == "__main__":
    main()
    desktop.start(app_name,end_point,size)