# coding=utf-8
import urllib
from django import forms
from django.core.files import File
from django.db import models


class JasnyImageWidget(forms.FileInput):
    existing = '<img src="{url}" alt="{name}" width="{width}" height="{height}">'

    html = """\
           <div class="fileinput fileinput-{state}" data-provides="fileinput">
             <div class="fileinput-preview thumbnail" data-trigger="fileinput" style="width: {width}px; height: {height}px;">
             {existing}
             </div>
               <div>
                 <span class="btn btn-default btn-file">
                 <span class="fileinput-new">Выберите изображение</span>
                 <span class="fileinput-exists">Изменить</span>
                 <input type="file" name="{name}" accept="images/*"></span>
                 <input type="hidden" id="jasny-deleted" name="{name}-deleted" value="0">
                 <input type="hidden" id="jasny-url" name="{name}-url" value="">
                 <a href="#" id="a-jasny-deleted" class="btn btn-default fileinput-exists" data-dismiss="fileinput">Удалить</a>
               </div>
           </div>
           """

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        width = attrs.get('width', None) or 150
        height = attrs.get('width', None) or width
        state = 'exists' if value else 'new'
        value = False
        # value if isinstance(value, str) else (value.url if value else None)
        existing = self.existing.format(url=value, name=name, width=width, height=height) if value else ''
        return self.html.format(state=state, width=width, height=height, existing=existing, name=name)

    def value_from_datadict(self, data, files, name):
        deleted = bool(int(data.pop(name+'-deleted', ['0'])[0]))
        url = data.pop(name+'-url', [''])[0]
        file = files.get(name, None)
        if deleted and not file:
            return False
        if not file and url:
            result = urllib.urlretrieve(url)
            file = File(open(result[0]))
        return file

    class Media:
        css = {
            'all': ['view/jasny/css/jasny-bootstrap.css']
        }
        js = ['view/jasny/js/jasny-bootstrap.js', 'view/jasny/js/jasny-image.js']


class JasnyImageField(forms.ImageField):
    widget = JasnyImageWidget


class JasnyImageModelField(models.ImageField):
    def formfield(self, **kwargs):
        defaults = {'form_class': JasnyImageField}
        defaults.update(kwargs)
        return super(JasnyImageModelField, self).formfield(**defaults)