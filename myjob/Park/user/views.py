from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from . import models


def park_base(request):
    if request.method == 'GET':
        response2 = models.park_prize.objects.filter(area="南京市政策（企业）").order_by("id")
        return render(request, 'base.html', {"response2": response2, "area": "南京市政策（企业）"})


def park_base_result_yuhua(request):
    if request.method == 'GET':
        response2 = models.park_prize.objects.filter(area="雨花区政策（企业）").order_by("id")
        return render(request, 'base.html', {"response2": response2, "area": "雨花区政策（企业）"})


def park_base_result_pukou(request):
    if request.method == 'GET':
        response2 = models.park_prize.objects.filter(area="浦口区（企业）").order_by("id")
        return render(request, 'base.html', {"response2": response2, "area": "浦口区（企业）"})


def park_base_result_gulou(request):
    if request.method == 'GET':
        response2 = models.park_prize.objects.filter(area="鼓楼区政策").order_by("id")
        return render(request, 'base.html', {"response2": response2, "area": "鼓楼区政策"})


def park_result(request):
    if request.method == 'GET':
        response1 = models.park_prize_result.objects.all()
        return render(request, 'result.html', {"response1": response1})
    if request.method == 'POST':
        id_list = request.POST.getlist("option")
        response1 = models.park_prize.objects.filter(pk__in=id_list).order_by("id")
        # 添加数据到park_prize_result库
        for response in response1:
            id = response.id
            area = response.area
            detail_type = response.detail_type
            prize = response.prize
            prize_money = response.prize_money
            prize_attach = response.prize_attach
            prize_require = response.prize_require
            result1 = models.park_prize_result(id=id, area=area, detail_type=detail_type, prize=prize,
                                               prize_money=prize_money, prize_attach=prize_attach,
                                               prize_require=prize_require)
            result1.save()
        response2 = models.park_prize_result.objects.all()
        return render(request, 'result.html', {"response1": response2})


# 删除部分
def result_del(request, a_id):
    article = models.park_prize_result.objects.get(pk=a_id)
    article.delete()
    return redirect('user:park_result')


# 删除全部
def result_del_all(request):
    article = models.park_prize_result.objects.all()
    article.delete()
    return redirect('user:park_base')


# 计算
def result_sum(request):
    if request.method == "GET":
        articles = models.park_prize_result.objects.all()
        prizes = 0
        prizes_id_list = []
        for article in articles:
            prize = article.prize_money
            try:
                prizes = prizes + float(prize)
            except:
                id = article.id
                prizes_id_list.append(id)
        prize_money_list = models.park_prize_result.objects.filter(pk__in=prizes_id_list).order_by("id")
        return render(request, 'result_sum.html', {"prize_money_list": prize_money_list, "prizes": str(prizes)})

    if request.method == "POST":
        area = request.POST.get("result").split("&")[0].split(",")
        company_member = request.POST.get("result").split("&")[1]
        company_area = request.POST.get("result").split("&")[2]
        result = models.park_prize.objects.filter(area__in=area).filter(
            company_member__in=[company_member, ""]).filter(typee__in=[company_area, ""]).order_by("id")
        prizes = 0
        prizes_id_list = []
        for article in result:
            prize = article.prize_money
            try:
                prizes = prizes + float(prize)
                id = article.id
                prizes_id_list.append(id)
            except:
                id = article.id
                prizes_id_list.append(id)
        prize_money_list = models.park_prize.objects.filter(pk__in=prizes_id_list).order_by("id")
        return render(request, 'result_sum.html', {"prize_money_list": prize_money_list, "prizes": str(prizes),
                                                   "result_last_area": "落地选择：" + area[0],
                                                   "yuhua_result": '{},{}&{}&{}'.format("雨花区政策（企业）", "南京市政策（企业）",
                                                                                        company_member, company_area),
                                                   "pukou_result": '{},{},{}&{}&{}'.format("浦口区（企业）", "浦口高新区",
                                                                                           "南京市政策（企业）", company_member,
                                                                                           company_area),
                                                   "gulou_result": '{},{}&{}&{}'.format("鼓楼区政策", "南京市政策（企业）",
                                                                                        company_member, company_area)
                                                   })


