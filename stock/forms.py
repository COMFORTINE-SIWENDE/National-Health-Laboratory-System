from django import forms
from stock.models import Products,Transaction,Order

class SearchItemsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['category', 'item_name']
class ProductCreateForm(forms.ModelForm):
    class Meta:
      model = Products
      fields = ['category','item_name','unit_of_issue','quantity']

class StockSearchForm(forms.ModelForm):
   export_to_CSV = forms.BooleanField(required=False)
   class Meta:
      model = Products
      fields = ['category','item_name']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['category','item_name','quantity','unit_of_issue']

class ViewReports(forms.Form):
    pass