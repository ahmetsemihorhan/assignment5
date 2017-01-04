from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import Blogx
from .forms import BlogxForm

def entry1(request):

    if request.method == "POST":
        formx = BlogxForm(request.POST)
        if formx.is_valid():
            blog_semih = formx.save(commit=False)
            blog_semih.ownerx = request.user
            blog_semih.save()
            formx.save_m2m()

    elif request.method == "GET":
        formx = BlogxForm()

    return render(request, "my_blog.html", {"blogn": Blogx.objects.filter(ownerx=request.user.id),
                                             "tagsx": Tag.objects.all(),
                                             "formx": formx})

def entry2(request, blog_id):
    try:
        blog_semih = Blogx.objects.get(id=blog_id)
        if request.user.id != blog_semih.ownerx.id:
            raise PermissionDenied
        return render(request, "detailed_blog.html", {"blog_semih": blog_semih})
    except Blogx.DoesNotExist:
        raise Http404("We don't have any.")

@permission_required('is_superuser')
def all_entries(request):
    return render(request, "my_blog.html", {"blogn": Blogx.objects.all()})

@permission_required('is_superuser')
def show_all_entries(request, userId):
    return render(request, "my_blog.html", {"blogn": Blogx.objects.filter(ownerx=userId)})
