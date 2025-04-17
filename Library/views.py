import json
from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt


from .models import Admin, Book
# Create your views here.

def admin_signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if Admin.objects.filter(email=email).exists():
            messages.error(request,'Admin already exists')
        else:
            Admin.objects.create_user(email=email,password=password)  
            messages.success(request,'Admin registerd successfully')  
    return render(request,'signup.html')  

def admin_login(request):
    if request.method=="POST":
        email=request.POST['email']  
        password=request.POST['password'] 
        user=authenticate(request,email=email,password=password)  
        if user:
            login(request,user)
            return redirect('list_books')
        else:
            messages.error(request,'Invalid credentials')
    return render(request,'login.html')    

@csrf_exempt
def create_book(request):
    if request.method=="POST":
        data=json.loads(request.body)
        book=Book.objects.create(title=data['title'],author=data['author'],published_date=data['published_date'])
        return JsonResponse({'message':'Book created','id':book.id})
    else:
        return HttpResponse('invalid id')

def list_books(request,book_id):
    books=list(Book.objects.values())
    return JsonResponse(books,safe=False)

@csrf_exempt
def update_book(request,book_id):
    if request.method=="PUT":
        data=json.loads(request.body)
        Book.objects.filter(id=book_id).update(title=data['title'],author=data['author'],published_date=data['published_date'])
        return JsonResponse({'message':'Book updated'})


def delete_book(request,book_id):
    if request.method=="DELETE":
        Book.objects.filter(id=book_id).delete()
        return JsonResponse({'message':'Book deleted'})

        