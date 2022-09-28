
from email import message
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category_name}"

class Bid(models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")

    def __str__(self):
       return f"Bid of {self.bid} from {self.user}"

class auction_list(models.Model):
    title = models.CharField(max_length=50)
    descrption = models.CharField(max_length=4000)
    image = models.CharField(max_length=1000)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="given_bid", default=None)
    isactive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, null = True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")

    def __str__(self):
        return f"{self.title}"




class comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    listing = models.ForeignKey(auction_list, on_delete=models.CASCADE, related_name="listing")
    message = models.CharField(max_length=3000, default="")

    def __str__(self):
        return f"{self.author} commented on {self.listing}"