"""
Code for reading and storing pdfs as vectors
"""

import re
import os
import PyPDF2
import numpy as np
from annoy import AnnoyIndex
from gensim.models import KeyedVectors

# 指定PDF文件所在的文件夹路径
PDF_BASE_DIR = "data"

# 指定glove词向量库 & 向量维数（要与glove词向量库维数保持一致）
GLOVE_FILE = "glove.6B.100d.txt"
VECTOR_SIZE = 100

def load_glove_vectors(glove_file):
    """
    加载GloVe词向量
    """

    with open(glove_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    word_vectors = KeyedVectors(vector_size = VECTOR_SIZE)
    vectors = []
    words = []
    for line in lines:
        values = line.strip().split()
        word = values[0]
        vector = [float(x) for x in values[1:]]
        vectors.append(vector)
        words.append(word)
    word_vectors.add_vectors(words, vectors)
    return word_vectors

WORD_VECTORS = load_glove_vectors(GLOVE_FILE)

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

    # 清理文本并分词
    words = re.findall(r'\w+', text.lower())

    # 初始化向量
    vector = np.zeros(VECTOR_SIZE)

    # 遍历单词并累加词向量
    word_count = 0
    for word in words:
        if word in WORD_VECTORS:
            vector += WORD_VECTORS[word]
            word_count += 1

    # 计算平均词向量
    if word_count > 0:
        vector /= word_count

    return vector

def main():
    """
    读取PDF文件并将其向量化,并将向量存储到Annoy索引中
    """

    print("Start generating Annoy indexes")

    # 指定向量的长度和向量间距离度量方式
    annoy_index = AnnoyIndex(VECTOR_SIZE, "angular")

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
    n_trees = 20
    annoy_index.build(n_trees)

    # 保存Annoy索引
    annoy_index.save("pdf_index.ann")

    print("Annoy indexes generation complete")

if __name__ == "__main__":
    main()
