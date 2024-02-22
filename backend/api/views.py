from django.http import JsonResponse

def api_home(*args, **kwargs):
    return JsonResponse({"message":"Hey there is a response from the api home"})