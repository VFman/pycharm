import os
import re
import PyPDF2
import pandas as pd

# 读取 PDF 文件路径
pdf_path = r"C:\Users\w\Desktop\tdc\示例数据\01_“未来校园”智能应用专项赛.pdf"

# 获取文件所在的文件夹路径
folder_path = os.path.dirname(pdf_path)

# 打开 PDF 文件并读取内容
with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

# 定义一个函数来提取每个信息
def extract_info(text):
    # 提取赛项名称
    competition_name = re.search(r"第[\u4e00-\u9fa5]+(?:赛|赛项)", text)
    competition_name = competition_name.group(0) if competition_name else "未知"

    # 提取赛道
    track = re.search(r"赛道[:：]?\s*(\S+)", text)
    track = track.group(1) if track else "未知"

    # 提取发布时间
    release_time = re.search(r"(\d{4}年\d{2}月|\d{4}-\d{2})", text)
    release_time = release_time.group(0) if release_time else "未知"
    # 提取报名时间
    registration_time = re.search(r"报名时间[:：]?\s*(\d{4}-\d{2}-\d{2})", text)
    registration_time = registration_time.group(1) if registration_time else "未知"

    # 提取组织单位
    organization = re.search(r"组织单位[:：]?\s*([\u4e00-\u9fa5]+)", text)
    organization = organization.group(1) if organization else "未知"

    # 提取官网
    website = re.search(r"官网[:：]?\s*(http[s]?://[^\s]+)", text)
    website = website.group(1) if website else "未知"

    return competition_name, track, release_time, registration_time, organization, website

# 提取信息
competition_name, track, release_time, registration_time, organization, website = extract_info(text)

# 将数据保存为 DataFrame
competition_info = {
    "赛项名称": [competition_name],
    "赛道": [track],
    "发布时间": [release_time],
    "报名时间": [registration_time],
    "组织单位": [organization],
    "官网": [website]
}

df = pd.DataFrame(competition_info)

# 输出文件路径：保存在与 PDF 相同的文件夹中
output_path = os.path.join(folder_path, "result_.xlsx")

# 将数据写入 Excel 文件
df.to_excel(output_path, index=False)

print(f"结果已保存至: {output_path}")

#sdfaaksdjflisadjifhjsakjdfhjaskdhfjkadshf