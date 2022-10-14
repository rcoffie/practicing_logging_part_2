from django.shortcuts import render
from django.http import HttpResponse
import datetime
#import the logging library
import logging

#Get an instance of logger

logger = logging.getLogger(__name__)

# Create your views here.

def hello_reader(request):
    logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
    return HttpResponse("<h1>Hello FreeCodeCamp.org Reader :)</h1>")
