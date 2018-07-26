from .models import Image

class NewImageForm(forms.ModelForm):
    class Meta:
         model = Image
         exclude = ['profile', 'pub_date']
         
