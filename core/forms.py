from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    
    email = forms.EmailField(label='E-mail', max_length=100)
    
    def send_mail(self):
        
        email = self.cleaned_data['email']
        
        conteudo = f'Email: {email}\n'
        
        mail = EmailMessage(
            from_email='bilu@gmail.com.br',
            to=['bilu@gmail.com.br',],
            headers={'Reply-To':email}
        )
        mail.send()   