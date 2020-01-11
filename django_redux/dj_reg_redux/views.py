from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from dj_reg_redux.models import Notice
# Create your views here.


class NoticeListView(ListView):
    model = Notice


class NoticeDetailView(DetailView):
    model = Notice
