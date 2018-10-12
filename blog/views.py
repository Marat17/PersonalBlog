from django.shortcuts import render
from personalblog.models import Mypost

# Create your views here.
def index(request):
	allposts = Mypost.objects.filter(time__lte=timezone.now()).order_by('-post_date')
	context = {
		'allposts' : allposts,
	}
	return render(request, 'blog/index.html', context)