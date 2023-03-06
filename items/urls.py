from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:url>', views.DetailItem.as_view()),
    path('about', views.About.as_view(), name='about'),
    path('contacts', views.Contacts.as_view(), name='contacts'),
    path('news', views.NewsView.as_view()),
    path('news/<slug:pk>', views.PostView.as_view()),
    path('phones', views.PhonesView.as_view()),
    path('notes', views.NotesView.as_view()),
    path('all', views.AllItemsView.as_view()),
    path('pads', views.PadsView.as_view()),

]
