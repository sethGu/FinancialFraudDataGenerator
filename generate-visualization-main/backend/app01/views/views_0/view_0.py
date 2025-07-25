from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
import json
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from app01.models import Login, System_log
from collections import defaultdict
import sys
import os
from django.utils import timezone
from datetime import datetime
import pytz

from django.contrib.auth.hashers import make_password, check_password

# 私钥
private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIBUwIBADANBgkqhkiG9w0BAQEFAASCAT0wggE5AgEAAkEA0vfvyTdGJkdbHkB8
mp0f3FE0GYP3AYPaJF7jUd1M0XxFSE2ceK3k2kw20YvQ09NJKk+OMjWQl9WitG9p
B6tSCQIDAQABAkA2SimBrWC2/wvauBuYqjCFwLvYiRYqZKThUS3MZlebXJiLB+Ue/
gUifAAKIg1avttUZsHBHrop4qfJCwAI0+YRAiEA+W3NK/RaXtnRqmoUUkb59zsZUB
LpvZgQPfj1MhyHDz0CIQDYhsAhPJ3mgS64NbUZmGWuuNKp5coY2GIj/zYDMJp6vQI
gUueLFXv/eZ1ekgz2Oi67MNCk5jeTF2BurZqNLR3MSmUCIFT3Q6uHMtsB9Eha4u7h
S31tj1UWE+D+ADzp59MGnoftAiBeHT7gDMuqeJHPL4b+kC+gzV4FGTfhR9q3tTbkl
ZkD2A==
-----END RSA PRIVATE KEY-----"""

def rsa_decrypt(ciphertext):
    key = RSA.importKey(private_key)
    cipher = PKCS1_v1_5.new(key)
    decrypted_text = cipher.decrypt(base64.b64decode(ciphertext), None)
    return decrypted_text.decode('utf-8')

@require_http_methods(["POST"])
def user_login(request):
    if request.method == 'POST':
        post_body = request.body.decode()
        p = json.loads(post_body)

        username = p.get('username')
        encrypted_password = p.get('password')
        password = rsa_decrypt(encrypted_password)  # 解密传入的密码
        print(username, password)
        try:
            # 获取用户对象
            user = Login.objects.get(username=username)
            print(user.password)
            # 验证密码
            # if (3 > 1):
            if check_password(password, user.password):
                # 记录登录日志
                log_entry = System_log(
                    user=username,
                    change="User login",
                    time=timezone.now(),
                    result="success"
                )
                log_entry.save()  # 保存日志

                # 将用户名存储在会话中
                request.session['username'] = username

                return JsonResponse({
                    "code": 200,
                    "data": {
                        "token": "example-token",
                        "message": "Login successful!",
                        "state": "true"
                    }
                })
            else:
                raise Login.DoesNotExist  # 密码不匹配则视为用户不存在

        except Login.DoesNotExist:
            log_entry = System_log(
                user=username,
                change="User login",
                time=timezone.now(),
                result="failure"
            )
            log_entry.save()  # 保存日志

            return JsonResponse({
                "code": 0,
                "data": {
                    "message": "Incorrect username or password.",
                    "state": "false"
                }
            })

@require_http_methods(["POST"])
def user_update_password(request):
    if request.method == 'POST':
        post_body = request.body.decode()
        p = json.loads(post_body)

        username = request.session.get('username', None)
        encrypted_old_password = p.get('oldPassword')
        old_password = rsa_decrypt(encrypted_old_password)  # 解密旧密码
        new_password = rsa_decrypt(p.get('newPassword'))  # 解密新密码

        try:
            # 获取用户对象
            user = Login.objects.get(username=username)
            # 验证旧密码
            # if (3 > 1):
            if check_password(old_password, user.password):
                # 更新密码，使用make_password进行哈希
                user.password = make_password(new_password)
                user.save()

                # 记录修改密码日志
                log_entry = System_log(
                    user=username,
                    change="User change password",
                    time=timezone.now(),
                    result="success"
                )
                log_entry.save()

                return JsonResponse({
                    "code": 200,
                    "data": {
                        "message": f"{username} Password successfully changed.",
                        "state": "true"
                    }
                })

            else:
                raise Login.DoesNotExist  # 如果旧密码不匹配

        except Login.DoesNotExist:
            log_entry = System_log(
                user=username,
                change="User change password",
                time=timezone.now(),
                result="failure"
            )
            log_entry.save()

            return JsonResponse({
                "code": 200,
                "data": {
                    "message": "Incorrect old password.",
                    "state": "false"
                }
            })




@require_http_methods(["GET"])
def user_info(request):
    return JsonResponse(
        {
            "code": 200,
            "data": {
                "roles": ['admin'],
                "introduction": 'I am a super administrator',
                "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                "name": 'Super Admin'
            }
        }, )


@require_http_methods(["POST"])
def user_logout(request):
    username = request.session.get('username', None)  # 获取会话中的用户名

    if username:
        # 如果用户名存在，则进行登出操作
        # 记录登录日志
        log_entry = System_log(
            user=username,
            change="User logout",  # 操作描述
            time=timezone.now(),  # 当前时间
            result="success"
        )

        log_entry.save()  # 保存日志
        request.session.flush()  # 清除所有会话数据（登出）

        # 返回成功的响应
        return JsonResponse({
            "code": 200,
            "data": {
                "message": f"{username} Successfully logged out.",
                "state": "true"
            }
        })
    else:
        return JsonResponse({
            "code": 400,
            "data": {
                "message": "User not logged in.",
                "state": "false"
            }
        })

@require_http_methods(["POST"])
def log_change(request):
    username = request.session.get('username', None)  # 获取会话中的用户名

    try:
        # 获取请求的 JSON 数据
        data = json.loads(request.body)
        change = data.get('change')
        result = data.get('result')

        if not change:
            return JsonResponse({
                "code": 400,
                "data": {
                    "message": "Missing required parameters (user or change).",
                    "state": "false"
                }
            })

        # 创建日志记录
        log_entry = System_log(
            user=username,
            change=change,
            time=timezone.now(),
            result=result
        )

        log_entry.save()  # 保存日志到数据库

        return JsonResponse({
            "code": 200,
            "data": {
                "message": "Log recorded successfully.",
                "state": "true"
            }
        })

    except Exception as e:
        return JsonResponse({
            "code": 500,
            "data": {
                "message": f"Log recording failed.: {str(e)}",
                "state": "false"
            }
        })