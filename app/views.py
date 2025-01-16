from django.shortcuts import render, redirect
from .forms import BillForm
from .models import Bill

def billing_page(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save() # Save the bill
            return redirect('billing_success')  # Redirect to a success page
    else:
        form = BillForm()
    return render(request, 'app/billing.html', {'form': form})

def billing_success(request):
    bills = Bill.objects.all()
    return render(request, 'app/success.html', {'bills': bills})

