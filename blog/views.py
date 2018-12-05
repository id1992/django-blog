from django.shortcuts import render

# render는 파이썬 단에서 지원해주는 시스템
# 리스트 명명법 - model name + _list
def post_list(request):
    return render(request, 'blog/post_list.html')
