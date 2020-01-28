from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=224)
    text = RichTextField()
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True,null=True)
    image = models.ImageField(upload_to='postpic/',default='postpic/fog4.jpg')

    def publish(self):
        self.published = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("blog:post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name = 'comments')
    text = models.TextField()
    author = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()


    def get_absolute_url(self):
        return reverse('post_list')


    def __str__(self):
        return self.text
class MyComment(models.Model):
    post = models.ForeignKey('POST', on_delete=models.CASCADE, related_name= 'comment')
    text = models.TextField()
    author = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail') 

    def __str__(self):
        return self.text    