from django.shortcuts import render, redirect

# Create your views here.
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.http import HttpResponse
from django.template import loader,Context


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return redirect('orders:completion_msg')#render(request, 'orders/order/create.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})

def completed(request):
    temp = loader.get_template('orders/order/created.html')
    return HttpResponse(temp.render())