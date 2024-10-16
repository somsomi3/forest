from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    
     class Meta(UserCreationForm.Meta):
        model = get_user_model()




class CustomUserChangeForm(UserChangeForm):
    #password 부분도 출력하고 싶지 않다면,
    # password = None


    class Meta(UserChangeForm.Meta):
        model =  get_user_model()

        #이하 추가
        fields = ('first_name', 'last_name') 