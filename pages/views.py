from django.http import HttpResponse, HttpResponseRedirect


def home_page_view(request):
    return HttpResponse("Hello world")
