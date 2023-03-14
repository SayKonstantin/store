from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('detail/<slug:slug>', views.DetailItem.as_view(),name = 'detail'),
    path('about', views.About.as_view(), name='about'),
    path('contacts', views.Contacts.as_view(), name='contacts'),
    path('news', views.NewsView.as_view(), name='news'),
    path('news/<slug:pk>', views.PostView.as_view()),
    path('phones', views.PhonesView.as_view(), name='phones'),
    path('notes', views.NotesView.as_view(), name='notes'),
    path('all', views.AllItemsView.as_view(), name='all'),
    path('pads', views.PadsView.as_view(), name='pads'),

]
