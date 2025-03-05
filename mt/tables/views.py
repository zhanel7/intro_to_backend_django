from django.shortcuts import render, get_object_or_404, redirect
from .models import Table
from .forms import TableForm

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'tables/tables_list.html', {'tables': tables})

def table_detail(request, pk):
    table = get_object_or_404(Table, pk=pk)
    return render(request, 'tables/table_detail.html', {'table': table})

def table_create(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table-list')
    else:
        form = TableForm()
    return render(request, 'tables/table_form.html', {'form': form})

def table_update(request, pk):
    table = get_object_or_404(Table, pk=pk)
    if request.method == "POST":
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('table-list')
    else:
        form = TableForm(instance=table)
    return render(request, 'tables/table_form.html', {'form': form})

def table_delete(request, pk):
    table = get_object_or_404(Table, pk=pk)
    if request.method == "POST":
        table.delete()
        return redirect('table-list')
    return render(request, 'tables/table_confirm_delete.html', {'table': table})
