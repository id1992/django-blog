from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# render는 파이썬 단에서 지원해주는 시스템
# 리스트 명명법 - model name + _list
def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')
    return render(request, 'blog/post_list.html', {
        'post_list': qs
    })

def post_detail(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk);
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {
        'post': post
    })