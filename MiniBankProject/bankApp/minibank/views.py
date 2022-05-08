from django.shortcuts import render
from django.http import HttpResponse
import pymongo
connection = pymongo.MongoClient('localhost',27017)
database = connection['miniDB']
collection = database['miniuserCollection']

def home(request):
    return render(request,'home.html')

def add(request):
    uname = request.GET['name']
    upass = request.GET['password']
    uamount = request.GET['amount']
    try:
        register_id =exitRegister(uname)
        if register_id:
            print('Data is already exit!')
            return render(request,'result.html',{"id":register_id,'name':uname,'password':upass,'amount':uamount})
        else:
            queryInsert = {'name':uname,'password':upass,'amount':uamount}
            insertion(queryInsert)
            next_id = exitRegister(uname)
            return render(request,'result.html',{"id":next_id,'name':uname,'password':upass,'amount':uamount})
    except Exception as err:
        print(err)

def exitRegister(name):
    try:
        query = {"name": name}
        result = collection.find(query)
        for i in result:
            register_id = i.get("_id")
            print("User email : ", register_id)
        return register_id
    except Exception as err:
        print(err)

def insertion(userForm):
    try:
        userInformation = collection.insert_one(userForm)
        print('Data are inserted...', userInformation.inserted_id)
    except Exception as err:
        print(err)

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def userlogin(request):
    uname = request.GET['name']
    upass = request.GET['password']
    try:
        result_id = exitUser(uname, upass)
        print('from DB ',result_id)
        if result_id:
            print('Login Successful...')
            findData = collection.find_one({'_id':result_id})
            id,name,password,amount = findData['_id'],findData['name'],findData['password'],findData['amount']
            return render(request,'result.html',{"id":id,'name':name,'password':password,'amount':amount})
        else:
            print('Login Fail!')
            return render(request,'loginfail.html')
    except Exception as err:
        print(err)

def exitUser(name, passcode):
    try:
        query = {"name": name, "password": passcode}
        result = collection.find(query)
        for i in result:
            login_id = i.get("_id")
            print("User login ID : ", login_id)
        return login_id
    except Exception as err:
        print(err)
