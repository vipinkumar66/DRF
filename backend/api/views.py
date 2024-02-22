import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # request -> HttpRequest
    body = request.body #This gives the string of json data
    request.GET #gives params
    data = {}
    try:
        data = json.loads(body) #This converts the string of json to dictionary
    except:
        pass
    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    return JsonResponse(data)