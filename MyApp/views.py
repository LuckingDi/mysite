from django.shortcuts import render
from .models import Person, Album
from django.http import Http404
# Create your views here.


def index(request):
    a = Person.objects.all()
    return render(request, 'MyApp/index.html', {'a': a})


def album_get(request, person_id):
    try:
        p = Person.objects.get(pk=person_id)
        a = p.album_set.all()
    except Person.DoesNotExist:
        raise Http404("人员不存在")
    return render(request, 'MyApp/album_get.html', {'a': a})