def message(request):
    if request.method == 'GET':
        return render(request, 'message.html')
    if request.method == 'POST':
        # 公司名称
        company_name = request.POST.get('name')
        # 公司规模
        company_member = request.POST.get('member')
        # 所属领域
        company_area = request.POST.get('area')
        result_list = '{} {} {}'.format(company_name, company_member, company_area)
        return render(request, 'message1.html', {"result_list": result_list})


def message1(request):
    if request.method == 'GET':
        return render(request, 'message1.html')
    if request.method == 'POST':
        # 1类自主研发
        independent_1 = request.POST.get('independent_1')
        # 1类受赠、受赠或并购
        donate_1 = request.POST.get('donate_1')
        # 1类与主要产品（服务）关联的有（）项
        relation_1 = request.POST.get('relation_1')
        # 2类自主研发
        independent_2 = request.POST.get('independent_2')
        # 2类受赠、受赠或并购
        donate_2 = request.POST.get('donate_2')
        # 2类与主要产品（服务）关联的有（）项
        relation_2 = request.POST.get('relation_2')
        # 企业是否参与编制国家标准、行业标准、检测方法、技术规范
        standard = request.POST.get('standard')
        # 企业科技成果转化数量（）项
        conversion = request.POST.get('conversion')
        result_list1 = request.POST.get("result_list")
        result_list = '{} {} {} {} {} {} {} {} {}'.format(result_list1, independent_1, donate_1, relation_1,
                                                          independent_2, donate_2, relation_2, standard, conversion)
        return render(request, 'message2.html', {"result_list": result_list})


def message2(request):
    if request.method == 'GET':
        return render(request, 'message2.html')
    if request.method == 'POST':
        # 企业是否制定了研究开发的组织管理制度，建立了研发投入核算体系，编制了研发费用辅助账？
        system = request.POST.get('system')
        # 企业是否建立了科技人员的培养进修、职工技能培训、优秀人才引进，以及人才绩效评价奖励制度
        culture = request.POST.get('culture')
        # 企业是否签订产学研合作协议
        industry = request.POST.get('industry')
        # 企业是否建立开放式的创新创业平台
        innovation = request.POST.get('innovation')
        # result_list2 = [system, culture, industry, innovation]
        result_list1 = request.POST.get("result_list")
        result_list = '{} {} {} {} {}'.format(result_list1, system, culture, industry, innovation)
        return render(request, 'message3.html', {"result_list": result_list})


