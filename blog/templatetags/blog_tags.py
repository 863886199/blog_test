from django import template
from django.db.models.aggregates import Count

from ..models import Post, Category
register = template.Library()
#侧边栏显示最新文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]

#按时间归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

#分类
@register.simple_tag
def get_categories():
    return Category.objects.all()




