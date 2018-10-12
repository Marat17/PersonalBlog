from django.shortcuts import render
from blog.models import Mypost
from django.utils import timezone
from .forms import CreateNewPost


# Create your views here.
def index(request):
	allposts = Mypost.objects.filter(time__lte=timezone.now()).order_by('-time')
	context = {
		'allposts' : allposts,
	}
	return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html')

def create(request):
    form = CreateNewPost()
    if request.method == 'POST':
        form = CreateNewPost(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'blog/create.html', {'form': form})