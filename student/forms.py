
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from phonenumber_field.modelfields import PhoneNumberField


class UserRegForm(UserCreationForm):
    
    COURSES= [
        ("MCA", "MCA"), ("MSc", "MSC CS"),
        ("Msc1", "MSc  CS Int."),
        ("MTech", "MTech CS"),
    ]

    email = forms.EmailField(max_length=300)
    Full_Name = forms.CharField(max_length=100)
    
    course =forms.ChoiceField(choices=COURSES)
    cgpa = forms.IntegerField(max_value=10)
    resume = forms.FileField()
    mobile = forms.CharField(widget=forms.NumberInput)
    class Meta:
        model = User
        fields =['username','password1','password2']
    def __init__(self, *args, **kwargs):
        # forms.ModelForm.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)
        
        self.fields["username"].label = "Regster No :"
        self.fields['password1'].label = "Password :"
        self.fields['password2'].label = "Confirm Password :"
        # self.fields["course"].label = "Course :"