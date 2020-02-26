from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.db.models.query_utils import DeferredAttribute
from django.views.generic.list import ListView
from django.http import Http404

import datetime
import random