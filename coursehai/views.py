from typing import Container, List
from django.shortcuts import render
from django.http.response import HttpResponse
from . models import Ecomapp11,Contact,order,Ownshop

import json
# Create your views here.

def Shop(request):
    # list=Ecomapp11.objects.all() this line is to get all the data from databses
    Allcat=Ecomapp11.objects.values("category")
    # cato={var['category'] for var in Allcat} #this is a dictionary for we use set() in python to stop dupilcate of values in dictionary
    # this is same as above
    cato=[]
    for var in Allcat:
        cato.append(var['category'])
    cato=set(cato)    
    
    
    list={}
    for val in cato:
        # list{"Daily use":[shoes,chair setup,default image]} basically we first created list and in first list key we made array
        list[val]=Ecomapp11.objects.filter(category=val)
    print(list)
    params={
        "Data":list}
    return render(request,'course1/List.html',params)

def detail(request,id):

    # id=request.GET.get("id")
    try:
        params={"Data":Ecomapp11.objects.get(id=id),"error":"null"}
    except:
        params={"error":"Product doesnt exists"}

    

    print(params)
    return render(request,'course1/Details.html',params)

def Cartpage(request):
    return render(request,'course1/Cartpage.html')


 
def Contactus(request):
    return render(request,'course1/Contact.html')   

def Contactsubmit(request):
    email=request.POST.get("email")
    name=request.POST.get("name")
    phone=request.POST.get("phone")
    desc=request.POST.get("desc")
    image1=request.FILES['screenshot']
    selfcontact=Contact(Name=name,Email=email,Tel=phone,Image=image1,Desc=desc)
    selfcontact.save()
    return HttpResponse("<h1>thanks for the response</h1><a href='/shop'><button style='background-color: #0275d8; color:white; /* Green */ border: none; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px;'>Click here to shop</button></a>")
    

def checkout(request):
    str = request.POST.get("cartJson")
    cart = json.loads(str)
    currentCart = cart


    totalPrice = 0 
    for id in cart:
        temp= cart[id]
        tempOb = Ecomapp11.objects.get(id=id)
        price = tempOb.price
        temp["price"]=price
        temp["totalItemPrice"] = price * temp["value"]
        totalPrice = totalPrice + temp["totalItemPrice"]
        currentCart[id] = temp 
    param= {
        "totalPrice" :totalPrice,
        "data":currentCart
    }
    return render(request,'course1/Checkout.html',param)   


def submitcheckout(request):
    jsonCart= request.POST.get("jsonCart")
    first_name= request.POST.get("first_name")
    last_name= request.POST.get("last_name")
    email= request.POST.get("email")
    address= request.POST.get("address")
    state= request.POST.get("state")
    zip= request.POST.get("zip")
    isSameBillingAddress= request.POST.get("isSameBillingAddress")
    if(isSameBillingAddress=="on"):
        isSameBillingAddress = True
    else:
        isSameBillingAddress = False
    newOrder = order(jsonCart=jsonCart,email=email, first_name=first_name ,last_name=last_name,state=state,zip=zip,address=address,isSameBillingAddress=isSameBillingAddress)
    newOrder.save()
    return HttpResponse("Thank you for ordering!!")
            

def blogcreate(request):
    return render(request,'course1/blogcreate.html')   

def displayblog(request):
    title=request.POST.get("name2")
    desc1=request.POST.get("desc2")
    price1=request.POST.get("phone2")
    image1=request.FILES['image2']
    ownshop1=Ownshop(title1=title,desc1=desc1,price1=price1,image1=image1)
    ownshop1.save()

    
    blog_shop=Ownshop.objects.all()
    parames={
        "data":blog_shop
    }
    return render(request,'course1/displayblog.html',parames)   

