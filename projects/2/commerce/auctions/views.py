

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,Category,auction_list,Bid,comments


def index(request):
    active_auction_list = auction_list.objects.filter(isactive = True)
    return render(request, "auctions/index.html",{
        "auction_list": active_auction_list
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "GET":
        all_cat = Category.objects.all()
        return render(request, "auctions/create.html",{
            "categories":all_cat
        })

    else:
        #  Getting the data from the form
        title = request.POST["title"]
        description = request.POST["content"]
        start_bid = request.POST["start_bid"]
        image_url = request.POST["image_url"]
        category = request.POST["category"]
        new_cat = Category.objects.get(category_name = category)

        currentuser = request.user
        # create  a bid
        bid = Bid(bid=float(start_bid), user = currentuser)
        bid.save()
        #  Creating new list object and add data
        new_auction_list = auction_list(title= title, descrption= description, image= image_url,price = bid,category = new_cat,owner= currentuser)

        #  Save the object to our database
        new_auction_list.save()
        #  Redirect to home page
        return HttpResponseRedirect(reverse("index"))

def categories(request):
    if request.method == "GET":
        all_cat = Category.objects.all()
        return render(request, "auctions/categories.html",{
                "categories":all_cat,
            })
    else:
        cat = request.POST["category"]
        new_cat = Category.objects.get(category_name = cat)
        active_auction_list = auction_list.objects.filter(isactive = True, category = new_cat)
        return render(request, "auctions/index.html",{
            "auction_list": active_auction_list
        })

def listing(request,id):
    listing = auction_list.objects.get(pk=id)
    is_list_in_watch = request.user in listing.watchlist.all()
    all_comments = comments.objects.filter(listing=listing)
    owner = request.user.username == listing.owner.username
    return render(request, "auctions/listing.html",{
        "a":listing,
        "is_list_in_watch": is_list_in_watch,
        "all_comments":all_comments,
        "owner":owner

    })

def remove_watch(request,id):
    listing = auction_list.objects.get(pk=id)
    current_user = request.user
    listing.watchlist.remove(current_user)
    return HttpResponseRedirect(reverse("listing",args=(id, )))
    

def add_watch(request,id):
    listing = auction_list.objects.get(pk=id)
    current_user = request.user
    listing.watchlist.add(current_user)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def watchlist(request):
    user = request.user
    w = user.watchlist.all()
    return render(request, "auctions/index.html",{
        "auction_list": w
    })

def add_comment(request, id):
    current_user = request.user
    listing      = auction_list.objects.get(pk=id)
    message      = request.POST['comment']
    new_comment  = comments(
        author   = current_user,
        listing  = listing,
        message  = message
    )
    
    new_comment.save()
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def add_bid(request,id):
    new_bid = request.POST["new_bid"]
    listing_data = auction_list.objects.get(pk=id)
    is_list_in_watch = request.user in listing_data.watchlist.all()
    all_comments = comments.objects.filter(listing=listing_data)
    if int(new_bid)>int(listing_data.price.bid):
        update_bid = Bid(user = request.user, bid = new_bid)
        update_bid.save()
        listing_data.price = update_bid
        listing_data.save()
        return render(request, "auctions/listing.html",{
            "a":listing_data,
            "message":"Bid updated successfully",
            "update" :True,
            "is_list_in_watch": is_list_in_watch,
            "all_comments":all_comments,
        })
    else:
        return render(request, "auctions/listing.html",{
            "a":listing_data,
            "message":"Bid updated failed",
            "update" :False,
            "is_list_in_watch": is_list_in_watch,
            "all_comments":all_comments,
            
        })

def close_auction(request,id):
    listing_data = auction_list.objects.get(pk=id)
    listing_data.isactive = False
    listing_data.save()
    is_list_in_watch = request.user in listing_data.watchlist.all()
    all_comments = comments.objects.filter(listing=listing_data)
    owner = request.user.username == listing_data.owner.username
    return render(request, "auctions/listing.html",{
        "a":listing_data,
        "is_list_in_watch": is_list_in_watch,
        "all_comments":all_comments,
        "owner":owner,
        "update" :True,
        "message":"Auction is Closed",

    })
    