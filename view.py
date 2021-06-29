import eel
import desktop
import pandas as pd
import pos_system

app_name="html"
end_point="index.html"
size=(700,600)

### メイン処理
@eel.expose
def input_order(order_code, order_qty):
    pos_system.Order.item_order_list[order_code] = int(order_qty)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)