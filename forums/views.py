from django.http import HttpResponse
from django.shortcuts import render
import getpass
user = getpass.getuser()

def index(reguest):
    return HttpResponse('Hello ' + user)

