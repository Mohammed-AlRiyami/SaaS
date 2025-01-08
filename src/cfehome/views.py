from django.http import HttpResponse
import pathlib
from django.shortcuts import render

def home_home_view(request, *args, **kwargs): 
    my_title = "Mo's Page"
    my_context = {
        "page_title": my_title,
    }
    html_template = "home.html"
    
    return render(request, html_template, my_context)

# def home_home_view(request, *args, **kwargs): 
#     print(this_dir)
#     html_ = ""
#     html_file_path= this_dir/"home.html"
#     html_ = html_file_path.read_text()
#     return HttpResponse(html_)