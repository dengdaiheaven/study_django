from django.http import QueryDict
from django.core.paginator import Paginator
from django.views.generic import View
from restapi.models import UserInfo
from restapi.utils.generate_json import GenResponseJson
import traceback
import datetime


class UserInfoView(View):

    def post(self, request):
        try:
            # 获取变量
            cert_id = request.POST.get("cert_id")
            cert_name = request.POST.get("cert_name")
            cert_no = request.POST.get("cert_no")
            insert_date = datetime.date.today()
            # 创建对象并保存
            user_info = UserInfo()
            user_info.cert_id = cert_id
            user_info.cert_name = cert_name
            user_info.cert_no = cert_no
            user_info.pub_date = insert_date
            user_info.save()
            return GenResponseJson.gen_json("0000", {"cert_id":cert_id, "cert_name":cert_name, "cert_no":cert_no, "insert_date":str(insert_date)})
        except Exception as e:
            print(traceback.format_exc())
            return GenResponseJson.gen_json("1000", msg=e)

    def delete(self, request, cert_id):
        try:
            user = UserInfo.objects.get(cert_id=cert_id)
            cert_name = user.cert_name
            cert_no= user.cert_no
            insert_date = user.pub_date
            user.delete()
            return GenResponseJson.gen_json("0000", {"cert_id":cert_id, "cert_name":cert_name, "cert_no":cert_no, "insert_date":str(insert_date)})
        except Exception as e:
            print(traceback.format_exc())
            return GenResponseJson.gen_json("2000", {"cert_id":cert_id}, msg=e)

    def put(self, request, cert_id):
        try:
            user = UserInfo.objects.get(cert_id=cert_id)
            user.delete()
            put = QueryDict(request.body)
            cert_id_p = put.get("cert_id")
            cert_name = put.get("cert_name")
            cert_no = put.get("cert_no")
            insert_date = datetime.date.today()
            UserInfo.objects.create(cert_id=cert_id_p, cert_name=cert_name, cert_no=cert_no, pub_date=insert_date)
            return GenResponseJson.gen_json("0000", {"cert_id":cert_id_p, "cert_name":cert_name, "cert_no":cert_no, "insert_date":str(insert_date)})
        except Exception as e:
            print(traceback.format_exc())
            return GenResponseJson.gen_json("3000", {"cert_id":cert_id}, msg=e)

    def get(self, request, cert_id):
        try:
            user = UserInfo.objects.get(cert_id=cert_id)
            return GenResponseJson.gen_json("0000", {"cert_id":cert_id, "cert_name":user.cert_name, "cert_no":user.cert_no, "insert_date":str(user.pub_date)})
        except Exception as e:
            print(traceback.format_exc())
            return GenResponseJson.gen_json("4000", {"cert_id":cert_id}, msg=e)


class UserInfoGetView(View):
    
    def get(self, request):
        try:
            # 第pindex页
            pindex = request.GET.get("pindex")
            if pindex == '' or pindex is None:
                pindex = '0'
            pindex = int(pindex) + 1
            users = UserInfo.objects.all().order_by("pub_date")
            p = Paginator(users, 10)
            # 获取所有的页码信息
            plist = p.page_range.stop-1
            # 获取pindex页数据
            users_objs = p.page(pindex)
            users_list = []
            for user in users_objs:
                dict_tmp = {}
                for part in str(user).split(","):
                    dict_tmp[part.split(":")[0]] = part.split(":")[1]
                users_list.append(dict_tmp)
            return GenResponseJson.gen_json("0000", {"pindex":pindex-1, "plist":plist, "users_list":users_list})
        except Exception as e:
            print(traceback.format_exc())
            return GenResponseJson.gen_json("4000", {"pindex":pindex-1, "plist":plist}, msg=e)
