from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import Http404

from headPage.models import MyMenu

class MyTest():
    menuModel = MyMenu
    template_name = 'windy.html'
    context_object_name = 'windy'

    def post(self, request, *args, **kwargs):
        try:
            menu = self.menuModel1.objects.all()
            raise Http404("ЧТЕНИE ДАННЫХ")
        except Exception:
            raise Http404("ОШИБКА ЧТЕНИЯ ИЗ БАЗЫ ДАННЫХ")
        b = self.menu(l1=1, l2=2, l3=3, l4=4, l5=5, first=0, visible=1, level=1, content='Новый уровень')
        b.save()