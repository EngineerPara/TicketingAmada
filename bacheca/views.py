from django.shortcuts import render
from .forms import PostForm
from .models import Post
# Create your views here.

def home(request):
    return render(request, 'home.html', None)


def ScriviBacheca(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            titolo = form.cleaned_data['titolo']
            descrizione = form.cleaned_data['descrizione']
            Post.objects.create(titolo=titolo, descr=descrizione)
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'scrivi_post.html', context)

def bacheca(request):
    data = Post.objects.all()
    return render(request, 'bacheca.html', {'data':data})

def bacheca_details(request, pk):
    data = Post.objects.get(pk=pk)
    return render(request, 'bacheca_details.html', {'data': data})