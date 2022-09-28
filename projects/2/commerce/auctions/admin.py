from django.contrib import admin
from .models import Bid, User,Category,auction_list, comments
# Register your models here.



admin.site.register(User)
admin.site.register(Category)
admin.site.register(auction_list)
admin.site.register(comments)
admin.site.register(Bid)
