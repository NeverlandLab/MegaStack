REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 允许未经身份认证的用户对API进行只读
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',

        # 只有经过身份认证确定用户身份才能访问
        "rest_framework.permissions.IsAuthenticated",

        # is_staff=True才能访问 —— 管理员(员工)权限
        # 'rest_framework.permissions.IsAdminUser',

        # 允许所有
        # 'rest_framework.permissions.AllowAny',

        # 有身份 或者 只读访问(self.list,self.retrieve)
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
