from django.shortcuts import render
from django.http import HttpResponse

import re
import datetime

#从func中导入send_mail模块
from .func import send_mail

#从cargo/func中导入处理相关的函数
#从pdf中提取字符串
from .func import getstrfrompdf
#将到达wa（含板箱信息）的字符串转为相关内容
from .func import extract_wa


def cgo_homepage(request):
    return render(request,'cgo_homepage_templates.html')

def cgo_desk_homepage(request):
    return render(request,'cgo_desk_homepage_templates.html')

def cgo_desk_importspecialcgo_upload(request):
    return render(request,'cgo_desk_importspecialcgo_upload_templates.html')

def cgo_desk_importspecialcgo_result(request):
    if request.method=="POST":
        myfile=request.FILES.get("Weight Arrival with ULDs")
        #读取的myfile要转为二进制文件才能被pdfplumber打开
        #转为二进制文件的方法已经包含在getstrfrompdf中
        str=getstrfrompdf(myfile.read())
        flightnumber,flightdate,arr_weight,revlocal,revtrst,nrevlocal,nrevtrst=extract_wa(str)
        context={
            'flightnumber':flightnumber,
            'flightdate':flightdate,
            'arr_weight':arr_weight,
            'revlocal':revlocal,
            'revtrst':revtrst,
            'nrevlocal':nrevlocal,
            'nrevtrst':nrevtrst,
        }
    return render(request,'cgo_desk_importspecialcgo_result_templates.html',context)


def cgo_fr_homepage(request):
    return render(request,'cgo_fr_homepage_templates.html')

def cgo_fr_cargosalesreport_upload(request):
    return render(request,'cgo_fr_cargosalesreport_upload_templates.html')

def cgo_fr_cargosalesreport_result(request):
    if request.method=="POST":
        file1=request.FILES.get('Cargo Sales Report 01')
        str1=getstrfrompdf(file1.read()).split("\n")
        dic1={}
        for item in str1:
            if "131-" in item:
                dic1[item[:13]]=item

        file2=request.FILES.get('Cargo Sales Report 02')
        str2=getstrfrompdf(file2.read()).split("\n")
        dic2={}
        for item in str2:
            if "131-" in item:
                dic2[item[:13]]=item

    set1=set(dic1.keys())
    set2=set(dic2.keys())

    in_set1_not_set2=set1 - set2
    in_set2_not_set1=set2 - set1
    in_both = set1 & set2

    in_both_not_equal=[]
    for item in in_both:
        if dic1[item] != dic2[item]:
            in_both_not_equal.append(item)



    context={
        'file1':file1.name,
        'file2':file2.name,
        'dic1':dic1,
        'dic2':dic2,
        'in_set1_not_set2':list(in_set1_not_set2),
        'in_set2_not_set1':list(in_set2_not_set1),
        'in_both_not_equal':in_both_not_equal,
        'empty_list':[],
    }
    return render(request,'cgo_fr_cargosalesreport_result_templates.html',context)


def cgo_traffic_homepage(request):
    return render(request,'cgo_traffic_homepage_templates.html')

def cgo_traffic_scsforotherairlines_upload(request):
    return render(request,'cgo_traffic_scsforotherairlines_upload_templates.html')

