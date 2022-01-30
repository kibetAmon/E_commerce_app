from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for cart_id in keys:
        if int(cart_id) == product.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for cart_id in keys:
        if int(cart_id) == product.id:
            return cart.get(cart_id)
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity(product, cart)


@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    total = 0
    for p in products:
        total += price_total(p, cart)

    return total
