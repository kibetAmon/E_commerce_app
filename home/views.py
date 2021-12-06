from django.http import HttpResponse


# Views

def index(request):
    return HttpResponse("WELCOME TO NAIVAS GROCERY STORE.")
