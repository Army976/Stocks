from django import template

register = template.Library()

@register.simple_tag
def percent(ytdchange):
	ytd = round((float(ytdchange)*100), 2)
	return ytd
