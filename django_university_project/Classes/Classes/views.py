from django.http import HttpResponse

def home (request):
    user= request.user
    return HttpResponse("<h1>Welcome {}! </h1>".format(user))