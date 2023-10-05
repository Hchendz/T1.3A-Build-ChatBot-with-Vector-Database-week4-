"""
Code for reading and storing pdfs as vectors
"""

import os
import PyPDF2
from annoy import AnnoyIndex

# 指定PDF文件所在的文件夹路径
PDF_BASE_DIR = "data"

def read_pdf(file_path):

    """
    读取PDF文件并返回其内容
    """

    with open(file_path, "rb") as file:
        # 读取PDF文件
        reader = PyPDF2.PdfReader(file)
        content = ""
        # 循环遍历每一页并将其内容拼接在一起
        for page_num, _ in enumerate(reader.pages):
            content += reader.pages[page_num].extract_text()
    return content

def build_vector(text):

    """
    将PDF文件的内容转换为一个向量
    """

    # 将PDF文件的前10个字符的ASCII码转换为一个向量
    vector = [ord(char) for char in text[:10]]
    return vector

def main():

    """
    读取PDF文件并将其向量化,并将向量存储到Annoy索引中
    """

    # 创建Annoy索引
    print("Start generating Annoy indexes")

    # 指定向量的长度和向量间距离度量方式
    annoy_index = AnnoyIndex(10, "angular")

    # 遍历PDF所在文件夹下的文件
    for i, item in enumerate(os.listdir(PDF_BASE_DIR)):
        if item.endswith(".pdf"):
            file_path = os.path.join(PDF_BASE_DIR, item)

            # 读取PDF文件
            try:
                content = read_pdf(file_path)
            except FileNotFoundError as error:
                print(f"无法读取文件{file_path}，错误信息为：{error}")
                continue

            # 生成向量
            vector = build_vector(content)

            # 将向量添加到Annoy索引
            annoy_index.add_item(i, vector)

    # 构建Annoy索引
    annoy_index.build(10)

    # 保存Annoy索引
    annoy_index.save("pdf_index.ann")

    print("Annoy indexes generation complete")

if __name__ == "__main__":
    main()
