undisplay()
// ツールを表示する関数
eel.expose(display)
function display(){
    control_panel.style.display = "block";
}
// ツールを非表示にする関数
eel.expose(undisplay)
function undisplay(){
    control_panel.style.display = "none";
}

login.addEventListener("click", ()=> {
    if (employee_code.value !== "") {
        eel.input_employee(employee_code.value);
        // 従業員マスターに登録されていない場合は実行されない
        eel.expose(alertlogin)
        function alertlogin(text) {
            alert(text);
            display();
        }
    } else {
        alert("従業員番号を入力してください")
    }
})

register_item.addEventListener("click", ()=> {
    if (order_code.value !== "" && order_qty.value !== "") {
        eel.input_order(order_code.value, order_qty.value);
    } else {
        alert("商品コードおよび個数の入力は必須です");
    }
})

eel.expose(view_cart)
function view_cart(text) {
    cart.value = text;
}

eel.expose(view_sum)
function view_sum(text) {
    sum.value = text;
}

eel.expose(alertJs)
function alertJs(text) {
    alert(text)
}

settle.addEventListener("click", ()=> {
    eel.settle(deposit.value);
})

eel.expose(clear_text)
function clear_text() {
    order_code.value = "",
    order_qty.value = "",
    deposit.value = "";
}