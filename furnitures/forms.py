from django import forms
from .models import Furniture, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Support

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'support'))


class FurnitureForm(forms.ModelForm):

    class Meta:
        model = Furniture
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.friendly_name) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
