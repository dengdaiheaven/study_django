#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ProjectName: study_django
# @FileName: test_rest
# @Time: 2020/10/13 16:51
# @Author: chengming
# @Email:972765453@qq.com


import requests


class restTest:

    @staticmethod
    def post_1():
        res = requests.post('http://127.0.0.1:8000/users', data={'cert_id': '859c44dec8613c5b8f7e5d7491dff33f', 'cert_no': '1234', 'cert_name':'小明'})
        print(res.text)

    @staticmethod
    def post_3():
        res = requests.post('http://127.0.0.1:8000/users',
                            data={'cert_id': '0f5a70f9e2fa3ec0a4831343a54f96e8', 'cert_no': '5678', 'cert_name': '小赵'})
        print(res.text)

    @staticmethod
    def get_1():
        res = requests.get('http://127.0.0.1:8000/users/id/859c44dec8613c5b8f7e5d7491dff33f')
        print(res.text)

    @staticmethod
    def get_2():
        res = requests.get('http://127.0.0.1:8000/users/id/19d5d59a4b6d39ed81028804c6d07acc')
        print(res.text)

    @staticmethod
    def get_3():
        res = requests.get('http://127.0.0.1:8000/users/id/0f5a70f9e2fa3ec0a4831343a54f96e8')
        print(res.text)

    @staticmethod
    def get_all():
        res = requests.get('http://127.0.0.1:8000/users/pages')
        print(res.text)

    @staticmethod
    def get_all_page():
        res = requests.get('http://127.0.0.1:8000/users/pages', params={"pindex":"1"})
        print(res.text)

    @staticmethod
    def put2():
        res = requests.put('http://127.0.0.1:8000/users/id/859c44dec8613c5b8f7e5d7491dff33f', data={'cert_id': '19d5d59a4b6d39ed81028804c6d07acc', 'cert_no': '1234', 'cert_name':'小李'})
        print(res.text)

    @staticmethod
    def delete_1():
        res = requests.delete('http://127.0.0.1:8000/users/id/859c44dec8613c5b8f7e5d7491dff33f')
        print(res.text)

    @staticmethod
    def delete_2():
        res = requests.delete('http://127.0.0.1:8000/users/id/19d5d59a4b6d39ed81028804c6d07acc')
        print(res.text)

    @staticmethod
    def delete_3():
        res = requests.delete('http://127.0.0.1:8000/users/id/0f5a70f9e2fa3ec0a4831343a54f96e8')
        print(res.text)

if __name__ == '__main__':
    #restTest.post_1() #85
    #restTest.put2() #19
    #restTest.post_3() #0f

    restTest.get_all()
    restTest.get_all_page()

    #restTest.get_1()
    #restTest.get_2()
    #restTest.get_3()

    #restTest.delete_1()
    #restTest.delete_2()
    #restTest.delete_3()
