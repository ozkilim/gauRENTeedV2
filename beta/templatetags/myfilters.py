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


@register.filter(name='NoInfoSorry')
def times(number):
    if number == None:
        return "Sorry, no further information was provided in this review."
    else:
        return number


@register.filter(name='toChart')
def times(number):
    if number != 0:
        return number/10
