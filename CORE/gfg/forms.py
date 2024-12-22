from django import forms

from .models import GeeksModel

# create a form
class GeeksForm(forms.ModelForm):

    # create meta class
    class Meta:

        # specify models to be used
        model = GeeksModel

        # Specify fields to be used
        fields = '__all__'