from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
    title = forms.CharField()
    email = forms.EmailField()
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=(
        ('blog', 'ブログについて'),
        ('jobs', '仕事の依頼について'),
        ('interview', '取材について'),
        ('ads', '広告掲載について'),
        ('other', 'その他について'),
    ))
    message = forms.CharField(widget=forms.Textarea)

    # メール送信処理
    def send_email(self):
        subject = self.cleaned_data['title']
        from_email = self.cleaned_data['email']
        choices = self.cleaned_data['choice']
        contents = self.cleaned_data['message']
        message = '目的:\n' + str(choices) + '\n\n内容:\n' + contents + '\n\n返信先:\n' + from_email
        to = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to)
