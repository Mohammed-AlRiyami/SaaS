from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit


def home_view(request, *args, **kwargs): 
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs): 
    
    # queryset = PageVisit.objects.all()
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "Mo's Page"
    html_template = "home.html"
    try:
        percent= (page_qs.count()*100)/qs.count()
    except:
        percent = 0
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(), 
        "percent": percent,
        "total_visit_count": qs.count()
    }
    
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
# def home_home_view(request, *args, **kwargs): 
#     print(this_dir)
#     html_ = ""
#     html_file_path= this_dir/"home.html"
#     html_ = html_file_path.read_text()
#     return HttpResponse(html_)