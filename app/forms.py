from django import forms

class MatrimonyForm(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'enter your name'}))
    gender=forms.CharField(max_length=100)
    dob=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    age=forms.IntegerField()
    religion=forms.CharField(max_length=100)
    job=forms.CharField(max_length=100)
    salary=forms.IntegerField()
    phone=forms.IntegerField()
    def clean(self):
        super().clean()
        age=self.cleaned_data['age']
        if age<18:
            raise forms.ValidationError("Age should be 18 or above")
        dob=self.cleaned_data['dob']
        year=str(dob)[:4]
        if int(year) != (2025-age):
            raise forms.ValidationError("Age and Dob dont match")
    def clean_name(self):
        super().clean()

        nameval=self.cleaned_data['name']
        if len(nameval)<5:
            raise forms.ValidationError("Name should be at least 5 characters long")
        return nameval
    def clean_number(self):
        super().clean()
        numval=self.cleaned_data['phone']
        if str(numval)!=10:
            raise forms.ValidationError("Number should be 10 digits")
    
        

        
