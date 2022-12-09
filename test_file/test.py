import pdfplumber,re

not_allowed_list=['SCOPE','SEA',"POWERPACK"]

pdf = pdfplumber.open('manifest.pdf')
pdf_list=[]
for page in pdf.pages:
    for page_str in page.extract_text().split('\n')[9:]:
        pdf_list.append(page_str)
pdf_list=pdf_list[:-2]
total_line=len(pdf_list)
awb_mark=[]
for i in range(len(pdf_list)):
    if re.match('[0-9]{3}-[0-9]{8} ',pdf_list[i]):
        awb_mark.append(i)
awb_mark.append(total_line)

# dic[awb]=第二行的开始7个字符，第四行国家内容，dic[houseawb]/(限制品(torf),最后一行国家内容)
manifest_detail={}

total_awbmark=len(awb_mark)
for i in range(total_awbmark-1):
    awbnumber=pdf_list[awb_mark[i]][:12]
    awb_dep=pdf_list[awb_mark[i]+1][:3]
    awb_arr=pdf_list[awb_mark[i]+1][4:7]
    awb_country=pdf_list[awb_mark[i]+3]
    awb_not_allowed_result=False
    for item in not_allowed_list:
        if item in pdf_list[awb_mark[i]]:
            awb_not_allowed_result=True
            break

    if awbnumber in manifest_detail:
        hawb_dic=manifest_detail[awbnumber][4]

    hawb_dic={}
    for k in range(1,int((awb_mark[i+1]-awb_mark[i])/4)):
        hawb_number = pdf_list[awb_mark[i]+4*k].split(" ")[0]
        not_allowed_result=False
        if hawb_number not in hawb_dic:
            for item in not_allowed_list:
                if item in pdf_list[awb_mark[i]+4*k]:
                    not_allowed_result=True
                    break
            hawb_country=pdf_list[awb_mark[i]+4*k+3]
            hawb_dic[hawb_number]=[not_allowed_result,hawb_country]
    manifest_detail[awbnumber]=[
        awb_dep,
        awb_arr,
        awb_not_allowed_result,
        awb_country,
        hawb_dic
    ]

for key in manifest_detail:
    print(key,manifest_detail[key])


            





