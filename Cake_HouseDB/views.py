from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Client


def index_page(request):
    data = Client.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def edit_page(request):
    return render(request, "edit.html")


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # email = request.POST.get('email')
        caketype = request.POST.get('caketype')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        phone = request.POST.get('phone')
        orderdate = request.POST.get('orderdate')
        deliverydate = request.POST.get('deliverydate')

        query = Client(name=name, caketype=caketype, quantity=quantity, price=price, phone=phone, orderdate=orderdate, deliverydate=deliverydate)
        query.save()
        return redirect("/")

        return render(request, 'index.html')


def deleteData(request, id):
    d = Client.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        # email = request.POST.get('email')
        caketype = request.POST.get('caketype')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        phone = request.POST.get('phone')
        orderdate = request.POST.get('orderdate')
        deliverydate = request.POST.get('deliverydate')

        update_info = Student.objects.get(id=id)
        update_info.name = name
        # update_info.email = email
        update_info.caketype = caketype
        update_info.quantity = quantity
        update_info.price = price
        update_info.phone = phone
        update_info.orderdate = orderdate
        update_info.deliverydate = deliverydate
        update_info.save()

        return redirect("/")

    d = Client.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)

