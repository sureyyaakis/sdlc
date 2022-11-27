// Model Testing  Scenario 
function increase(item) 
{
  return item += 1;
}
function testIncreaseQuantityByOne(item)
{
  increase(item);
  assertEquals(item.quantity, 1);
}


function testItemAddedSuccessfully(item)
{
// example 
addItemTfoCart(cart, item);
assertEquals(cart.response, 200);
}


// Update click add navigate to cart web element
function testAddItemToCart()
{
  $(.item).click();
  $(.cart).navigate();
  assertEquals(.quantity),1);
}
