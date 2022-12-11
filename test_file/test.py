import pdfplumber,re,openpyxl,decimal

# not_allowed_list=['SCOPE','SEA',"POWERPACK"]

# pdf = pdfplumber.open('manifest.pdf')
# pdf_list=[]
# for page in pdf.pages:
#     for page_str in page.extract_text().split('\n')[9:]:
#         pdf_list.append(page_str)
# pdf_list=pdf_list[:-2]
# total_line=len(pdf_list)
# awb_mark=[]
# for i in range(len(pdf_list)):
#     if re.match('[0-9]{3}-[0-9]{8} ',pdf_list[i]):
#         awb_mark.append(i)
# awb_mark.append(total_line)

# # dic[awb]=第二行的开始7个字符，第四行国家内容，dic[houseawb]/(限制品(torf),最后一行国家内容)
# manifest_detail={}

# total_awbmark=len(awb_mark)
# for i in range(total_awbmark-1):
#     awbnumber=pdf_list[awb_mark[i]][:12]
#     awb_dep=pdf_list[awb_mark[i]+1][:3]
#     awb_arr=pdf_list[awb_mark[i]+1][4:7]
#     awb_country=pdf_list[awb_mark[i]+3]
#     awb_not_allowed_result=False
#     for item in not_allowed_list:
#         if item in pdf_list[awb_mark[i]]:
#             awb_not_allowed_result=True
#             break

#     if awbnumber in manifest_detail:
#         hawb_dic=manifest_detail[awbnumber][4]

#     hawb_dic={}
#     for k in range(1,int((awb_mark[i+1]-awb_mark[i])/4)):
#         hawb_number = pdf_list[awb_mark[i]+4*k].split(" ")[0]
#         not_allowed_result=False
#         if hawb_number not in hawb_dic:
#             for item in not_allowed_list:
#                 if item in pdf_list[awb_mark[i]+4*k]:
#                     not_allowed_result=True
#                     break
#             hawb_country=pdf_list[awb_mark[i]+4*k+3]
#             hawb_dic[hawb_number]=[not_allowed_result,hawb_country]
#     manifest_detail[awbnumber]=[
#         awb_dep,
#         awb_arr,
#         awb_not_allowed_result,
#         awb_country,
#         hawb_dic
#     ]

# for key in manifest_detail:
#     print(key,manifest_detail[key])


# def pdf_excel_cross_check(pdf,xlsx):            
#     pdf=pdfplumber.open(pdf)
#     pdf_awb_dic={}
#     for page in pdf.pages:
#         for line in page.extract_text().split("\n"):
#             if line[:4] == "131-":
#                 if "/" in line:
#                     pdf_awb_dic[line[:3]+line[4:12]]=" ".join(line[13:].split(' ')[:-1]).replace(",","")
#                 else:
#                     pdf_awb_dic[line[:3]+line[4:12]]=" ".join(line[13:].split(' ')).replace(",","")

#     wb=openpyxl.load_workbook(xlsx,data_only=True)
#     ws=wb.worksheets[0]
#     excel_awb_dic={}
#     for i in range (2,ws.max_row+1):
#         awbnum=ws.cell(i,13).value
#         v=decimal.Decimal(ws.cell(i,22).value).quantize(decimal.Decimal('0.00'))
#         ac=decimal.Decimal(ws.cell(i,29).value).quantize(decimal.Decimal('0.00'))
#         y=decimal.Decimal(ws.cell(i,25).value).quantize(decimal.Decimal('0.00'))
#         v_ab=decimal.Decimal(float(ws.cell(i,22).value)-float(ws.cell(i,28).value)).quantize(decimal.Decimal('0.00'))
#         ab__ac=decimal.Decimal(float(ws.cell(i,28).value)+float(ws.cell(i,29).value)).quantize(decimal.Decimal('0.00'))#ab+ac
#         i_j=ws.cell(i,9).value+"-"+ws.cell(i,10).value#i-j
#         x=decimal.Decimal(float(ws.cell(i,24).value)).quantize(decimal.Decimal('0.00'))#x
#         excel_awb_str=str(v)+" "+str(ac)+" "
#         if y:
#             excel_awb_str+=str(y)+" "
#         if v_ab:
#             excel_awb_str+=str(v_ab)+" "
#         excel_awb_str+= str(ab__ac)+" "+i_j+" "+str(x)
#         excel_awb_dic[ws.cell(i,13).value]=excel_awb_str

#     setpdf=set(pdf_awb_dic.keys())
#     setexcel=set(excel_awb_dic.keys())
#     inpdfnotexcel=list(setpdf-setexcel)
#     inexcelnotpdf=list(setexcel-setpdf)
#     notequal=[]
#     for item in list(setexcel & setpdf):
#         if excel_awb_dic[item] != pdf_awb_dic[item]:
#             notequal.append(item)
#     return inpdfnotexcel,inexcelnotpdf,notequal

# a,b,c=pdf_excel_cross_check('sale.pdf','111.xlsx')
# print(a)
# print("---")
# print(b)
# print("---")
# print(c)

# def excel_excel_check(xlsx1,xlsx2):     
#     check_col_list=[22,24,25,26,28,29]       
#     wb1=openpyxl.load_workbook(xlsx1,data_only=True)
#     ws=wb1.worksheets[0]
#     xlsx1_awb_dic={}
#     for i in range (2,ws.max_row+1):
#         add_list=[]
#         for col in check_col_list:
#             add_list.append(ws.cell(i,col).value)
#         xlsx1_awb_dic[ws.cell(i,13).value]=add_list
#     wb1.close()

#     wb2=openpyxl.load_workbook(xlsx2,data_only=True)
#     ws=wb2.worksheets[0]
#     xlsx2_awb_dic={}
#     for i in range (2,ws.max_row+1):
#         add_list=[]
#         for col in check_col_list:
#             add_list.append(ws.cell(i,col).value)
#         xlsx2_awb_dic[ws.cell(i,13).value]=add_list
#     wb2.close()

#     xlsx1_set=set(xlsx1_awb_dic.keys())
#     xlsx2_set=set(xlsx2_awb_dic.keys())

#     in1not2=list(xlsx1_set-xlsx2_set)
#     in2not1=list(xlsx2_set-xlsx1_set)
#     not_equal_list=[]

#     for awb in (xlsx1_set & xlsx2_set):
#         if xlsx1_awb_dic[awb] != xlsx2_awb_dic[awb]:
#             not_equal_list.append(awb)

#     return in1not2,in2not1,not_equal_list
