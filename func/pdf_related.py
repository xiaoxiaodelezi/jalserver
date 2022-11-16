# 这是一个处理pdf的通用包

# 导入包清单
# pdfplumber

import pdfplumber

# 返回一个从pdf中提取的字符串，如果错误或者不是pdf文件，返回空字符串。
def getstrfrompdf(path,filename):
    if filename[len(filename)-4:].lower() != '.pdf':
        return ""
    
    pdf = pdfplumber.open(path+'/'+filename)
    str=""
    for page in pdf.pages:
        str+=page.extract_text()+'\n'
    return str







