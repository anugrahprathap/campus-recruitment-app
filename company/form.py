
from django import forms
# from django.contrib.auth import authenticate
# from django.contrib.auth import get_user_model
# from django.contrib import auth
from phonenumber_field.modelfields import PhoneNumberField
from .models import *
from .models import company
from django.contrib.auth.models import User

class regform(forms.Form):
    name = forms.CharField()
    comp_name = forms.CharField()
    location = forms.CharField()
    description = forms.CharField()
    email = forms.EmailField()
    Phone = forms.CharField(widget=forms.NumberInput)
    
    url = forms.URLField()
    linkedin = forms.URLField()
    Password = forms.CharField(widget=forms.PasswordInput)
    CPassword = forms.CharField(widget=forms.PasswordInput)
    
    
    
    def __init__(self, *args, **kwargs):
        # forms.ModelForm.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)
        
        self.fields["name"].label = "Name :"
        self.fields['comp_name'].label = "Company Name :"
        self.fields['location'].label = "Company Location :"
        self.fields['description'].label = "Job Description :"
        self.fields['email'].label = "Email Id :"
        self.fields['Phone'].label = "Phone Number :"
        self.fields['linkedin'].label = "Linkedin :"
        self.fields['url'].label = "Website :"
        self.fields['Password'].label = "Password :"
        self.fields['CPassword'].label = "Confirm Password :"
        
        
        
        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Your Name',
            }
        )        
        self.fields['comp_name'].widget.attrs.update(
            {
                'placeholder': 'Company Name',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : Bangalore,India',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Mail Id' ,
            }
        )                        
        self.fields['description'].widget.attrs.update(
            {
                'placeholder': 'Job Description ',
            }
        )        
        
        self.fields['Phone'].widget.attrs.update(
            {
                'placeholder': 'Phone Number  ',
            }
        )         
       
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )  
        self.fields['linkedin'].widget.attrs.update(
            {
                'placeholder': 'https://www.linkedin.com/in/username-',
            }
        ) 
        self.fields['Password'].widget.attrs.update(
            {
                'placeholder': 'Password ',
                'type': 'password',
            }
        )   
        self.fields['CPassword'].widget.attrs.update(
            {
                'placeholder': 'Re Enter Password ',
                'type': 'password',
            }
        )  
  
    
    def clean_job_type(self):
        name = self.cleaned_data.get("name")

        if not name:
            raise forms.ValidationError("Required")
        return name

    def clean_category(self):
        description = self.cleaned_data.get('description')

        if not description:
            raise forms.ValidationError("description is required")
        return description
    def clean_category(self):
        mobile = self.cleaned_data.get('mobile')

        if not mobile:
            raise forms.ValidationError("mobile no is required")
        return mobile
    def clean_category(self):
        mail = self.cleaned_data.get('mobile')

        if not mail:
            raise forms.ValidationError("mail id is required")
        return mail
    def clean_category(self):
        linkedin = self.cleaned_data.get('linkedin')

        if not linkedin:
            raise forms.ValidationError("linkedin id is required")
        return linkedin
    def clean_category(self):
        url = self.cleaned_data.get('linkedin')

        if not url:
            raise forms.ValidationError("url is required")
        return url

    def clean_category(self):
        Password = self.cleaned_data.get('Password')

        if not Password:
            raise forms.ValidationError("Password is required")
        return Password
    def clean_category(self):
        CPassword = self.cleaned_data.get('CPassword')

        if not CPassword:
            raise forms.ValidationError("Password is required")
        return CPassword
    def clean(self):
        cleaned_data = super(regform, self).clean()
        password = cleaned_data.get("Password")
        confirm_password = cleaned_data.get("CPassword")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        return cleaned_data