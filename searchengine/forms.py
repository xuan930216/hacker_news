# declare a form
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class NewsSearchForm(forms.Form):
    stories_title = forms.CharField(label='Story Title', max_length=100)
    stories_text = forms.CharField(label="Story Text", max_length=200)
    date = forms.DateField(label="Date", required = False)

    #validate form
    def clean_date(self):
        data = self.cleaned_data['date']#optional field
        if data:
            #check data is not in future
            if data > datetime.date.today():
                raise ValidationError(_('Invalid date - date in future'))
        else:
            self.cleaned_data['date']= ''

        return data
        