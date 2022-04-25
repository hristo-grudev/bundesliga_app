from django import template

register = template.Library()

BUNDESLIGA_ONE = "bl1"
BUNDESLIGA_TWO = "bl2"
BUNDESLIGA_THREE = "bl3"

LEAGUES_DICT = {
    BUNDESLIGA_ONE: 'Bundesliga 1',
    BUNDESLIGA_TWO: 'Bundesliga 2',
    BUNDESLIGA_THREE: 'Bundesliga 3',

}


@register.filter
def divide(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None


@register.filter
def league(slug):
    if slug in LEAGUES_DICT.keys():
        return LEAGUES_DICT[slug]
    return ''
