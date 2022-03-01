from django import forms

from utilities_and_rent.models import RentPayment, UnitRentDetails

class DateInput(forms.DateInput):
    input_type = 'date'
    
class AddRentDetailsForm(forms.ModelForm):
    class Meta:
        model = UnitRentDetails
        fields = ['rent_amount','currency','amount_paid','pay_for_month','start_date',
                  'end_date','due_date','notify_tenant']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'due_date': DateInput(),
        }

class SubmitPaymentsForm(forms.ModelForm):
    class Meta:
        model = RentPayment
        fields = ['payment_code', 'amount', 'payment_method', 'paid_on']   
        widgets = {
            'paid_on': DateInput(),
        } 
        
class UpdateRentDetails(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateRentDetails, self).__init__(*args, **kwargs)
        self.fields['currency'].disabled = True
        self.fields['rent_amount'].disabled = True
        self.fields['amount_paid'].disabled = True
        self.fields['pay_for_month'].disabled = True
        self.fields['paid_in_advance'].disabled = True
        self.fields['amount_paid_in_advance'].disabled = True
        self.fields['cleared'].disabled = True
        self.fields['start_date'].disabled = True
        self.fields['end_date'].disabled = True
        self.fields['added'].disabled = True
    class Meta:
        model = UnitRentDetails
        fields = ['currency','rent_amount','amount_paid','pay_for_month','paid_in_advance','amount_paid_in_advance',
                  'cleared','start_date','end_date','added','due_date','status','notify_tenant']
        widgets = {
            'due_date': DateInput(),
        }
        
class PaymentUpdateForm(forms.ModelForm):
    class Meta:
        model = RentPayment
        fields = ['status','reason','notify_tenant']