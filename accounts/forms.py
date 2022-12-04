from django import forms
from .models import User, UserProfile
from accounts.validators import allow_only_images_validator
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self): # inbuilt overriding method tto raise custom valdiation error
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number']

class UserProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'start typing....', 'required':'required'}))
    profile_picture = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    cover_photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'cover_photo', 'address', 'country', 'state', 'city','pin_code', 'longitutde', 'latitude']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'latitude' or field == 'longitutde':
                self.fields[field].widget.attrs['readonly']='readonly'
                
    # longitutde = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # latitude = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'})) #TODO 1st way to readonly