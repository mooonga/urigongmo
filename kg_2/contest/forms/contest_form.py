from django import forms
from contest.models import Contest 

#1. 시작일이 마감일보다 늦을 수 없게 하기
class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = [
            'title', 'agency', 'category', 'description',
            'start_date', 'end_date', 'weight_idea', 'weight_creativity',
            'weight_feasibility', 'weight_completion'
        ]

#2. 가중치 합이 1.0(100%)이 아니면 오류
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("시작일은 마감일보다 이전이어야 합니다.")

        total_weight = (
            cleaned_data.get('weight_idea', 0) +
            cleaned_data.get('weight_creativity', 0) +
            cleaned_data.get('weight_feasibility', 0) +
            cleaned_data.get('weight_completion', 0)
        )
        if abs(total_weight - 1.0) > 0.01:
            raise forms.ValidationError("가중치의 총합은 1.0이 되어야 합니다.")

        return cleaned_data