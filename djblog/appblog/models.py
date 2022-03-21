from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category= models.CharField(max_length=100)
    def __str__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=100)
    # there is a built-in model called user in django.contrib.auth.models
    # so gonna import it and link it as a foriegn key to post model
    # cause one post is created by only one user but user can create more than one post 
    #oncascade delete cuase if user deleted his posts shall be deleted also 
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    body = models.TextField(null=True, blank=True)
    #cause of more than one post shall take the same tag 
    #creatig tags model and relate it many to many with post model
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    created = models.DateField(auto_now_add=True)
    #only one category per each post 
    # if category is deleted post shall be deleted  
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default = 1)
   
    def comments(self):
        return self.comment_set.all()
    def comments_count(self):
        return self.comment_set.all().count()
    def __str__(self):
        return self.title 
    #to oreder posts through this class and order it by its creation date 
    # class Meta:
    #     ordering=('-created')

class Comments(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    authority = models.BooleanField(default=User.is_staff)
    post= models.ForeignKey(Post,on_delete=models.CASCADE)
    comment= models.CharField(max_length=300)
    comment_date= models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment    

# class Likes(models.Model):
#     user= models.ForeignKey(User,on_delete=models.CASCADE)
#     post= models.ForeignKey(Post,on_delete=models.CASCADE)
#     like = models.CharField(max_length=100)
#     def __str__(self):
#         return self.like

# class DisLikes(models.Model):
#     user= models.ForeignKey(User,on_delete=models.CASCADE)
#     post= models.ForeignKey(Post,on_delete=models.CASCADE)
#     dislike = models.CharField(max_length=100)
#     def __str__(self):
#         return self.dislike





