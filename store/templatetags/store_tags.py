from django import template

register = template.Library()


@register.filter
def get_quantity(dictionary, key):
    try:
        return dictionary.get(str(key))['quantity']
    except KeyError:
        return str(1)


@register.filter
def get_cost(dictionary, key):
    try:
        quantity = float(dictionary.get(str(key))['quantity'])
        unit_price = float(dictionary.get(str(key))['unit_price'])
        return '${:.2f}'.format(quantity * unit_price)
    except KeyError:
        return '${}'.format('0')