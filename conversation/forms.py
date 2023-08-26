from django import forms

from .models import ConversationalMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationalMessage
        fields = {'content',}
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }