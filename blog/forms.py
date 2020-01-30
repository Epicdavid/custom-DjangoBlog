from django import forms
from blog.models import Post,MyComment
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text','image')
        
        labels = {
            'text': _(''),
            'image': _('Post Image')
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control mw-90'}),
            'author':forms.TextInput(attrs={"size":"input-field col s6"})
        }
class MyCommentForm(forms.ModelForm):

    class Meta():
        model = MyComment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':''}),
            'text':forms.Textarea(attrs={'class':'form-control mw-10'})
        }
