from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class PostObjects(models.Manager):#manager a class that acts as an interfaace helping models interact with database .....querying in the models
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'draft'),
        ('published', 'published'),
    )
    category = models.ForeignKey(Category(), on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length= 100)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published') #way of generating a valid url ,,,unique means there cant be more than 1 slug with the same date
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'blog_posts')#related_name specifies reverse relation from user models to my models
    status = models.CharField(max_length=20, choices=options, default='published')
    objects = models.Manager() #insstance of the super class
    postobjects = PostObjects()#instance of the child class


    class Meta:
        ordering = ('-published',)




    def __str__(self):
        return self.title