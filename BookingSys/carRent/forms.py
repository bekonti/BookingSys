from django.forms import ModelForm
from .models import *
from PIL import Image
import datetime


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'surname', 'tel', 'email', 'start_rent', 'end_rent']

    def save(self, commit=True):
        payment = super(PaymentForm, self).save(commit = False)
        payment.name = self.cleaned_data['name']
        payment.surname = self.cleaned_data['surname']
        payment.tel = self.cleaned_data['tel']
        payment.email = self.cleaned_data['email']
        payment.start_rent = self.cleaned_data['start_rent']
        payment.end_rent = self.cleaned_data['end_rent']

        if commit:
            payment.save()

        return payment