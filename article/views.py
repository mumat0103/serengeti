from django.shortcuts import get_object_or_404, redirect, render
from .forms import ArticleForm
from article.models import Article
def new(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(
                commit = False
            )
            article.author = request.user
            article.save()

            return redirect('article:show', id=article.id)

    return render(request, 'new.html', {'form':form})

def show(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'show.html', {'article':article})

def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            article = form.save()

            return redirect('article:show', id=article.id)
            
    return render(request, 'edit.html', {'form':form, 'article':article})

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    return redirect('main:index')
