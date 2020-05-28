from django.shortcuts import render,reverse
from .models import Movie,Category
from django.views.generic import CreateView
# Create your views here.
def MainView(request):
    #return render(request,'FKApp/index.html',{'movies':Movie.objects.all()})
    return render(request,'FKApp/index-category.html',{'categories':Category.objects.all()})


class InsertView(CreateView):
    model=Movie
    fields="__all__"
    #default template name =movie_form.html
    def get_success_url(self):
        return reverse("home")
