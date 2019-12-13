# # -*- coding: utf-8 -*-


from fake_useragent import UserAgent


class UserAgentMiddleware(object):
    def __init__(self, user_agent=''):
        self.ua = UserAgent(verify_ssl=False)

    def process_request(self, request, spider):
        # print('===UserAgentMiddleware process_request==')
        if self.ua:
            # 显示当前使用的useragent
            # print("********Current UserAgent:%s************")
            custom_ua = self.ua.random
            # print('custom_ua:',custom_ua)
            request.headers.setdefault(b'User-Agent', custom_ua)



