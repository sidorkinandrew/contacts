from django.shortcuts import render, get_object_or_404

from .models import Contact

from django.views.generic import ListView, DetailView

# Create your views here

#def home(request):
#    context = {
#        'status': 'Working on this Django Contacts project app',
#        'contacts': Contact.objects.all,
#    }
#    return render(request, 'index.html', context)

#def detail(request, id):
#    context = {
#        'contact': get_object_or_404(Contact, pk=id)
#    }
#    return render(request, 'detail.html', context)

class HomeView(ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    model = Contact
    template_name = "detail.html"
    context_object_name = 'contact'

def search(request):
    context = {
        
    }
    return render(request, 'search.html', context)