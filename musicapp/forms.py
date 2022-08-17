
from django import forms
from musicapp.models import Blog, Comment

class BlogUpdate(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class BlogForm(forms.Form):
    #내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__' #Blog 클래스 안에 있는 모든 객체 대상
        #fields = ['title', 'body'] #특정 데이터 대상