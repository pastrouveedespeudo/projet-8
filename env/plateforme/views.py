"""Here we discuss with home, mention and errors templates"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    """Template home"""
	fjpezfpojzepf
    return render(request, "home.html", {})

def mention(request):
    """template mention"""

    return render(request, "mention.html", {})

def handler404(request, exception, template_name="error.html"):
    """handler404 error template"""

    return render(request, "error.html", {'message':'Page non trouvée'})

def handler500(request):
    """handler500 error template"""
    
    return render(request, "error.html", {'message':'Erreur 505'})
