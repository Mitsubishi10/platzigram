"""Post forms."""

#Django
from django import forms

#Models 
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post model Form"""
    class Meta:
        """Form setting"""

        model = Post
        fields  = ('user','profile','title','photo')