from django import forms

from blog.models import BlogPost 


class CreateBlogPostForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ['title', 'body', 'image']
	
	def clean_title(self, *args,**kwargs):
		title = self.cleaned_data["title"]
		if 'CFE' in title:
			raise forms.ValidationError("not valid")
		return title


class UpdateBlogPostForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ['title','body', 'image']


	def save(self,commit=True):
		blog_post = self.instance
		blog_post.title = self.cleaned_data['title']
		blog_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			blog_post.image = self.cleaned_data['image']
		
		if commit:
			blog_post.save()
		return blog_post