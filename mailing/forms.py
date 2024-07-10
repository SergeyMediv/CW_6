from django import forms

from mailing.models import Client, Mailing, Message

forbidden_words = ['казино',
                   'криптовалюта',
                   'крипта',
                   'биржа',
                   'дешево',
                   'бесплатно',
                   'обман',
                   'полиция',
                   'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ('owner',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)

    def clean_theme(self):
        cleaned_data = self.cleaned_data['theme']
        for word in forbidden_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Название не должно содержать запрещённых слов')
            else:
                return cleaned_data

    def clean_text(self):
        cleaned_data = self.cleaned_data['text']
        if cleaned_data.lower() in forbidden_words:
            raise forms.ValidationError('Описание не должно содержать запрещённых слов')
        return cleaned_data
