from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.db.models.query_utils import DeferredAttribute
from django.views.generic.list import ListView
from django.http import Http404
from django.urls import reverse
from screeninfo import get_monitors

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.contrib.auth.views import LoginView

from .forms import UserForm, BookForm, TovarForm

from .models import Section, Article, Tovar, MyMenu, User

import datetime
import random

class MyView(View):
    menuModel = MyMenu
    articleModel = Article
    userForm = UserForm
    bookForm = BookForm
    template_name = 'headPage.html'
    context_object_name = 'articles'

    def post(self, request, *args, **kwargs):
        id =  request.POST.get('id')
        l1 =  request.POST.get('l1')
        l2 =  request.POST.get('l2')
        l3 =  request.POST.get('l3')
        l4 =  request.POST.get('l4')
        l5 =  request.POST.get('l5')
        first =  request.POST.get('first')
        visible =  request.POST.get('visible')
        level =  request.POST.get('level')
        content =  request.POST.get('content')
        link =  request.POST.get('link')
        #установка всех visible в 0
        self.menuModel.objects.all().update(visible=0)
        self.menuModel.objects.all().update(first=0)
        self.menuModel.objects.all().update(activ=0)
        #обновление данных в базе данных
        # 1 уровень
        if l2 == '0':
            for x in range(1,(int(level) + 2)):
                self.menuModel.objects.all().filter(level=x).filter(l1=l1).update(visible=1)
        # 2 уровень
        elif l3 == '0':
            self.menuModel.objects.all().filter(l1=l1).filter(l3='0').update(first=1)
            for x in range(1,(int(level) + 2)):
                self.menuModel.objects.all().filter(level=x).filter(l2=l2).filter(l1=l1).update(visible=1)
        # 3 уровень
        elif l4 == '0':
            self.menuModel.objects.all().filter(l1=l1).filter(l3='0').update(first=1)
            for x in range(1,(int(level) + 2)):
                self.menuModel.objects.all().filter(level=x).filter(l3=l3).filter(l2=l2).filter(l1=l1).update(visible=1)
        # 4 уровень
        else:
            self.menuModel.objects.all().filter(l1=l1).filter(l3='0').update(first=1)
            for x in range(1,(int(level) + 2)):
                self.menuModel.objects.all().filter(level=x).filter(l3=l3).filter(l3=l3).filter(l2=l2).filter(l1=l1).update(visible=1)
        self.menuModel.objects.all().filter(id=id).update(activ=1)
        return render(request, self.template_name, context=self.fun(link))

    def get(self, request, *args, **kwargs):
        link = self.menuModel.objects.all().get(activ=1)
        return render(request, self.template_name, context=self.fun(link.link))

    def fun(self, link):
        randomNum1 = random.randint(0, 30)
        randomNum2 = random.randint(0, 100) 
        randomNum3 = random.randint(0, 100)
        try:
            menu = self.menuModel.objects.all()
            articles = self.articleModel.objects.all()  
        except Exception:
            raise Http404("ОШИБКА ЧТЕНИЯ ИЗ БАЗЫ ДАННЫХ")
        rend = self.articleModel.objects.count()
        context = {"link": link,"latest_firstPage": randomNum2, "var_1" : randomNum3, "range": range(randomNum1), "rend" : rend, 'articles':articles, 'userForm':self.userForm, 'bookForm':self.bookForm, 'menu':menu}
        return context

    def my_view(self, request):
        if not request:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            return HttpResponse('<h1>Page was found</h1>')
        
        return HttpResponse(status=2001)

    @staticmethod
    def current_datetime():
        now = datetime.datetime.today()
        html = "<html><body><br> It is now: %s.</body></html>" % now
        return html

class MyIndexView(View):
    tovar = Tovar
    form = UserForm
    template_name = 'index.html'
    context_object_name = 'sections'
 
    def get(self, request, *args, **kwargs):
        tovars = self.tovar.objects.all()
        count = self.tovar.objects.count()
        context = {'tovars':tovars,'count':count,'form':self.form} 
        return render(request, self.template_name, context=context)
 
class MySectionView(View):
    template_name = 'headPage/section.html'
 
    def get(self, request, *args, **kwargs):
        context = {}
        section = get_object_or_404(Section, section_url=self.kwargs['section'])
        
        context['section'] = section
 
        return render(request, template_name=self.template_name, context=context)
  
class MyArticleView(View):
    template_name = 'headPage/article.html'
 
    def get(self, request, *args, **kwargs):
        context = {}
        article = get_object_or_404(Article, id=self.kwargs['article_id'])
        
        context['article'] = article
 
        return render(request, template_name=self.template_name, context=context)

class MyTovarView(View):    
    tovar = Tovar
    form = TovarForm
    template_name = 'tovar.html'
    context_object_name = 'tovar'
 
    def get(self, request, *args, **kwargs):
        context = {'id':-1, 'form':self.form,} 
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        discript =  request.POST.get('discript')
        cost =  request.POST.get('cost')
        name =  request.POST.get('name')
        if (self.baseCheck(name)):
            b = self.tovar(name=name, discript=discript, cost=cost,)
            b.save()
            context = {'name':name, 'discript':discript, 'cost':cost, 'id':1, 'form':self.form,} 
        else:
            context = {'id':0, 'form':self.form,}
        return render(request, self.template_name, context=context)
    
    def baseCheck (self, name):
        #проверка наличия записи с таким названием в базе
        if (self.tovar.objects.filter(name=name)):
            return False
        return True

class MyWindyView(UpdateView):
    template_name = 'windy.html'
    context_object_name = 'windy'

    def get(self, request, *args, **kwargs):        
        obj = self
        username = request.user.username
        if username != '':
            first_name = request.user.first_name
            last_name = request.user.last_name
            email = request.user.email
            password = request.user.password
            groups = request.user.groups
            user_permissions = request.user.user_permissions
            is_staff = request.user.is_staff
            is_active = request.user.is_active
            is_superuser = request.user.is_superuser
            last_login = request.user.last_login
            user = {username, first_name, last_name, email, password, groups, user_permissions, is_staff, is_superuser, is_active, last_login,}
        else:
            user = {'НЕТ ДАННЫХ'}
        context = {'obj': obj, 'LoginRequiredMixin': LoginRequiredMixin, 'UpdateView': UpdateView, 'user': user, 'username': username, 'reg': True, }
        if self.test(username):
            try:
                return render(request, self.template_name, context=context) 
            except Exception:
                context = {'user': user, 'reg': False}
                return render(request, self.template_name, context=context)
                #raise Http404("ОШИБКА ДОСТУПА ПОЛЬЗОВАТЕЛЯ")
        else:
            context = {'user': user, 'reg': False}
            return render(request, self.template_name, context=context)  

    def test(self, arg):
        if arg == '':
            return False
        return True
    
 
class MyTest(View):
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