from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# timezone用于处理时间相关的事务
from django.utils import timezone
# 导入reverse方法
from django.urls import reverse

# Create your models here.


# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者，on_delete参数用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题，models.CharField为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)

    # 文章正文，保存大量文本使用TextField
    body = models.TextField()

    # 文章创建时间，default=timezone.now参数指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间，auto_now=True参数指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 访问量
    total_views = models.PositiveIntegerField(default=0)

    # 内部类Meta用于给model定义元数据
    class Meta:
        # ordering指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数__str__定义当前调用对象的str()方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])
