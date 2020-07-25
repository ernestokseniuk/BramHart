from django import template

register = template.Library()

def stars(value):
    toReturn = ""
    for i in range(5):
        if value-1 >= i:
            toReturn += '<i class="fa fa-star checked"></i>'
        else:
            toReturn += '<i class="fa fa-star"></i>'
    return toReturn

register.filter("stars",stars)