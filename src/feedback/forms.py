from django import forms

from .models import FeedBack

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = [
            "fullname",
            "contactNo",
            "emailAddr",
            "type",
            "message",
        ]
# def __init__(self, *args, **kwargs):
#     super(FeedBackForm, self).__init__(*args, **kwargs)
#     self.fields['fullname'].label = "Your name please:"
