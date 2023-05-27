from django import forms


from .models import ConversationMessages





class ConversationMessagesForm(forms.Form):
    class Meta:
        model = ConversationMessages
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-32 py-4 px-6 border border-green-500'
            })
        }