from django.shortcuts import render, redirect
from .models import user_data

# JWT 토큰관련
from datetime import datetime, timedelta
import jwt

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        
    elif request.method == 'POST':
        if user_data.objects.filter(id = request.POST.get('user_id', None)).exists():
            now = datetime.now()
            user = user_data.objects.filter(id = request.POST.get('user_id', None)).values('id', 'pw')
            encoded = jwt.encode({
                                'id': user[0].get('id'),
                                'time': now.strftime('%Y-%m-%d %H:%M:%S'),
                                'exp': datetime.utcnow() + timedelta(minutes=3) # 세션유지시간 3분
                            }, 'secret', algorithm='HS256')
            print("코드: ", encoded)
            print(jwt.decode(encoded, 'secret', algorithm=['HS256']))

        return redirect('/member')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        id      = request.POST.get('user_id', None)
        pw      = request.POST['user_pw']
        name    = request.POST.get('user_name', None)

        res_data = {}
        if not (id or pw or name):
            res_data['error'] = '모든 값을 입력해주세요.'

            return redirect('/member/register/')
        else:
            user = user_data(
                id = id,
                pw = pw,
                name = name,
            )
            user.save()
            print('#####회원가입#####\nid: ', user.id, '\npw: ', user.pw, '\nname: ', user.name)
    
    return redirect('/member')