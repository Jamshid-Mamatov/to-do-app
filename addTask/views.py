from django.shortcuts import render
from django.http import HttpResponse
import json
information={}
information['tasks']=[]

def home(request):
    home_page='''
    <h1 style= color:red;text-align:center> added task </h1>
    '''
    information['tasks'].append("ishi qii")    

    print(information)
    inform=json.dumps(information)
    with open("sample.json", "w") as outfile:
        outfile.write(inform)

    return HttpResponse(home_page)



