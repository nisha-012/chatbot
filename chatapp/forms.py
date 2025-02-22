from django import forms
from .models import UserQuery

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = UserQuery
        fields = ["name", "email", "department", "question"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-control"}),
            "question": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
