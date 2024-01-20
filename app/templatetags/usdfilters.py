from django import template
register=template.Library()

def swapping(value):
    return value.swapcase()
register.filter('swapping',swapping)


def remove(value,arg):
    return value.replace(arg,'$')
register.filter('remove',remove)


def counting(value,arg):
    c=0
    for i in range(len(value)):
        if arg==value[i:len(arg)+i:1]:
            c+=1
    return c
register.filter('counting',counting)

def uppercase(value):
    return value.upper()
register.filter('uppercase',uppercase)

def lower(value):
    return value.lower()
register.filter('lower',lower)

def title(value):
    return value.title()
register.filter('title',title)

