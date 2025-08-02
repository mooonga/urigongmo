# contest/forms.py

from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['contest', 'category_id', 'status', 'submission_file']
    
    def clean_submission_file(self):
        file = self.cleaned_data.get('submission_file', False)
        if file:
            ext = file.name.split('.')[-1].lower()
            if ext not in ['pdf', 'jpg', 'jpeg', 'docx']:
                raise forms.ValidationError("허용되지 않은 파일 형식입니다.")
        return file