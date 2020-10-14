from django.test import TestCase
from restapi.models import UserInfo
from restapi.utils.generate_id import GenerateId
import datetime
import requests


class ModelTests(TestCase):
    def setUp(self) -> None:
        userinfo = UserInfo()
        name = "xiaoming"
        no = "123"
        userinfo.cert_name = name
        userinfo.cert_no = no
        userinfo.cert_id = GenerateId.gen_id(name + no)
        userinfo.pub_date = datetime.date.today()
        userinfo.save()
        # UserInfo.objects.create(cert_id="111", cert_no="1234", cert_name="xiaoming", pub_data=datetime.date.today())
