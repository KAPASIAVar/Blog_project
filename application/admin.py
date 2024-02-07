from django.contrib import admin
from .models import Blog_category,Blog_post,add_Likes,add_views,add_comments
# Register your models here.
admin.site.register(Blog_category)
admin.site.register(Blog_post)
admin.site.register(add_Likes)
admin.site.register(add_views)
admin.site.register(add_comments)
