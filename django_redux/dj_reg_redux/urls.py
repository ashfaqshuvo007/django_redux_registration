from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from dj_reg_redux import views

urlpatterns = [
    path('notice/', views.NoticeListView.as_view()),
    path('notice/<int:pk>', views.NoticeDetailView.as_view()),
    path('', RedirectView.as_view(url="notice/")),

]
