from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ["title", "description"]
        widgets = {
            'description': forms.Textarea(attrs={'cols': "100%", 'rows': 5}),
            'title': forms.TextInput(attrs={"cols": "100%"})
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["description"].widget.attrs.update({'type': 'textarea;'})