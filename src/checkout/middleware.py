from .models import CartItem



def cart_item_middleware(get_response):
    def middleware(request):
        session_key = request.session.session_key
        response = get_response(request)
        if session_key != request.session.session_key:
			if(CartItem.objects.filter(cart_key=session_key).count() > 0 and request.session.session_key != None):
				CartItem.objects.filter(cart_key=session_key).update(
					cart_key=request.session.session_key
					)
        return response
    return middleware