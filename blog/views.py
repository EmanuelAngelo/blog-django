from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # tres postagens em cada pagina
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # se a pagina nao for um inteiro do intervalo, exibe a ultima pagina de resultados
        posts = paginator.page(1)
    except EmptyPage:
        # se a pgaina estiver fora do intervalo, exibe a ultima pagina de resultados
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html',{'page': page, 'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'blog/post/detail.html',{'post': post})