__author__ = 'arkaaito'

from django.forms import ModelForm
from advisor.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['offering', 'withdrawn', 'grade', 'difficulty_rating', 'value_rating',
                  'peak_effort', 'typical_effort', 'comments', 'anonymous']