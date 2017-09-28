from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from checkout.models import CartItem
def home(request):
	c = {}
	populateCart(request,c)
	populateContext(request,c)
	return render(request, 'home.html', c)
def loginview(request):
    c = {}
    populateContext(request, c)
    c.update(csrf(request))
    return render_to_response('account/login.html', c)

def auth_and_login(request, onsuccess='/', onfail='/login/'):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        c = {}
        populateContext(request, c)
        return redirect(onsuccess)
    else:
        return redirect(onfail)  
def logout(request):
	context = {}
	try:
		auth_logout(request)
	except:
		context['error'] = 'Some error occured.'
	
	populateContext(request, context)
	return render(request, 'home.html', context)
def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def sign_up_in(request):
    post = request.POST
    if not user_exists(post['email']): 
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
    	return auth_and_login(request)
    else:
    	return redirect("/login/")

@login_required(login_url='/login/')
def secured(request):
    return render_to_response("secure.html")

def populateContext(request, context):
	context['authenticated'] = request.user.is_authenticated()
	if context['authenticated'] == True:
		context['username'] = request.user.username
def populateCart(request, context):
    session = request.session.session_key
    if session and CartItem.objects.filter(cart_key=session).exists():
        context['cart'] = CartItem.objects.filter(cart_key=session)
        print context['cart']
        print context['cart'].count()
        context['cart_count'] = context['cart'].count()
    else:
        print "cart is empty"