from django.shortcuts import render, redirect
from .models import user_data

# JWT 토큰관련
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        
    elif request.method == 'POST':
        # DB 조회방법(https://ssungkang.tistory.com/entry/Django-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%A1%B0%ED%9A%8C-queryset)
        if user_data.objects.filter(id = request.POST.get('user_id', None)).exists():
            user = user_data.objects.filter(id = request.POST.get('user_id', None)).values('id', 'pw')            
            if user[0].get('pw') == request.POST['user_pw']:
                try:
                    print("@@@@@@@@@@토큰발행@@@@@@@@@@")
                    print("발행할 ID: ", user[0].get('id'), ", 타입=", type(user[0].get('id')), "\n발행할 PW: ", user[0].get('pw'), ", 타입=", type(user[0].get('pw')))
                    user_token_data = authenticate(username=user[0].get('id'), password=user[0].get('pw'))
                    print("계정: ", user_token_data)
                    
                    payload = JWT_PAYLOAD_HANDLER(user_token_data)
                    jwt_token = JWT_ENCODE_HANDLER(payload)
                    update_last_login(None, user_token_data)
                
                except DoesNotExist:
                    raise serializers.ValidationError(
                        'User with given username and password does not exist'
                        )
                
                print("token: ", jwt_token)
                return redirect('/member') # 회원목록 List로 변경

            else:
                print("###비밀번호 불일치###")
                return redirect('/member')

        else:
            print('일치하는 아이디가 없습니다.\n회원가입페이지로 이동합니다.')
            return redirect('/member/register')

        return('/') # 안돌아가는 return

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        id      = request.POST.get('user_id', None)
        pw      = request.POST['user_pw']
        name    = request.POST.get('user_name', None)

        res_data = {}
        if not (id and name):
            res_data['error'] = '모든 값을 입력해주세요.'
        else:
            user = user_data(
                id = id,
                pw = pw,
                name = name,
            )
            user.save()
            print('#####회원가입#####\nid: ', user.id, '\npw: ', user.pw, '\nname: ', user.name)
    
    return redirect('/member')