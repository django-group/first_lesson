from django import template
import random

register = template.Library()
x = random.randint(1, 1000)


@register.filter(name="game_number")
def game(value, x):
    res = x - value
    if res > 200 or res < -200:
        return "red"
    elif res > 75 or res < -75:
        return "orange"
    elif res > 20 or res < -20:
        return "yellow"
    elif res == 0:
        return "green"
    else:
        return "black"