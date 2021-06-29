register.addEventListener("click", ()=> {
    if (order_code.value !== "" && order_qty.value !== "") {
        eel.input_order(order_code.value, order_qty.value);
        alert("登録しました");
    } else {
        alert("商品コードおよび個数の入力は必須です");
    }
})

eel.expose(view_item_list)
function view_item_list(text) {
    item_order_list = text;
}

// pos_system.addEventListener('click', () => {
//     eel.pos_system(order_code.value,order_qty.value)
// })

// eel.expose(register)
// function register(text){
//     process.value += text + "\n"
// }

// eel.expose(item_order_list)
// function item_order_list(text){
//     item_order_list.value += text + "\n"
// }

// eel.expose(sum)
// function sum(text){
//     sum.value += text + "\n"
// }

// eel.expose(change)
// function change(text){
//     change.value += text + "\n"
// }