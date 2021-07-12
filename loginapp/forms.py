from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


"""
My Notes: contrib.auth.models>
1.  To get more of Users we are going to use in built features of django
    first of all we will import USER model from contrib.auth as mentioned abvove

2.  Now import UserCreationForm as well 
3.  Create class form and inherit from UserCreationForm
4. Use model as User which is inbuilt, you can either call '__all__' or you can mention which fields you need.
Both are mentioned for you, but one is inactive

5. Changed the name of signupform to SignForm, it will let me keep the builtin form in views.
"""

class SignForm(UserCreationForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}