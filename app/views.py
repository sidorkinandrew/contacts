from django.shortcuts import render

from .models import Contact

# Create your views here

def home(request):
    context = {
        'status': 'Working on this Django Contacts project app',
        'contacts': Contact.objects.all,
    }
    return render(request, 'index.html', context)