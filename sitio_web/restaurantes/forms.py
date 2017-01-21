"""
Created at 20/1/17
__author__ = 'Sergio Padilla'
"""
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from django.forms import IntegerField, CharField, ChoiceField


class AddForm(forms.Form):
    id = IntegerField()
    cuisine = CharField(max_length=100, required=False)
    borough = ChoiceField(
        choices=(
            ('Manhattan', "Manhattan"),
            ('Brooklyn', "Brooklyn"),
            ('Queens', "Queens"),
            ('Staten Island', "Staten Island"),
            ('Bronx', "Bronx")
        ),
        widget=forms.RadioSelect,
        initial='Manhattan',
    )
    name = CharField(max_length=100)
    postal_code = IntegerField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-4'
    helper.field_class = 'col-lg-4'
    helper.layout = Layout(
        Field('id', css_class='input-small'),
        Field('cuisine', css_class='input-large'),
        'borough',
        Field('name', css_class='input-large'),
        Field('postal_code', css_class='input-small'),
        FormActions(
            Submit('save_changes', 'Add restaurant', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )

    def clean(self):
        self.is_valid()
        borough = self.cleaned_data.get('borough')
        code = self.cleaned_data.get('postal_code')

        if (borough == 'Manhattan' and 10000 < code < 10044) or (borough == 'Brooklyn' and 11200 < code < 11239) or \
                (borough == 'Queens' and 11690 < code < 11107) or (borough == 'Staten Island' and 10000 < code < 10044)\
                or (borough == 'Bronx' and 10450 < code < 10475):
            return self.cleaned_data

        raise forms.ValidationError('The postal code doesn\'t correspond with the borough')
