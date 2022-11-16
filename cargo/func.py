import io
import pdfplumber
import re

#定义一些基本函数
# 返回一个从二进制pdf中提取的字符串
def getstrfrompdf(file):
    f=io.BytesIO(file) 
    pdf = pdfplumber.open(f)
    str=""
    for page in pdf.pages:
        str+=page.extract_text()+'\n'
    return str


# 进口带板箱信息的wa解析
def extract_wa(str):
    #以行为单位分割str
    original_list=str.split('\n')    
    length=(len(original_list))
    for i in range(0,length):
        #标记运单号前的锚点，方便按运单切割
        if re.match("[0-9]{3}-[0-9]{8}",original_list[i]) != None:
            original_list[i]=";"+original_list[i]

    #获取航班号，航班日期，航班到达总重量
    #for函数在str的前15行寻找正则匹配
    for i in range(15):
        if re.search('[0-9,A-Z]{2}[ ]{0,2}[0-9]{1,4}/[0-9]{1,2}-[A-Z]{3}-[0-9]{4}',original_list[i]) !=None:
                dateinfo=re.search('[0-9,A-Z]{2}[ ]{0,2}[0-9]{1,4}/[0-9]{1,2}-[A-Z]{3}-[0-9]{4}',original_list[i])[0].split('/')
                #航班号
                flightnumber=dateinfo[0]
                #航班日期
                flightdate=dateinfo[1]   
    #到达货重，整数位四舍五入
    arr_weight=round(float(original_list[-2].split(" ")[-1][:-1]))
    
    #删除不需要的信息
    #需要删除的部分必定包含delete_list中的一个字段
    delete_list=[
        "Date :",
        "Import Check Manifest",
        "Page : ",
        "Prepared by :",
        "Flight No.",
        "NATURE",
        "AIR WAYBILL PIECES",
        "OF GOODS",
        "-NIL-",
    ]
    for i in original_list[::-1]:
        for j in delete_list:
            if j in i:
                original_list.remove(i)
                break

    #标记各个进口各种运单属性的锚点，初始值为0                
    revlocal=0
    revtrst=0
    nrevlocal=0
    nrevtrst=0
    grandtotal=0
    #获取各个锚定位置的信息
    for i in range(0,len(original_list)):
        if "<REV Local>" in original_list[i]:
            revlocal=i
        if "<REV TRST>" in original_list[i]:
            revtrst=i
        if "<NREV Local>" in original_list[i]:
            nrevlocal=i
        if "<NREV TRST>" in original_list[i]:
            nrevtrst=i
        if "GRAND TOTAL" in original_list[i]:
            grandtotal=i

    #初始化各个类型运单的字符串     
    rev_local = ""
    rev_trst = ""
    nrev_local = ""
    nrev_trst= ""
    #将各个类型的运单的各行分别串起来，形成各自的字符串
    for i in range(revlocal+1,revtrst):
        rev_local = rev_local + original_list[i].strip() +" "
    rev_local=rev_local.strip()
    
    for i in range(revtrst+1,revtrst):
        rev_trst = rev_trst + original_list[i].strip() + " "
    rev_trst = rev_trst.strip()

    for i in range(nrevlocal+1,nrevtrst):
        nrev_local = nrev_local + original_list[i].strip() + " "
    nrev_local = nrev_local.strip()

    for i in range(nrevtrst+1,grandtotal-1):
        nrev_trst = nrev_trst + original_list[i].strip() + " "
    nrev_trst = nrev_trst.strip()

    #定义一个函数，用于从一个字符串中获得单个运单的信息
    #运单号，出发到达港，特殊代码，所在板箱和重量信息
    def getdetail(str):
        # 作为返回值的货物字典
        special_dic={}
        #去掉第一个空的item
        str_list=str.split(";")[1:]
        for item in str_list:
            #找出出发港-目的港这个标记
            pos=re.search(' [A-Z]{3}-[A-Z]{3} ',item).span()
            #获取运单号
            awb=item[:12]
            #获取出发港
            deps=item[pos[0]+1:pos[0]+4]
            #获取到达港
            arrs=item[pos[0]+5:pos[0]+8]
            #sstr包含从特殊代码到板箱信息的所有部分
            sstr=item[pos[1]:].strip()

            #获取运单shc代码个数
            sp_index=0
            while True:
                #循环直至第n*4的位置不是空格，代表特殊代码结束
                if sstr[sp_index*4+3]==" ":
                    sp_index=sp_index+1
                else:
                    break
            
            #初始化特殊代码字段
            shc_str=''
            #初始化板箱信息字段
            uld_str=''
            #如果特殊代码个数为0，那么所有sstr都是板箱字段
            if sp_index == 0:
                uld_str=sstr
            #其余情况是sstr去掉特殊代码部分余下的字段就是板箱字段
            else:
                uld_str=sstr[sp_index*4:]
                shc_str=sstr[:sp_index*4-1]
            
            #获得shc的各个代码，以列表形式返回
            shc_code=shc_str.split(' ')
            #板箱字符串通过空格分隔成一个列表
            uld_l=uld_str.split(' ')
            #列表中3个一组，第一个为板箱号，第二个是件数，第三个是重量
            uld_n=int(len(uld_l)/3)
            #这票运单的板箱信息，key：板箱号，value是(这个板箱上的件数，这个板箱上的重量)
            uld_dic={}
            #初始化这票运单本航班的到达总件数
            arr_total_p=0
            #初始化这票运单本航班的到达总重量
            arr_total_weight=0

            #循环板箱列表，获取信息
            for i in range(uld_n):
                uld_dic[uld_l[i*3]]=(uld_l[i*3+1],uld_l[i*3+2])
                #统计这票运单的到达总件数
                arr_total_p+=int(uld_l[i*3+1])
                #统计这票运单的到达总重量
                arr_total_weight+=float(uld_l[i*3+2])
            #round到小数点一位，防止浮点运算造成的误差
            arr_total_weight=round(arr_total_weight,1)

            #构建返回信息
            special_dic[awb]=[
                #list形式，包含special
                shc_code,
                #dict形式，板箱号:(件数，重量)
                uld_dic,
                #出发港
                deps,
                #目的港
                arrs,
                #本次航班到达总件数
                arr_total_p,
                #本次航班到达总重
                arr_total_weight,                
            ]
        return special_dic

    # 总共返回以下几个信息
    # 1.航班号    str
    # 2.航班日期  str
    # 3.到达重量  float
    # 4.rev_local的运单信息   dic[awb]=list
    # 5.rev_trst的运单信息    dic[awb]=list
    # 6.nrev_local的运单信息  dic[awb]=list
    # 7.nrev_trst的运单信息   dic[awb]=list
    
    return flightnumber,flightdate,arr_weight,getdetail(rev_local),getdetail(rev_trst),getdetail(nrev_local),getdetail(nrev_trst)

