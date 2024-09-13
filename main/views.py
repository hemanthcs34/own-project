from django.shortcuts import render, redirect, get_object_or_404
from .models import American
from .forms import AmericanForm

# Create your views here.
def menu_list(request):
    menu = American.objects.all()
    return render(request, 'menu_list.html', {'menu': menu})

def add_menu(request):
    if request.method == 'POST':
        form = AmericanForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
          
            menu.save()
            return redirect('menu_list')  # Make sure this name matches your URL pattern
    else:
        form = AmericanForm()
    
    return render(request, 'add_menu.html', {'form': form})
def delete_menu(request, pk):
    menu = get_object_or_404(American, pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    
    return render(request, 'delete_menu.html', {'menu': menu})

def update_menu(request, pk):
    menu = get_object_or_404(American, pk=pk)
    if request.method == 'POST':
        form = AmericanForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = AmericanForm(instance=menu)
    
    return render(request, 'update_menu.html', {'form': form, 'menu':menu})