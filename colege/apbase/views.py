from django.shortcuts import render

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'page/index.html', {})

from django.utils import timezone
from django.shortcuts import render
from .models import Nota






# Create your views here.
