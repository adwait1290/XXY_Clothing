var total = 0;
var totalQuantity = 0;
    $(document).ready(function calculate() {
        
        $('tr.productrow').each(function() {
            var itemPriceText = $(this).find('td.price').text();
            itemPriceString = itemPriceText.replace('$','');
            var itemQuantity = parseFloat($(this).find('h4.quantity').text());
            totalQuantity += itemQuantity;
            console.log(itemQuantity);
            var itemPrice = parseFloat(itemPriceString) * itemQuantity;
            console.log(itemPrice);
            total += itemPrice;
        })
        $('.sTotal').text("$" + total);
        $('.myCart').text("My Cart (" + totalQuantity + ")");
    })