def cgo_traffic_scsforotherairlines_result(request):
    america_list=[
        'BOS','ORD','JFK','YVR','PDX','SEA','YYT','YUL','YHZ','YYC',
        'YYZ','YEG','DFW','AUS','LRD','MIA','IAH','ATL','MEM','SAT','MSY','BUF',
        'BWI','CHS','CLE','CLT','CMH','IAD','MCO','ORF','PHL','RDU',
        'ROC','TPA','JAX','BNA','CVG','DTW','IND','MCI',
        'MSP','PIT','SDF','STL','LAX','SLC','SFO','DEN','ELP','LAS','PHX','SAN',
    ]
    if request.method=="POST":

        #wd的出发内容
        file1=request.FILES.get('weightdep')
        str1=getstrfrompdf(file1.read()).split("\n")
        #获取航班信息
        flightinfo=re.search('[0,9,A-Z]{2} {0,4}[0-9]{2,5}/[0-9]{1,2}-[A-Z]{3}-20[0-9]{2}',str1[4])[0].split('/')
        flightnumber=flightinfo[0]
        flightdate=flightinfo[1]
        #获得星期几的结果，用于CK航班的号码确认
        week_day=datetime.datetime.strptime(flightinfo[1],"%d-%b-%Y").weekday()
        week_day_dic={
            0:"CK 253",
            1:"2",
            2:"CK 241",
            3:"4",
            4:"CK 241",
            5:"CK 241",
            6:"7",
        }
        if flightnumber=="JL 6744":
            flightnumber=week_day_dic[week_day]
        #获取运单信息
        # 需要发送scs的部分       
        scslist=[]
        #总运单数
        total_jlawb=0
        #总的日航重量
        total_jlweight=0
        #所有日航运单list,不包含邮件
        total_awb_list=[]
        for item in str1:         
            if item[:4]=='131-':
                total_awb_list.append(item[:12])
                total_jlawb+=1
                if item[12:15]==" P ":
                    total_jlweight+=float(item.split(' ')[3].split("/")[0])
                else:
                    total_jlweight+=float(re.match('[0-9]{3}-[0-9]{8} [0-9]{1,} [0-9]{1,}.[0-9]{1,}',item)[0].split(" ")[-1])
                dstn = re.search(' [A-Z]{3}-[A-Z]{3} ',item)[0].split(" ")[-2][4:]
                if dstn in america_list:
                    scslist.append(item[:12])

        #邮件位置的检查
        mailawb1=request.POST.getlist('mailawb1')
        mailawb2=request.POST.getlist('mailawb2')
        mailawb3=request.POST.getlist('mailawb3')
        maildstn1=request.POST.getlist('maildstn1')
        maildstn2=request.POST.getlist('maildstn2')
        maildstn3=request.POST.getlist('maildstn3')
 
        #邮件输入内容检查
        # 运单号位数
        if len(mailawb1[0]) !=8 and len(mailawb1[0]) !=0 :
            return HttpResponse('Mail1 awb number is wrong')
        if len(mailawb2[0]) !=8 and len(mailawb2[0]) !=0 :
            return HttpResponse('Mail2 awb number is wrong')
        if len(mailawb3[0]) !=8 and len(mailawb3[0]) !=0 :
            return HttpResponse('Mail3 awb number is wrong')
        #检查8位是不是数字
        #检查目的港是不是英语3个字符

        #邮件目的港的检查
        if maildstn1[0].upper() in america_list:
            scslist.append('131-'+mailawb1[0])
        if maildstn2[0].upper() in america_list:
            scslist.append('131-'+mailawb2[0])
        if maildstn3[0].upper() in america_list:
            scslist.append('131-'+mailawb3[0])

        #邮件内容
        scs_content=''
        for item in scslist:
            scs_content+=item+", "
        content=''
        if flightnumber[:2]=="CK" or flightnumber[:2]=="MU":
            content+='TO COCC\n\n'
        content+=flightnumber+"/"+flightdate+" 美国方面货物保函清单\n\n\n"
        content+=scs_content+"\n\n\n"
        content+="共 "+str(len(scslist))+"票\n"
        content+="日本航空"
        #发送给cocc美国保函
        send_mail('eachdayachance@hotmail.com',flightnumber+"/"+flightdate+" 美国方面货物保函",content)
        #发送给自己的航班信息
        content_jl=flightnumber+"/"+flightdate+'\n'
        content_jl+='航班总运单数：'+str(total_jlawb)+'票\n'
        content_jl+='航班总重量：'+str(total_jlweight)+'KG\n\n'
        for item in total_awb_list:
            content_jl+=item+'\n'
        send_mail('eachdayachance@hotmail.com',flightnumber+"/"+flightdate+" 航班信息情况",content_jl)

    return HttpResponse('scs info email ok')

