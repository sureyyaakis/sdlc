# In this example, the test_add_to_cart function is a unit test for the add_to_cart method of the Cart class.
# The test creates a new Cart instance, adds a Product to the cart with a quantity of 2, and then asserts that the length of the cart.items list is 1 (indicating that the product was successfully added to the cart), 
# that the product in the cart is the same as the product that was added, and that the quantity of the product in the cart is 2.

# When this test is run, it will either pass (if the add_to_cart method is working as expected) or fail (if there is an issue with the method).
# If the test passes, we can be confident that the add_to_cart method is working correctly and we can move on to testing other parts of the e-commerce website. 
# If the test fails, we know that there is an issue with the add_to_cart method and can fix it before it causes problems for customers trying to purchase products from the website.



def test_add_to_cart():
    # Test that a product can be added to the cart
    cart = Cart()
    product = Product(name="Test Product", price=10.00)
    cart.add_to_cart(product, quantity=2)
    assert len(cart.items) == 1, f"Expected 1 item in cart, but got {len(cart.items)}"
    assert cart.items[0].product == product, f"Expected product to be {product}, but got {cart.items[0].product}"
    assert cart.items[0].quantity == 2, f"Expected quantity to be 2, but got {cart.items[0].quantity}"

class Cart:
    def __init__(self):
        self.items = []
        
    def add_to_cart(self, product, quantity):
        self.items.append(CartItem(product, quantity))
        
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
