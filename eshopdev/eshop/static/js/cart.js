var count = 0;
var ii = 0;
var cartData = [];
var taka =[]
var count=0
var l=[]
var test =[]
 l= JSON.parse(localStorage.getItem('cartData'))
console.log(l)
if(l != undefined){
    for(var n=0;n<l.length;n++){
        showcart(l[n].image,l[n].title,l[n].price)
}
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ready)


} else {

    ready();
}

function ready() {
    var removeButton = document.getElementsByClassName('btn btn-danger')
    for (var i = 0; i < removeButton.length; i++) {
        var button = removeButton[i]
        button.addEventListener('click', removeItem)
    }
    var itemInputs = document.getElementsByClassName('cart-quantity-input')

    for (j = 0; j < itemInputs.length; j++) {
        var itemInput = itemInputs[j]
        itemInput.addEventListener('change', updateInputField)
    }

    var addCart = document.getElementsByClassName('add-to-cart-link')
    for (var x = 0; x < addCart.length; x++) {
        var product = addCart[x]
        product.addEventListener('click', addToCart)
    }
}

function addToCart(event) {
    var item = event.target
    var shopItem = item.parentElement.parentElement.parentElement

    var price = shopItem.getElementsByClassName('product-carousel-price')[0].innerText
    var title = shopItem.getElementsByClassName('product-detail')[0].innerText
    var productID = shopItem.getElementsByClassName('productId')[0].value
    var image = shopItem.getElementsByClassName('product-image')[0].src
    console.log(productID)
    showcart(image, title, price)
    updatecart()
}

function showcart(image, title, price) {
        count++
        cartData.push({
        image : image,
        price :price,
        title :title
    })
    localStorage.setItem('cartData', JSON.stringify(cartData));


    var cartRow = document.createElement('div')
    cartRow.classList.add('cart-row')
    var cartItems = document.getElementsByClassName('cart-items')[0]



     var     cartRowContents  = `
        <div class="cart-item cart-column">
        <span class="idTest">${count}</span>
         <img class="cart-item-image" src="${image}" width="100" height="100">
                        <span class="cart-item-title">${title}</span>
                    </div>
                    <span class="cart-price cart-column">${price}</span>
                    <div class="cart-quantity cart-column">
                        <input type="hidden" id="custId"  value="">
                        <input class="cart-quantity-input" type="number" value="1">
                      
                        <button class="btn btn-danger"  type="button">REMOVE</button>
                    </div>
 `


      cartRow.innerHTML = cartRowContents
      cartItems.append(cartRow)

    cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeItem)
    cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', updateInputField)


}

function updateInputField(event) {
    var input = event.target
    if (isNaN(input.value) || input.value < 0) {
        input.value = 1.00

    }
    updatecart()
}

function removeItem(event) {
    var clickButton = event.target
    var test = clickButton.parentElement.parentElement
    let lio =  parseInt(test.getElementsByClassName('idTest')[0].innerText)
    var t= JSON.parse(localStorage.getItem('cartData'))
    t.splice(t.indexOf(lio),1)
    console.log(t)
    localStorage.setItem('cartData', JSON.stringify(t));
    clickButton.parentElement.parentElement.remove()
    updatecart()

}

function updatecart() {
    var cartItems = document.getElementsByClassName('cart-items')[0]
    var cartRows = cartItems.getElementsByClassName('cart-row')
    var total = 0

    for (var k = 0; k < cartRows.length; k++) {
        var cartRow = cartRows[k]
        var cartRowPrice = cartRow.getElementsByClassName('cart-price')[0]
        var quantity = cartRow.getElementsByClassName('cart-quantity-input')[0]
        cartRowPrice = parseFloat(cartRowPrice.innerText.replace('$', ''))
        quantity = quantity.value
        // console.log(cartRowPrice,quantity)
        total = total + (cartRowPrice * quantity)

    }
    document.getElementsByClassName('cart-total-price')[0].innerText = Math.round(total)

}

