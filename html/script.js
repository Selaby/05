register.addEventListener("click", ()=> {
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
function alertJs(text){
    alert(text)
}