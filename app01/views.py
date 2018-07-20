from django.shortcuts import render
from django.http import JsonResponse
from app01 import models

# Create your views here.

def imgs(request):
    # img_list = models.Img.objects.all()
    return render(request, 'img.html')


def get_imgs(request):
    nid = request.GET.get('nid')
    img_list = list(models.Img.objects.filter(id__gt=nid).values('id', 'src', 'title'))
    ret = {
        'status': True,
        'data': img_list
    }
    return JsonResponse(ret)
