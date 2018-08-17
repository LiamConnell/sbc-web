from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json

from django.template import loader


@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }
    
    return render(request, 'auth0login/dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

def index(request):
    return render(request, 'auth0login/index.html')