import json

import requests

from apps.my_base import MyBaseTest, domain, MyLoginBaseTest


class AnoymousAccountApi(MyBaseTest):
    """
    匿名非登录接口服务端的基础接口
    """

    def setUp(self):
        self.path = '%s/account' % domain  # 本模块的相对路径

    # def test_create_user(self):
    #     """
    #     用户注册接口测试，用户登录测试
    #     :return:
    #     """
    #     url = self.path + '/create-new-user/'
    #
    #     post_data = dict(
    #         user='test_user',
    #         password='asdf1234',
    #         u_name='xtst-user'
    #     )
    #
    #     res = requests.post(url, data=json.dumps(post_data))
    #
    #     code = res.status_code
    #     self.assertEqual(code, 200, msg='这个服务器home页面要有返回值')

    def test_user_login(self):
        """
        用户注册接口测试，用户登录测试
        :return:
        """
        url = self.path + '/user-login/'

        post_data = dict(
            user='test_user',
            password='asdf1234',
        )

        res = requests.post(url, data=json.dumps(post_data))
        print(res.text)

        res_json = json.loads(res.text)
        self.token = res_json['data']['token']

        code = res.status_code
        self.assertEqual(code, 200, msg='这个服务器home页面要有返回值')

    def test_user_logout(self):
        """
        测试用户登出
        :return: 
        """
        url = self.path + '/user-login/'
        get_data = dict(
            user='test_user',
            password='asdf1234',
        )
        res = requests.post(url, data=json.dumps(get_data))
        res_json = json.loads(res.text)
        token = res_json['data']['token']

        logout_url = self.path + '/user-logout/'

        get_data = dict(
            token=token
        )

        res = requests.get(logout_url, params=get_data)
        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)


class LoginAccountApi(MyLoginBaseTest):
    """
    登录之后的账号的接口
    """

    # todo 后面就大量的写这里面的接口了
    def setUp(self):
        pass
        # self.token = None  # 登录后换取的token

    def test_login_api(self):
        """
        测试登录状态的接口
        :return:
        """
        self.assertFalse(True, msg='只是做个测试init')

    def test_get_user_org(self):
        """
        获取登录用户的组织信息
        :return:
        """
        url = self.path + '/get-auth-user-org/'

        param = {}
        param = self.wrap_param_with_token(param)
        res = requests.get(url, params=param)
        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)

    def test_get_auth_user_all_orgs_info(self):
        """
        获取用户所有的全部组织信息
        :return:
        """

        url = self.path + '/get-auth-user-all-orgs-info/'
        param = {}
        param = self.wrap_param_with_token(param)
        res = requests.get(url, params=param)
        self.assertStatusOk(res)
        self.assertResCodeOk(res.text)
