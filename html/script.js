// moji_done.addEventListener("click", ()=> {
//     eel.moji(moji_moto.value);
// })

// eel.expose(view_moji_result)
// function view_moji_result(text) {
//     moji_result.value = text;
// }

// suji_done.addEventListener("click", ()=> {
//     eel.suji(suji_moto.value);
// })

// eel.expose(view_suji_result)
// function view_suji_result(text) {
//     suji_result.value = text;
// }

register.addEventListener("click", ()=> {
    if (order_code.value !== "" && order_qty.value !== "") {
        eel.input_order(order_code.value, order_qty.value);
    } else {
        alert("商品コードおよび個数の入力は必須です");
    }
})

eel.expose(view_sum)
function view_sum(text) {
    sum.value = text;
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