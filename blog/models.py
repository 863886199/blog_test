from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
from DjangoUeditor.models import UEditorField
# Create your models here.
#分类
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#文章
class Post(models.Model):
    title = models.CharField(max_length=100)
    #正文 富文本
    boby = UEditorField(width=800, height=300, toolbars="full", imagePath="images/", filePath="files/",
    upload_settings={"imageMaxSize":1204000}, settings={}, verbose_name='内容')


    #创建时间
    created_time = models.DateTimeField()
    #修改时间
    modified_time = models.DateTimeField()
    #文章摘要
    excperpt = models.CharField(max_length=100, blank=True)
    #分类外键
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #标签外键多对多
    tags = models.ManyToManyField(Tag, blank=True)
    #作者外键
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #统计阅读次数
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    #class Meat:
        #文章逆序排列
     #   ordering = ['created_time']
    #不知道为什么不行
    def increase_views(self):
        self.views += 1
        #只更新views
        self.save(update_fields=['views'])
    #没有摘要自动获取
    def save(self, *args, **kwargs):
        #如果没有摘要
        if not self.excperpt:
            #首先实例化Markdown
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excperpt = strip_tags(md.convert(self.boby))[:54]
        super(Post, self).save(*args, **kwargs)


