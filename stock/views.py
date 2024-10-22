import csv
from django.contrib import messages
from django.shortcuts import render,redirect,get_list_or_404
from django.http import HttpResponse
# from stock.models import ProductTable
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Products,Order
from .forms import SearchItemsForm,ProductCreateForm,OrderForm
from stock import views
from django.db.models import Q

@login_required
def orders(request):
    title = "Service Users"
    orders = Order.objects.all()
    context = {
        "title":title,
        'orders':orders,
        
    }
    return render(request,'dashboard/orders.html',context)
@login_required
def update(request):
    header = "Add Item"
    form = OrderForm(request.POST or None)
    orders = Order.objects.all()
    context = {
        'header':header,
        'form':form,
        'orders':orders,
    }
    return render(request,'manager/update_admin.html', context)


@login_required
def list_items(request):

    return render(request, 'list_items.html')


@login_required
def add_items(request):
    return render(request, 'adm_add_items.html')


@login_required
def update_items(request, pk):
    # queryset = Products.objects.get(id=pk)
    # form = StockUpdateForm(instance=queryset)
    # if request.method == 'POST':
    #     form = StockUpdateForm(request.POST, instance=queryset)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,'Successfully saved')
    #         return redirect('/list_items')

    # context = {
    #     'form': form
    # }
    return render(request, 'add_items.html')


@login_required
def delete_items(request, pk):
    # queryset = Products.objects.get(id = pk)
    # if request.method == 'POST':
    #     queryset.delete()
    #     messages.success(request,'Deleted Successfully')
    #     return redirect('/list_items')
    return render(request, 'delete_items.html')


@login_required
def stock_detail(request, pk):
    queryset = Products.objects.get(id=pk)
    context = {
        "title":queryset.item_name,
        "queryset":queryset,

    }
    return render(request,"stock_detail.html", context)

@login_required
def issue_items(request, pk):
    # queryset = Products.objects.get(id=pk)
    # form = IssueForm(request.POST or None, instance=queryset)
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     instance.receive_quantity = 0
    #     instance.quantity -= instance.issue_quantity
    #     instance.issue_by = str(request.user)
    #     # instance.issue_by = str(request.user)
    #     instance.save()
    #     messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
    #     return redirect('/stock_detail/' + str(instance.id))

    # context = {
    #     "title": "Issue " + str(queryset.item_name),
    #     "queryset": queryset,
    #     "form": form,
    #     "username": "Issue By: " + str(request.user),
    # }
    return render(request, "add_items.html",)

@login_required
def receive_items(request, pk):
    return render(request, "add_items.html",)

@login_required
def reorder_level(request,pk):
    return render(request, "add_items.html",)

@login_required
def list_history(request):
    return render(request, "list_history.html",)
# Admin views
@csrf_protect
@login_required(login_url='login')
def admin_panel(request):
    title = "Administration"
    order = Order.objects.all()
    product = Products.objects.all()
    context = {
        "title":title,
        'order':order,
        'product':product,
    }
    return render(request,'dashboard/admin_panel.html',context)

@login_required
def adm_add_items(request):
    title = "Add products"
    # Django ORM
    items = Products.objects.all()
    form = ProductCreateForm()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully saved')
            return redirect('adm_add_items')
         
    context ={
        "title":title,
        "form":form,
        "items":items
    }
    return render(request, 'dashboard/adm_add_items.html', context)
def deleteProduct(request,pk):
    item = Products.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('adm_add_items')
    return render(request,'dashboard/delete_item.html')
def editProduct(request, pk):
    # to prefill the forms,,instance = item
    item = Products.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductCreateForm(request.POST,instance = item)
        if form.is_valid():
            form.save()
            messages.success(request,'Product updated successfully')
            return redirect('adm_add_items')
    else:
        form = ProductCreateForm(instance=item)
    
    context = {
        'form':form,
        'item':item
    }
    return render(request,'dashboard/update_item.html',context)
@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect('page')
    return render(request, 'list_items.html')

@login_required
def lab_manager_dashboard(request):
    if not request.user.is_lab_manager:
        return redirect('page')
    return render(request, 'orders.html')
# manager views

@login_required
def manager_view(request):
    form = SearchItemsForm(request.GET)
    items = Products.objects.all()
    item_count = items.count()
    if form.is_valid():
        category = form.cleaned_data.get('category')
        item_name = form.cleaned_data.get('item_name')
        if category:
            items = items.filter(category=category)
        if item_name:
            items = items.filter(item_name__icontains=item_name)
     
   

    context = {
        'form': form,
        # 'product':prod,
        'item_count':item_count,
        'items':items
    
    }
    return render(request, 'manager/manager.html', context)


@login_required
def add_items_update(request):
    header = "Add Item"
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Successfully saved')
        return redirect('/update_admin')
    context = {
        "form":form,
        "title":header,
    }
    return render(request, 'update_admin.html', context)

@login_required
def category_items_view(request, category_id):
    # items = Products.objects.filter(category_id=category_id)
    return render(request, 'category_items.html',)

@login_required
def add_items_view(request):
    # if request.method == 'POST':
    #     selected_items = request.POST.getlist('selected_items')
    #     items = Products.objects.filter(id__in=selected_items)
    #     form = LabInfoForm()
    #     context = {'items': items, 'form': form}
    #     return render(request, 'selected_items.html',context)
    return redirect('manager_view')

@login_required
def download_csv(request):
    # if request.method == 'POST':
    #     form = LabInfoForm(request.POST)
    #     if form.is_valid():
    #         lab_name = form.cleaned_data['lab_name']
    #         lab_id = form.cleaned_data['lab_id']
    #         user_name = form.cleaned_data['user_name']
    #         phone = form.cleaned_data['phone']
    #         items = Products.objects.filter(id__in=request.POST.getlist('item_ids'))

    #         response = HttpResponse(content_type='text/csv')
    #         response['Content-Disposition'] = f'attachment; filename="service_orders_{lab_id}.csv"'

    #         writer = csv.writer(response)
    #         writer.writerow(['Lab Name', lab_name])
    #         writer.writerow(['Lab ID', lab_id])
    #         writer.writerow(['User Name', user_name])
    #         writer.writerow(['Phone', phone])
    #         writer.writerow([])
    #         writer.writerow(['Item ID', 'Item Name', 'Item Type', 'Quantity', 'Date', 'Unit of Measurement'])

    #         for item in items:
    #             writer.writerow([item.id, item.item_name, item.item_type, item.quantity, item.date, item.unit_of_issue])

    #         return response

    return redirect('manager_view')

@login_required
def report(request):
    context = {}
    return render(request, 'manager/report.html',context)
