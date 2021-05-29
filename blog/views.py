from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html',{})
#第二引数はtemplatesを参照することになっている