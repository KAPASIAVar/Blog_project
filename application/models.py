from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Blog_category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    blog_img=models.ImageField(upload_to='images/')
    blog_description=RichTextUploadingField()
    blog_summary=models.TextField(blank=True,max_length=200)

    def __str__(self):
        return self.category_name
class Blog_post(models.Model):
    Blog_Name=models.CharField(max_length=100, unique=True)
    category_name=models.ForeignKey(Blog_category,on_delete=models.CASCADE)
    blog_img=models.ImageField(upload_to='Cover/')
    blog_summary=models.TextField(blank=True,max_length=200)
    blog_description=RichTextUploadingField()
    def __str__(self):
        return self.Blog_Name
class add_Likes(models.Model):
    
    blog_id=models.ForeignKey(Blog_post,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.blog_id)
class add_views(models.Model):
    blog_id=models.ForeignKey(Blog_post,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.blog_id)
class add_comments(models.Model):
    
    blog_id=models.ForeignKey(Blog_post,on_delete=models.CASCADE)
    comment=models.TextField()
    username=models.CharField(max_length=20,null=True)
    def __str__(self):
        return str(self.blog_id)                             