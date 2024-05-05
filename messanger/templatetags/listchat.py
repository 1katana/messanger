from django import template
from messanger import models


register=template.Library()


@register.inclusion_tag('messanger/show_messages')
def show_messages(pk=-1):
    pass


