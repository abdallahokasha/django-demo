from django import forms


from .models import Landmark


class LandmarkForm(forms.ModelForm):
    class Meta:
        model = Landmark
        fields = [
            "title",
            "description",
            "country",
            "latitude",
            "longitude",
        ]