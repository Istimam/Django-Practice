from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    d = {'name': 'taylor Swift','nickName':'Swifty','hobby': "Like's to sing", 'age':20,'dob': datetime(1990, 5, 15, 8, 30, 0),'books':[
        {
            'name':'Bangla',
            'price':200,
            'quantity':5,
            'author':{'name':'Habib', 'age': 50},
            'fileSize':123456789
        },
        {
            'name':'English',
            'price':300,
            'quantity':10,
            'author':{'name':'Sajid', 'age': 40},
            'fileSize':123456789
        },
        {
            'name':'Maths',
            'price':400,
            'quantity':15,
            'author':{'name':'Tamim', 'age': 70},
            'fileSize':123456789
        },
        {
            'name':'BGS',
            'price':500,
            'quantity':20,
            'author':{'name':'Habib', 'age': 30}
        }
    ]}
    dict = { 
        'letter':['a','b','c']
    }
    sorted_books = sorted(d['books'], key=lambda x: x['name'])
    return render(request,'first_app/home.html',{'d': d,'sorted_books':sorted_books,'dict':dict})