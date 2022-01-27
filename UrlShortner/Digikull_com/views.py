from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from Digikull_com import models
import uuid


def Home(request):
    return render(request, "home.html")


@csrf_exempt
def Shorten(request):
    if request.method == "POST":
        link = request.POST
        uid = str(uuid.uuid4())[:5]
        models.UrlsTable.objects.create(
            main_url=link["link"],
            ShortUrl=f"localhost:8000/{uid}",
            description=link['description'],
            user_id=models.User.objects.get(id=request.POST['user_id']),
            uuid=uid
        )
    return HttpResponse(f"localhost:8000/{uid}")


@csrf_exempt
def Original(request, pk):
    data = models.UrlsTable.objects.get(uuid=pk)
    link = data.main_url
    return redirect(f'https://{link}')
