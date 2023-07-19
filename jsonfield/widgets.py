import json
from django import forms

from .utils import default


class JSONWidget(forms.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""
        if not isinstance(value, str):
            value = json.dumps(value, ensure_ascii=False, indent=2,
                               default=default, separators=(',', ':'))
        return super(JSONWidget, self).render(name, value, attrs, renderer)


class JSONSelectWidget(forms.SelectMultiple):
    pass
