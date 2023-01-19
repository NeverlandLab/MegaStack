from datetime import timedelta

SIMPLE_JWT = {
    # token有效时长
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=120),
    # token刷新后的有效时间
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # 设置前缀
    "AUTH_HEADER_TYPES": ("JWT",),
    "ROTATE_REFRESH_TOKENS": True,
}
