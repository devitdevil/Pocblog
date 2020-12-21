from django import forms
from .models import Post,Category
choices=Category.objects.all().values_list('name','name')
choice_list= []
for item in choices:
    choice_list.append(item)
    print(choice_list)
class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields = ('title','title_tag','author','category','body')

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'This is the title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'This is the title tag'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Share your views'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','title_tag','body')

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'This is the title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'This is the title tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Share your views'}),

        }