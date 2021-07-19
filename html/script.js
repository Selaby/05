register_employee.addEventListener("click", ()=> {
    if (employee_code.value !== "") {
        eel.input_employee(employee_code.value);
    } else {
        alert("従業員コードの入力は必須です");
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