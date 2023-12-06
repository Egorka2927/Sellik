from django.shortcuts import render, redirect
from main.models import ListingList, Listing
from django.contrib.auth import logout
from django.http import HttpRequest
import datetime

# Create your views here.

def homePage(response):
    if response.method == "POST":
        if response.POST.get("create-option-button"):
            if response.user.is_authenticated:
                return redirect("/optionCreation")
            else:
                return redirect("/")
        elif response.POST.get("logout"):
            logout(response)
            return redirect("/")
    return render(response, "main/home.html", {})

def options(response):
    # print(response.COOKIES)
    categoryList = []
    listingTypeList = []
    dateList = []
    priceFrom = 0
    priceTo = 2 ** 31 - 1
    date = datetime.datetime.now().date()

    # if (response.session.has_key("categoryList")):
    #     # categoryList = response.session["categoryList"]
    #     categoryList = []
    # else:
    #     categoryList = []
    # if (response.session.has_key("listingTypeList")):
    #     # listingTypeList = response.session["listingTypeList"]
    #     listingTypeList = []
    # else:
    #     listingTypeList = []

    listingList = list(ListingList.objects.all().get().listing_set.all())
    # renderToResponse.set_cookie("categoryList", categoryList)
    typeChosen = False
    categoryChosen = False
    dateChosen = False
    if response.method == "POST":
        if response.POST.get("filter-apply-button"):
            if response.POST.get("buy"):
                typeChosen = True
                listingTypeList.append("Selling")
            if response.POST.get("rent"):
                typeChosen = True
                listingTypeList.append("Renting")
            if response.POST.get("donations"):
                typeChosen = True
                listingTypeList.append("Donating")

            if response.POST.get("electronics"):
                categoryChosen = True
                categoryList.append("electronics")
            if response.POST.get("furniture"):
                categoryChosen = True
                categoryList.append("furniture")
            if response.POST.get("books"):
                categoryChosen = True
                categoryList.append("books")
            if response.POST.get("clothing"):
                categoryChosen = True
                categoryList.append("clothing")
            if response.POST.get("vehicles"):
                categoryChosen = True
                categoryList.append("vehicles")
            if response.POST.get("appliences"):
                categoryChosen = True
                categoryList.append("appliences")
            if response.POST.get("jewelry"):
                categoryChosen = True
                categoryList.append("jewelry")
            if response.POST.get("sports"):
                categoryChosen = True
                categoryList.append("sports")
            if response.POST.get("toys"):
                categoryChosen = True
                categoryList.append("toys")
            if response.POST.get("collectibles"):
                categoryChosen = True
                categoryList.append("collectibles")
            if response.POST.get("others"):
                categoryChosen = True
                categoryList.append("others")

            if response.POST.get("price-from"):
                priceFrom = int(response.POST.get("price-from"))
            if response.POST.get("price-to"):
                priceTo = int(response.POST.get("price-to"))

            if response.POST.get("today"):
                date = datetime.datetime.now().date()
                dateChosen = True
                dateList.append("today")
            if response.POST.get("last-week"):
                date = (datetime.datetime.now() - datetime.timedelta(days=7)).date()
                dateChosen = True
                dateList.append("last-week")
            if response.POST.get("last-month"):
                date = (datetime.datetime.now() - datetime.timedelta(days=30)).date()
                dateChosen = True
                dateList.append("last-month")
                
            if not typeChosen:
                listingTypeList = []
                if not categoryChosen:
                    categoryList = []
                else:
                    listingList = list(ListingList.objects.all().get().listing_set.filter(category__in = categoryList))
            else:
                if not categoryChosen:
                    categoryList = []
                    listingList = list(ListingList.objects.all().get().listing_set.filter(listingType__in = listingTypeList))
                else:
                    listingList = list(ListingList.objects.all().get().listing_set.filter(category__in = categoryList, listingType__in = listingTypeList))
            # categoryList = ["electronics", "furniture", "books", "clothing", "vehicles", "appliences", "jewelry", "sports", "toys", "collectibles", "others"]

            # response.session["categoryList"] = categoryList
            # response.session["listingTypeList"] = listingTypeList
            for listing in reversed(listingList):
                if listing.price < priceFrom or listing.price > priceTo:
                    listingList.remove(listing)
            # not (listing.price >= priceFrom and listing.price <= priceTo)
            
            if dateChosen:
                for listing in reversed(listingList):
                    if listing.dateCreated < date:
                      listingList.remove(listing)            

        elif response.POST.get("filter-reset-button"):
            categoryList = []
            listingTypeList = []
            # response.session["categoryList"] = categoryList
            # response.session["listingTypeList"] = listingTypeList
            renderToResponse = render(response, "main/options.html", {"categoryList": categoryList,
            "listingTypeList": listingTypeList, "listingList": listingList, "priceFrom": priceFrom, "priceTo": priceTo, "dateList": dateList})
            return renderToResponse
    renderToResponse = render(response, "main/options.html", {"categoryList": categoryList,
    "listingTypeList": listingTypeList, "listingList": listingList, "priceFrom": priceFrom, "priceTo": priceTo, "dateList": dateList})
    return renderToResponse

def optionCreation(response):
    if response.method == "POST":
        if response.POST.get("create-button"):
                formPhoto = response.FILES["file"]
                formUsername = response.user.username
                formCategory = response.POST.get("category")
                formDescription = response.POST.get("description")
                if response.POST.get("listingType") == "buy":
                    formListingType = "Selling"
                elif response.POST.get("listingType") == "rent":
                    formListingType = "Renting"
                else:
                    formListingType = "Donating"
                formDate = response.POST.get("dateAvailable")
                formPrice = response.POST.get("price")
                formPhoneNumber = response.POST.get("phoneNumber")
                formContacts = response.POST.get("contacts")
                option = Listing(listingList = ListingList.objects.all().get(),
                                 username = formUsername,
                                 photo = formPhoto, 
                                 category = formCategory, 
                                 description = formDescription,
                                 listingType = formListingType,
                                 dateCreated = formDate,
                                 dateAvailable = formDate,
                                 price = formPrice,
                                 phoneNumber = formPhoneNumber,
                                 contacts = formContacts)
                if len(formCategory) > 0:
                    option.save()
                    return redirect("/")
    return render(response, "main/optionCreation.html", {})