from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.db.models.query_utils import DeferredAttribute
from django.views.generic.list import ListView

from .models import Section, Article

import datetime

class MyView(View):

    def get(self, request, *args, **kwargs):
        body = 'Hello, World!' + MyView.current_datetime()
        return HttpResponse(body)

    def my_view(self, request):
        if request:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            return HttpResponse('<h1>Page was found</h1>')
        
        return HttpResponse(status=201)

    @staticmethod
    def current_datetime():
        now = datetime.datetime.today()
        html = "<html><body><br> It is now: %s.</body></html>" % now
        return html

class MyIndexView(View):
    model = Section
 
    def get(self, request, *args, **kwargs):
        the_data={}
        the_data1={}
        all_lessons= self.model.objects.all()
        for lesson in all_lessons:
            the_data1[lesson]=all_lessons.all()
            for section in the_data1[lesson]:
                the_data[lesson][section]=section.file.all()
                context={'the_data':the_data,}

        #context += str(self.model.section_title)
        #context += self.model.section_url
        #context += self.model.section_description
        #context = {Section.section_description, Section.section_title, Section.section_url}
        #context['section_list'] = Section.Meta.db_table.__getitem__#.Meta.db_table.objects.all().order_by('section_title')
        #body = 'Hello, Index!<br>'
        #body1 = context[0]
        #body2 = body1.blank
        #body += body2
        #body = render_to_string('index.html', {'section_list' : context})
 
        return render(request, template_name=self.template_name, context=context)
        #return HttpResponse(context)
 
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