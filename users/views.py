from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse  # Добавь этот импорт
from .forms import RegisterForm, LoginForm
from .models import Cart, CartItem
from catalog.models import T_shirt, Sweatshirt

def register_view(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Корзина создастся автоматически через сигнал (если добавишь)
            # Но на всякий случай создаем её здесь
            Cart.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, 'Registration successful!')
            # ИСПРАВЛЕНО: Добавлен namespace
            return redirect('users:profile')  # Было просто 'profile'
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    """Вход пользователя"""
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Проверяем наличие корзины при входе
                Cart.objects.get_or_create(user=user)
                messages.success(request, f'Welcome back, {username}!')
                
                # Перенаправляем на предыдущую страницу, если была
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                # ИСПРАВЛЕНО: Добавлен namespace
                return redirect('users:profile')  # Было просто 'profile'
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    """Выход пользователя"""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('main')  # Это должно быть в myapp

@login_required
def profile_view(request):
    """Профиль пользователя с корзиной"""
    # Получаем или создаем корзину для пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total_price = cart.get_total_price()
    
    context = {
        'user': request.user,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'users/profile.html', context)

@login_required
def add_to_cart(request, item_type, item_id):
    """Добавление товара в корзину"""
    # Получаем или создаем корзину для пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        size = request.POST.get('size', 'S')
        quantity = int(request.POST.get('quantity', 1))
        
        if item_type == 't-shirt':
            item = get_object_or_404(T_shirt, id=item_id)
            
            # Проверяем, есть ли уже такой товар в корзине
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                t_shirt=item,
                size=size,
                defaults={'quantity': quantity}
            )
            
            if not created:
                # Если товар уже есть, увеличиваем количество
                cart_item.quantity += quantity
                cart_item.save()
                messages.success(request, f'Added {quantity} more {item.name} (Size: {size}) to cart!')
            else:
                messages.success(request, f'{item.name} (Size: {size}) added to cart!')
                
        elif item_type == 'sweatshirt':
            item = get_object_or_404(Sweatshirt, id=item_id)
            
            # Проверяем, есть ли уже такой товар в корзине
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                sweatshirt=item,
                size=size,
                defaults={'quantity': quantity}
            )
            
            if not created:
                # Если товар уже есть, увеличиваем количество
                cart_item.quantity += quantity
                cart_item.save()
                messages.success(request, f'Added {quantity} more {item.name} (Size: {size}) to cart!')
            else:
                messages.success(request, f'{item.name} (Size: {size}) added to cart!')
        else:
            messages.error(request, 'Invalid item type')
            return redirect('collections:collec')
    
    # Возвращаемся на предыдущую страницу
    return redirect(request.META.get('HTTP_REFERER', 'users:profile'))

@login_required
def update_cart_item(request, item_id):
    """Обновление количества товара или удаление из корзины"""
    # Получаем корзину пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Получаем элемент корзины
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'increase':
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, 'Quantity increased')
            
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.success(request, 'Quantity decreased')
            else:
                # Если количество стало 0, удаляем товар
                cart_item.delete()
                messages.success(request, 'Item removed from cart')
                
        elif action == 'remove':
            cart_item.delete()
            messages.success(request, 'Item removed from cart')
    
    return redirect('users:profile')

@login_required
def checkout(request):
    """Оформление заказа"""
    # Получаем корзину пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    
    if not cart_items:
        messages.warning(request, 'Your cart is empty!')
        return redirect('users:profile')
    
    if request.method == 'POST':
        # Здесь будет логика оформления заказа
        # Например, создание заказа, списание денег и т.д.
        
        # Пока просто очищаем корзину
        cart_items.delete()
        messages.success(request, 'Order placed successfully! Thank you for your purchase.')
        return redirect('users:profile')
    
    total_price = cart.get_total_price()
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'users/checkout.html', context)

@login_required
def clear_cart(request):
    """Очистка всей корзины"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.items.all().delete()
    messages.success(request, 'Cart cleared successfully')
    return redirect('users:profile')