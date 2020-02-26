#from django.db import models
#from .forms import forms
from django import forms

import cgi 

storage = cgi.FieldStorage()
data = storage.getvalue('data')
print('Status: 200 OK')
print('Content-Type: text/plain')
print('')
if data is not None:
    print(data)

class BookForm(forms.Form):
    class Meta:
        db_table = "form"
        fields = '__all__'

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()