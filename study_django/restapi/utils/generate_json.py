#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ProjectName: study_django
# @FileName: generate_json
# @Time: 2020/10/13 14:03
# @Author: chengming
# @Email:972765453@qq.com
# from django.shortcuts import render # 返回html
# from django.shortcuts import redirect # 重定向
from django.shortcuts import HttpResponse # 返回json数据
import json


class GenResponseJson:

    @staticmethod
    def gen_json(code=None, data=None, msg=None):
        if isinstance(msg, Exception):
             error_bytes = bytes(str(msg), encoding='utf-8')
             msg = str(error_bytes, encoding='utf-8')
        return_value = {"code": code, "data":data, "msg":msg}
        return HttpResponse(json.dumps(return_value, ensure_ascii=False), content_type="application/json;charset:'utf-8'")
