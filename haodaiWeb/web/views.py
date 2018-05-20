import re

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from web.models import Pros, Details


def change_locName(loc):
    pass

def change_money(money):
    pass

def details_change_time_to_pros(time):
    pass



def spli_supply(supply):
    # for i in supply:
    a = re.findall(r'[0-9]+|[a-z]+', supply)
    if len(a) > 0:
        b = supply.split(a[0])  # ['分期还款', '元/月']
        print(a[0]) # 钱数
        print(b)
        b.append(a[0])
        return b
    else:
        b=[]
        b.append(supply)
        return b


def lists(request,loc='beijing',money='50',time='12',page=1):
    pro_lists = Pros.objects.filter(url_loc=loc).filter(money=money).filter(time=time)
    paginator = Paginator(pro_lists,10)
    posts = paginator.page(page)

    posts.num = pro_lists.count()
    for i in posts:

        i.bank_name = i.name.split('-')[0]
        i.bank_type = i.name.split('-')[1]
        i.new_supply = spli_supply(i.supply)
        i.list_instruction = i.instruction.split('-')

    context = {
        "pro_lists":posts,
    }
    return render(request,'lists.html',context=context)


def detail(request,id='1023',money='30',time='12'):

    pros_lists = Pros.objects.get(cid=id,money=money,time=time)  #  很多家公司
    detail_lists = Details.objects.get(id=id,deadline=time+'月',money=money+'万元')
    # 同公司同价格同时间 只差地方  根据product_url来匹配具体是哪个
    # for i in pros_lists:
    #     if not detail_lists.one:
    #         detail_lists.one = detail_lists.filter(product_url=i.product_url)

    context_list2 = detail_lists.context.split('-')
    print(context_list2)
    detail_lists.context_list = context_list2
    context = {'detail_lists':detail_lists,
               'pros_lists':pros_lists,
               # 'detail_one':detail_one,
               }
    return render(request,'detail.html',context=context)