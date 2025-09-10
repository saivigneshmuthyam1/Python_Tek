def apply_discount(price, discount_percent):
    disc=((price)*(discount_percent/100))
    return (price-disc)

def add_gst(price, gst_percent=18):
    gst=((price)*(18/100))
    return (price+gst)

def generate_invoice(cart, discount_percent=0, gst_percent=18):
    print("------ INVOICE ------")
    subtotal = 0
    for product, price in cart.items():
        print(f"{product:}: ₹{price}")
        subtotal += price
    print("---------------------")
    print(f"Subtotal: ₹{subtotal}")
    price_after_discount = apply_discount(subtotal, discount_percent)
    print(f"After {discount_percent}% discount: ₹{price_after_discount}")
    final_price = add_gst(price_after_discount, gst_percent)
    print(f"After {gst_percent}% GST: ₹{final_price:.2f}")
    print("---------------------")
    print("Thank you for shopping with us!")