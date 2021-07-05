from django import template

register = template.Library()


@register.filter(name='times')
def times(number):
    if number == None:
        return None
    else:
        return range(int(number))


@register.filter(name='leftover')
def times(number):
    if number == None:
        return None
    else:
        return range(5 - int(number))


@register.filter(name='percent')
def times(number):
    if number == None:
        return None
    else:
        return (number/5)*100


@register.filter(name='exists')
def times(number):
    if number == None:
        return False
    else:
        return True


@register.filter(name='true2yes')
def times(number):
    if number == True:
        return "Yes"
    else:
        return "No"
