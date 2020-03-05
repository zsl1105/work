# models.py
from django.db import models


class park_prize(models.Model):
    area = models.CharField(max_length=200)
    big_detail = models.CharField(max_length=200)
    company_member = models.CharField(max_length=200)
    typee = models.CharField(max_length=200)
    detail_type = models.CharField(max_length=200)
    prize = models.CharField(max_length=200)
    prize_money = models.CharField(max_length=200)
    prize_attach = models.CharField(max_length=200)
    prize_require = models.CharField(max_length=200)


class park_prize_result(models.Model):
    area = models.CharField(max_length=200)
    big_detail = models.CharField(max_length=200)
    company_member = models.CharField(max_length=200)
    typee = models.CharField(max_length=200)
    detail_type = models.CharField(max_length=200)
    prize = models.CharField(max_length=200)
    prize_money = models.CharField(max_length=200)
    prize_attach = models.CharField(max_length=200)
    prize_require = models.CharField(max_length=200)


class park_company_result(models.Model):
    company_name = models.CharField(max_length=55)
    company_member = models.CharField(max_length=55)
    company_area = models.CharField(max_length=55)
    # 1类自主研发
    independent_1 = models.CharField(max_length=55)
    # 1类受赠、受赠或并购
    donate_1 = models.CharField(max_length=55)
    # 1类与主要产品（服务）关联的有（）项
    relation_1 = models.CharField(max_length=55)
    # 2类自主研发
    independent_2 = models.CharField(max_length=55)
    # 2类受赠、受赠或并购
    donate_2 = models.CharField(max_length=55)
    # 2类与主要产品（服务）关联的有（）项
    relation_2 = models.CharField(max_length=55)
    # 企业是否参与编制国家标准、行业标准、检测方法、技术规范
    standard = models.CharField(max_length=55)
    # 企业科技成果转化数量（）项
    conversion = models.CharField(max_length=55)
    # 企业是否制定了研究开发的组织管理制度，建立了研发投入核算体系，编制了研发费用辅助账？
    system = models.CharField(max_length=55)
    # 企业是否建立了科技人员的培养进修、职工技能培训、优秀人才引进，以及人才绩效评价奖励制度
    culture = models.CharField(max_length=55)
    # 企业是否签订产学研合作协议
    industry = models.CharField(max_length=55)
    # 企业是否建立开放式的创新创业平台
    innovation = models.CharField(max_length=55)
    # 近一年企业高新技术产品（服务）收入占企业同期总收入的比例是否不低于60%
    proportion = models.CharField(max_length=55)
    # 企业近三个会计年度研发费用投入总额占同期销售收入总额的比例。
    development = models.CharField(max_length=55)
    # 近三年销售收入
    sales_1 = models.CharField(max_length=55)
    sales_2 = models.CharField(max_length=55)
    sales_3 = models.CharField(max_length=55)
    # 近三年净资产
    assets_1 = models.CharField(max_length=55)
    assets_2 = models.CharField(max_length=55)
    assets_3 = models.CharField(max_length=55)

