# A Django app to add Ajax capabilities to django-tables2

This app is an enhancement for [django-tables2](https://pypi.python.org/pypi/django-tables2). It adds Ajax capability to allow tables to be sorted and paged without reloading the entire page. 

- On Pypi [django-ajax-tables](https://pypi.org/project/django-ajax-tables/)
- On Git [django-ajax-tables](https://github.com/KiwiTrinsic/django-ajax-tables)

## Requirements

- Python 3
- Django (version 2+)
- [django-tables2](https://pypi.python.org/pypi/django-tables2)
- jQuery (for the Ajax calls)

## Installation

Install with pip:

```python
pip install django-ajax-tables
```

Add django_ajax_tables to the settings.py installed_apps:

```python
INSTALLED_APPS = (
    ...,
    "django_ajax_tables",
)
```

## Features

This app adds a new Django template tag {% ajax_table %}. 
This is a replacement for the django-tables2 {% render_table %} tag.

To implement the Ajax functionality you will need to add a view which returns the raw table html (example shown below).
The tag will use that html to render the table on the page.
It will also configure the table sorting and pagination links to perform Ajax calls and in-place updates of the table.
This will allow you to sort and page through the table without the entire webpage refreshing on each click.

This will not affect any LinkColumns that have been added to the table layout.

## Example

Create a django-tables2 table and wire it to a model as normal:

```python
import django_tables2 as tables

class SimpleTable(tables.Table):
    class Meta:
        model = Simple
```

Create a view that exposes the table as raw html:

```python
from django.http import HttpResponse
from django_tables2 import RequestConfig

def simple_view(request):
    simple_table = SimpleTable(Simple.objects.all())
    RequestConfig(request).configure(simple_table)
    return HttpResponse(simple_table.as_html(request))
```

Load the django_ajax_tables tags in the template and add ajax_table tags as needed:

```
{% load django_ajax_tables %}
{% ajax_table "unique_div_id" "simple_view_url" %}
```

## Usage

The ajax_table tag requires at least two parameters.

- The first parameter is a unique id. This id should not used for any other element on the page. The ajax_table tag will create a <div> with this id to contain the table.
- The second parameter is the name of the url that is mapped to the table view.
- Any additional non-keyword arguments will be passed as positional arguments to the url. If used this will prevent the passing of keyword arguments to the url.
- The template keyword argument can be used to replace the django-ajax-tables javascript with custom javascript.
- Any additional keyword arguments will be passed as keyword aguments to the url but only if there were no positional arguments passed to the url.



