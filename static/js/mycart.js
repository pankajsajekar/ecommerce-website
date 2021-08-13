console.log('working');
    if (localStorage.getItem('cart') == null) {
        var cart = {};
    } else {
        cart = JSON.parse(localStorage.getItem("cart"));
        updateCart(cart);
    }


    $('.div').on('click', 'button.cart', function() {
        var idstr = this.id.toString();
        console.log(idstr);
        if (cart[idstr] != undefined) {
            qty = cart[idstr][0] + 1;
            cart[idstr][0] = qty;
        } else {
            qty = 1;
            name = document.getElementById('name' + idstr).innerHTML
            my_url = document.getElementById('myurl' + idstr).href
            price2 = document.getElementById('price' + idstr).innerHTML
            imgsrc = document.getElementById('imgsrc' + idstr).src
            var price = parseInt(price2);
            var itotal = qty * price;
            cart[idstr] = [qty, name, price, itotal, imgsrc, my_url];
        }
        updateCart(cart);
    });

    //$('#popcart').popover();
    //updatePopover(cart);


    function updatePopover(cart) {

        var popStr = "";
        popStr = popStr + "<h5> Cart for your items in my shopping cart </h5> <div class='mx-2 my-2 divbn'>";
        var i = 1;
        for (var item in cart) {
            popStr = popStr + "<b>" + i + "</b>. ";
            popStr = popStr + cart[item][1].slice(5, ) + "... Qty: <button id='minus" + item + "' class='btn btn-primary minus' onclick='minus(this.id)'>-</button>" + cart[item][0] + ' <button id="plus' + item + '" class="btn btn-primary plus" onclick="plus(this.id)" >+</button> <br>';
            i = i + 1;

        }
        popStr = popStr + "</div>";
        var a = "{% url 'cart' %}";
        popStr = popStr + "<a href='" + a + "'><button class='btn btn-primary' id ='checkout' type='submit' name='send'  value='send'>View Cart</button></a> <button class='btn btn-primary' onclick='clearCart()' id ='clearCart'>Clear Cart</button>";

        document.getElementById('popcart').setAttribute('data-content', popStr);

        $('#popcart').popover('show');


    }

    function clearCart() {
        cart = JSON.parse(localStorage.getItem('cart'));
        localStorage.clear();
        cart = {};
        updateCart(cart);
        location.reload();
    }

    function updateCart(cart) {
        var sum = 0;
        for (var item in cart) {
            sum = sum + cart[item][0];
            cart[item][3] = cart[item][2] * cart[item][0];
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        document.getElementById('cartnm').innerHTML = sum;
        //updatePopover(cart);
    }

var totalf = 0;
    function minus(clicked_id) {
        var a = clicked_id.slice(5, );
        cart = JSON.parse(localStorage.getItem('cart'));
        cart[a][0] = cart[a][0] - 1;
        cart[a][0] = Math.max(0, cart[a][0]);
        updateCart(cart);
        document.getElementById('qty' + a).innerHTML = cart[a][0].toString();
        document.getElementById("singletotal" + a).innerHTML = cart[a][3].toString();
        for(itemm in cart){
        totalf = totalf + cart[itemm][3];
        }
        document.getElementById('carttotal').innerHTML = totalf;

    }

    function plus(clicked_id) {
        var a = clicked_id.slice(4, );
        cart = JSON.parse(localStorage.getItem('cart'));
        cart[a][0] = cart[a][0] + 1;
        updateCart(cart);
        document.getElementById('qty' + a).innerHTML = cart[a][0].toString();
        document.getElementById("singletotal" + a).innerHTML = cart[a][3].toString();
        for(itemm in cart){
        totalf = totalf + cart[itemm][3];
        }
        document.getElementById('carttotal').innerHTML = totalf;

    }

    function deleteitem(b) {
        var c = b.slice(6, ).toString();
        cart = JSON.parse(localStorage.getItem('cart'));
        for (items in cart) {
            a = items.toString();
            if (a == c) {
                delete cart[a];
            }
        }
        updateCart(cart);
        var tr = "trspam" + c;
        document.getElementById(tr).innerHTML = "";
}