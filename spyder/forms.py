from django import forms

from .models import Sitemap


class SitemapForm(forms.ModelForm):
    class Meta:
        model = Sitemap
        fields = ("address")
