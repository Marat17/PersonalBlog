from django.shortcuts import render
from blog.models import Mypost
from django.utils import timezone


# Create your views here.
def index(request):
	allposts = Mypost.objects.filter(time__lte=timezone.now()).order_by('-time')
	context = {
		'allposts' : allposts,
	}
	return render(request, 'blog/index.html', context)