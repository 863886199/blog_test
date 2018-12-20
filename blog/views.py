from django.shortcuts import render, get_object_or_404
from .models import Post, Category
import markdown
#分页头文件
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

#from django.forms import forms
#from DjangoUeditor.forms import UEditorField


#主页
def index(request):
    #获取post表的全部信息
    post_list = Post.objects.all().order_by('-created_time')
    #每一页3个文章
    paginator = Paginator(post_list, 3)
    #接收网页中的page值
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #如果用户请求的页码号不是整数，显示第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={'post_list': contacts})

#文章页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #访问数增加函数
    post.increase_views()
    #文本高亮 没有效果
    post.boby = markdown.markdown(post.boby,
                                 extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                 ])
    return render(request, 'blog/detail.html', context={'post': post})
#按时间归档页
def archives(request, year, month):
    #filter通过过滤一些文章
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
#分类页
def category(request, pk):
    #获取文章分类
    #分类匹配 没有匹配到报404错误
    cate = get_object_or_404(Category, pk=pk)
    #按条件获取
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

