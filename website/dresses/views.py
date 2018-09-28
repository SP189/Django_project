
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from .models import Lehengas
# from django.template import loader
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from .forms import UserForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core import *
from django.template.context_processors import csrf
from cart.cart import Cart
from cart.forms import CartAddProductForm
from tkinter import messagebox



# Create your views here.

def product_list(request):
    lehengas = Lehengas.objects.all()
    context = {
        'obj':lehengas
    }
    return render(request, 'dresses/list.html' , context)


def product_detail(request, id,):
    product = get_object_or_404(Lehengas, id=id, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'dresses/detail2.html', context)

class IndexView(generic.ListView):
    template_name = 'dresses/index.html'

    def get_queryset(self):
        return Lehengas.objects.all()


class DetailView(generic.DetailView):
    model = Lehengas
    template_name = 'dresses/detail2.html'


class LehengasCreate(CreateView):
    model = Lehengas
    fields = ['lehenga_desc', 'lehenga_size', 'lehenga_pic','lehenga_price','available','stock']

class LehengasUpdate(UpdateView):
    model = Lehengas
    fields = ['lehenga_desc', 'lehenga_size', 'lehenga_pic','lehenga_price','available','stock']

class LehengasDelete(DeleteView):
    model = Lehengas
    success_url = reverse_lazy('dresses:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'dresses/registration_form.html'

    #dispaly blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    #procss form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #change password
            user.set_password(password)
            user.save()

            #returns User obj if all is correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request)
                    return redirect('dresses:index')

        #if all is not correct, return blank form
        return render(request, self.template_name, {'form': form})


def login(request):
    c = {
    }
    c.update(csrf(request))
    return render_to_response('dresses/login.html', c)

def logout(request):
    return redirect('dresses:index')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        return redirect('dresses:index')
    else:
        msg = 'Please enter correct Username and Password'
        messagebox.showerror("Error", msg)
        return render(request, 'dresses/login.html', {'error': msg})

class DescView(generic.ListView):
    model = Lehengas
    template_name = 'dresses/description.html'

    def get_queryset(self):
        return Lehengas.objects.all()

def search_list(request):
    search_term = Lehengas.objects.all()
    query = request.GET.get("q")
    if query:
        search_term = search_term.filter(lehenga_desc__icontains=query)
    page_req = 'page'
    page = request.GET.get(page_req, 1)
    paginator = Paginator(search_term, 10)
    try:
        lehengas = paginator.page(page)
    except PageNotAnInteger:
        lehengas = paginator.page(1)
    except EmptyPage:
        lehengas = paginator.page(paginator.num_pages)
    context = {
        "object_list": search_term,
        "legenga_size": query
    }
    return render(request, 'dresses/search.html', {'lehengas':lehengas})
