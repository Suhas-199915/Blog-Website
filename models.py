from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    createDate = models.DateField(default=timezone.now) 
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()
    
    def approveComments(self):
        return self.comments.filter(approvedComment=True)
    
    def get_absolute_url(self):
        return reverse("postDetail", kwargs= {"pk":self.pk})
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('blogApp.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    text = models.TextField()
    createDate = models.DateTimeField(default = timezone.now()) 
    approvedComment = models.BooleanField(default=False)

    def approve(self):
        self.approvedComment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse('postList')
    
    def __str__(self):
        return self.text
