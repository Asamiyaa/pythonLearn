def count_words(text):
    words = text.split()
    return len(words)

# text = input("请输入要统计字数的文本：")
# word_count = count_words(text)
# print("文本字数为：", word_count)

import PyPDF2

# 别人的调教   Github Copilot X Chat  无敌    https://www.youtube.com/watch?v=rjCYgBdJlUo

# def merge_pdfs(input_pdfs, output_pdf):
#     merger = PyPDF2.PdfFileMerger()
#
#     for pdf in input_pdfs:
#         merger.append(pdf)
#
#     merger.write(output_pdf)
#     merger.close()
#
#
# # 指定要合并的PDF文件列表
# input_pdfs = ["file1.pdf", "file2.pdf", "file3.pdf"]
#
# # 指定要输出的合并后的PDF文件
# output_pdf = "merged.pdf"
#
# # 调用合并函数
# merge_pdfs(input_pdfs, output_pdf)


import os
from PyPDF2 import PdfMerger

def merge_pdfs_from_folder(folder_path, output_pdf):
    merger = PdfMerger()

    # 遍历文件夹中的所有PDF文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder_path, filename)
            merger.append(filepath)

    # 将合并后的PDF保存到输出文件
    merger.write(output_pdf)
    merger.close()

# 指定要合并的PDF文件夹路径
folder_path = "D:\\Aitest\\input"

# 指定要输出的合并后的PDF文件路径
# output_pdf = "C:\\Users\\73699\\PycharmProjects\\pythonLearn"
output_pdf = "D:\\Aitest\\output\\test.pdf"  #写道具体文件而不是文件夹
# os.chmod(output_pdf, 0o777)



# 调用合并函数
merge_pdfs_from_folder(folder_path, output_pdf)