def message3(request):
    if request.method == 'GET':
        return render(request, 'message3.html')
    if request.method == 'POST':
        # 近一年企业高新技术产品（服务）收入占企业同期总收入的比例是否不低于60%。
        proportion = request.POST.get('proportion')
        # 企业近三个会计年度研发费用投入总额占同期销售收入总额的比例。
        development = request.POST.get('development')
        # 近三年销售收入
        sales_1 = request.POST.get('sales_1')
        sales_2 = request.POST.get('sales_2')
        sales_3 = request.POST.get('sales_3')
        # 近三年净资产
        assets_1 = request.POST.get('assets_1')
        assets_2 = request.POST.get('assets_2')
        assets_3 = request.POST.get('assets_3')

        result_list = request.POST.get("result_list").split(" ")

        result = models.park_company_result(company_name=result_list[0], company_member=result_list[1],
                                            company_area=result_list[2],
                                            independent_1=result_list[3], donate_1=result_list[4],
                                            relation_1=result_list[5],
                                            independent_2=result_list[6], donate_2=result_list[7],
                                            relation_2=result_list[8],
                                            standard=result_list[9], conversion=result_list[10], system=result_list[11],
                                            culture=result_list[12],
                                            industry=result_list[13], innovation=result_list[14], proportion=proportion,
                                            development=development, sales_1=sales_1, sales_2=sales_2, sales_3=sales_3,
                                            assets_1=assets_1, assets_2=assets_2, assets_3=assets_3)
        result.save()
        company_member = result_list[1]
        company_area = result_list[2]
        # 雨花区政策（企业）
        yuhua = models.park_prize.objects.filter(area__in=["雨花区政策（企业）", "南京市政策（企业）"]).filter(
            company_member__in=[company_member, ""]).filter(typee__in=[company_area, ""]).order_by("id")
        yuhua_prizes = 0
        yuhua_prizes_id_list = []
        for yuhua_article in yuhua:
            yuhua_prize = yuhua_article.prize_money
            try:
                yuhua_prizes = yuhua_prizes + float(yuhua_prize)
                id = yuhua_article.id
                yuhua_prizes_id_list.append(id)
            except:
                id = yuhua_article.id
                yuhua_prizes_id_list.append(id)
        yuhua_prize_money_list = models.park_prize.objects.filter(pk__in=yuhua_prizes_id_list).order_by("id")
        # 浦口区（企业）
        pukou = models.park_prize.objects.filter(area__in=["浦口区（企业）", "浦口高新区", "南京市政策（企业）"]).filter(
            company_member__in=[company_member, ""]).filter(typee__in=[company_area, ""]).order_by("id")
        pukou_prizes = 0
        pukou_prizes_id_list = []
        for pukou_article in pukou:
            pukou_prize = pukou_article.prize_money
            try:
                pukou_prizes = pukou_prizes + float(pukou_prize)
                id = pukou_article.id
                pukou_prizes_id_list.append(id)
            except:
                id = pukou_article.id
                pukou_prizes_id_list.append(id)
        pukou_prize_money_list = models.park_prize.objects.filter(pk__in=pukou_prizes_id_list).order_by("id")
        # 鼓楼区政策
        gulou = models.park_prize.objects.filter(area__in=["鼓楼区政策", "南京市政策（企业）"]).filter(
            company_member__in=[company_member, ""]).filter(typee__in=[company_area, ""]).order_by("id")
        gulou_prizes = 0
        gulou_prizes_id_list = []
        for gulou_article in gulou:
            gulou_prize = gulou_article.prize_money
            try:
                gulou_prizes = gulou_prizes + float(gulou_prize)
                id = gulou_article.id
                gulou_prizes_id_list.append(id)
            except:
                id = gulou_article.id
                gulou_prizes_id_list.append(id)
        gulou_prize_money_list = models.park_prize.objects.filter(pk__in=gulou_prizes_id_list).order_by("id")

        result_dict = {"yuhua_prizes": yuhua_prize_money_list, "pukou_prizes": pukou_prize_money_list,
                       "gulou_prizes": gulou_prize_money_list}
        result_sum_dict = {"yuhua_prizes": yuhua_prizes, "pukou_prizes": pukou_prizes, "gulou_prizes": gulou_prizes}
        result_sum = max(result_sum_dict.values())
        key_name = max(result_sum_dict, key=result_sum_dict.get)
        result_last_area = result_dict[key_name].last().area
        return render(request, 'result_sum.html',
                      {"prize_money_list": result_dict[key_name], "prizes": str(result_sum),
                       "result_last_area": "最佳落地选择：" + result_last_area,
                       "yuhua_result": '{},{}&{}&{}'.format("雨花区政策（企业）", "南京市政策（企业）", company_member, company_area),
                       "pukou_result": '{},{},{}&{}&{}'.format("浦口区（企业）", "浦口高新区", "南京市政策（企业）", company_member,
                                                               company_area),
                       "gulou_result": '{},{}&{}&{}'.format("鼓楼区政策", "南京市政策（企业）", company_member, company_area),

                       })
