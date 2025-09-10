import ecommerce_utils as x

cart = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000
}
x.generate_invoice(cart, discount_percent=10, gst_percent=18)
