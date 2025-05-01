from .models import Cart

def cart(request):
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        cart, _ = Cart.objects.get_or_create(session_key=session_key)
    
    return {'current_cart': cart}