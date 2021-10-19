from django.db import models

# Create your models here.
from datetime import datetime


# class Book(models.Model):
#     title = models.TextField()
#     rating = models.FloatField()
#     author_name=models.TextField()
#     publisher_name = models.TextField()

# class Author(models.Model):
#     name = models.TextField()
#     hometown = models.TextField()

# #book = Book.objects.get(...)
# # author = Author.objects.get(name=book.author_name)
# #print(author.hometown)


# class Publisher(models.Model):
#     name = models.TextField()
#     founding_year = models.IntegerField()


#publisher = Publisher.objects.get(name=book.publisher_name)
#print(publisher.founding_year)


#publisher = Publisher.objects.get(...)
#book = Book.objects.filter(publisher_name=publisher.name)





class User(models.Model):
    email = models.EmailField()
    last_login = models.DateTimeField(null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    name = models.TextField()
    picture_url = models.URLField(blank=True)
    headline = models.TextField(blank=True)
    likes_cats = models.BooleanField(default=True)

class Article(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=60)
    sub_title = models.CharField(max_length=100, blank=True)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    users_that_like = models.ManyToManyField(User, related_name="liked_articles", related_query_name="liked_article")

#profile.user.email


#u.article_set.all()
#Article.objects.all()




#u = User.objects.first()
#u
# u.article_set.all()
# u.liked_articles.all()
# my_article = u.article_set.first()
# my_article.title
# u.liked_articles.add(my_article)
# my_article_users_that_like.all()
#  #########