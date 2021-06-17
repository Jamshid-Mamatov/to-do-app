from django.shortcuts import render

from django.http import HttpResponse
import json
def rem(request):
    satr=""
    with open('sample.json', 'r') as openfile:
        json_object = json.load(openfile)
        item=json_object['tasks'][-1]
        json_object['tasks'].remove(item)
        print(json_object['tasks'])
 
        
    with open('sample.txt', 'w') as outfile:
        json.dump(json_object, outfile)
        print("54655")
        print(json_object['tasks'])
        

   

    # print(type(json_object))
    for i in json_object['tasks']:
        satr+=i
        satr+="<br>"

    return HttpResponse(satr)