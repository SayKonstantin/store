from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView

from .models import Item, Category, SubCategory, Post
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'users/main.html')#'users/../templates/users/main.html')




def page_not_found_view(request, exception):
    return render(request, 'users/404.html', status=404)



class NewsView(ListView):
    model = Post
    template_name = 'items/news.html'
    context_object_name = 'news'



class About(TemplateView):
    template_name = 'items/about.html'


class Contacts(TemplateView):
    template_name = 'items/contacts.html'





class AllItemsView(ListView):
    template_name = 'items/all.html'
    model = Item
    context_object_name = 'items'
    #paginate_by = 2


class PhonesView(AllItemsView):
    def get_queryset(self):
        filter_qs = Item.objects.select_related('subcategory__category').filter(subcategory__name__startswith='Iphone')
        return filter_qs

class PadsView(AllItemsView):
    def get_queryset(self):
        filter_qs = Item.objects.select_related('subcategory__category').filter(subcategory__name__startswith='Ipad')
        return filter_qs



class NotesView(AllItemsView):
    def get_queryset(self):
        filter_qs = Item.objects.select_related('subcategory__category').filter(subcategory__name__startswith='Mac')
        return filter_qs



class DetailItem(DetailView):
    template_name = 'items/detail_item.html'
    model = Post
    slug_field = 'url'
    slug_url_kwarg = 'url'


class PostView(DetailView):
    template_name = 'items/post.html'
    model = Post
    slug_field = 'id'
    slug_url_kwarg = 'id'
    context_object_name = 'post'

