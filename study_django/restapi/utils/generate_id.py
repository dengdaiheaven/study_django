#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ProjectName: study_django
# @FileName: generate_id
# @Time: 2020/10/13 9:21
# @Author: chengming
# @Email:972765453@qq.com

import uuid


class GenerateId:

    @staticmethod
    def gen_id(input_s: str) ->str:
        return uuid.uuid3(uuid.NAMESPACE_DNS, input_s).hex

if __name__ == '__main__':
    print(GenerateId.gen_id("小明"+"1234")) # 859c44dec8613c5b8f7e5d7491dff33f
    print(GenerateId.gen_id("小李 + 1234")) # 19d5d59a4b6d39ed81028804c6d07acc
    print(GenerateId.gen_id("小赵 + 5678")) # 0f5a70f9e2fa3ec0a4831343a54f96e8