from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name', '').strip()
        item_cost = request.POST.get('item_cost')

        # Validate input
        if not item_name or not item_cost:
            return redirect('view_cart')  # Handle missing values gracefully
        
        try:
            item_cost = float(item_cost)
        except ValueError:
            return redirect('view_cart')  # Handle invalid cost value

        # Retrieve and update cart safely
        try:
            cart = json.loads(request.COOKIES.get('cart', '[]'))
        except json.JSONDecodeError:
            cart = []  # Reset cart if JSON is invalid

        cart.append({'name': item_name, 'cost': item_cost})

        # Prepare response
        response = redirect('view_cart')
        response.set_cookie(
            'cart', 
            json.dumps(cart), 
            max_age=86400,  # Cookie expires in 1 day
            httponly=True,  # Prevent JavaScript access for security
            samesite='Lax'  # Improve security
        )
        return response
    return HttpResponse("Invalid request method", status=400)

def view_cart(request):
    cart = json.loads(request.COOKIES.get('cart', '[]'))
    total_cost = sum(item['cost'] for item in cart)
    return render(request, 'cart.html', {'cart': cart, 'total_cost': total_cost})

def clear_cart(request):
    response = redirect('view_cart')
    response.delete_cookie('cart')
    return response
