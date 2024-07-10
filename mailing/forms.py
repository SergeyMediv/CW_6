from django import forms

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
