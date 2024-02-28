btn_minus = document.getElementById('btn_minus');
btn_plus = document.getElementById('btn_plus');

btn_minus.addEventListener('click', function() {
    qty = document.getElementById('qty').value
    if(qty >= 2){
        qty--
        document.getElementById('qty').value = qty
    }

    console.log(qty)
});


btn_plus.addEventListener('click', function() {
    qty = document.getElementById('qty').value
    qty++
    document.getElementById('qty').value = qty
});
