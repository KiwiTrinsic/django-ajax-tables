from django.template import Library
from django.template.loader import get_template
from django.urls import reverse

register = Library()

@register.simple_tag(takes_context=True)
def ajax_table(context, divname, url, *args, template='django_ajax_tables/ajax_wrapper.html', **kwargs):
    template = get_template(template)
    
    if args:
        tableurl = reverse(url, args=args)
    elif kwargs:
        tableurl = reverse(url, kwargs=kwargs)
    else:
        tableurl = reverse(url)

    context.push(ajax_tableurl=tableurl, ajax_divname=divname)

    try:
        return template.render(context.flatten())
    finally:
        context.pop()
