from django.contrib import admin
from django.urls import path, include

# JWT 토큰관련
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('member/', include('prac_jwt.urls')),

    # # JWT 토큰
    # path('api-token-auth/', obtain_jwt_token), # 발생
    # path('api-token-refresh/', refresh_jwt_token), # 갱신
    # path('api-token-verify/', verify_jwt_token), # 조회
]
