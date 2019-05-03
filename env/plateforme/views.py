"""Here we discuss with home, mention and errors templates"""


import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


def home(request):
    """Template home"""
    logger.info('New search', exc_info=True, extra={
        # Optionally pass a request and we'll grab any information we can
    	'request': request,
    })

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
