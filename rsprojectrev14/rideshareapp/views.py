from django.shortcuts import render, get_object_or_404, redirect 
from .models import Route 
from .forms import RouteForm

# List all Routes 
def route_list(request): 
    routes = Route.objects.all() 
    return render(request, 'routes/route_list.html', {'routes': routes}) 

# Create a New Route 
def route_create(request): 
    if request.method == 'POST': 
        form = RouteForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('route_list') 
    else: 
        form = RouteForm() 
    return render(request, 'routes/route_form.html', {'form': form}) 

# Update an Existing Route 
def route_update(request, pk): 
    route = get_object_or_404(Route, pk=pk) 
    if request.method == 'POST': 
        form = RouteForm(request.POST, instance=route) 
        if form.is_valid(): 
            form.save() 
            return redirect('route_list') 
    else: 
        form = RouteForm(instance=route) 
    return render(request, 'routes/route_form.html', {'form': form}) 

# Delete a Route 
def route_delete(request, pk): 
    route = get_object_or_404(Route, pk=pk) 
    if request.method == 'POST': 
        route.delete() 
        return redirect('route_list') 
    return render(request, 'routes/route_confirm_delete.html', {'route': route})

# Home
def route_base(request): 
    return render(request, 'base.html') 