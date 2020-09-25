from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here

# def home(request):
#    context = {
#        'status': 'Working on this Django Contacts project app',
#        'contacts': Contact.objects.all,
#    }
#    return render(request, 'index.html', context)

# def detail(request, id):
#    context = {
#        'contact': get_object_or_404(Contact, pk=id)
#    }
#    return render(request, 'detail.html', context)


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'
    
    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager = self.request.user)


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "detail.html"
    context_object_name = 'contact'

@login_required
def search(request):
    #    context = {'search_term': "",}
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(info__icontains=search_term) |
            Q(phone__icontains=search_term)
        )
        context = {
            'search_term': search_term,
            'contacts': search_results,
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = "create.html"
    fields = ['name', 'email', 'phone', 'gender', 'info', 'image']
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        return redirect('home')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = "update.html"
    fields = ['name', 'email', 'phone', 'gender', 'info', 'image']
    # success_url = '/' default behavior

    def form_valid(self, form):
        instance = form.save()
        return redirect('detail', instance.id)

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "delete.html"
#    fields = ['name', 'email', 'phone', 'gender', 'info', 'image']
    success_url = '/'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

