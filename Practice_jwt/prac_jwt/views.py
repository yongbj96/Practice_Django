from django.shortcuts import render, redirect
from .models import user_data

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        id      = request.POST.get('user_id', None)
        pw      = request.POST['user_pw']

        user = user_data(
            id = id,
            pw = pw
        )

        print('#####로그인#####\nid: ', user.id, '\npw: ', user.pw)

        return redirect('/prac_jwt')

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
    
    return redirect('/prac_jwt')