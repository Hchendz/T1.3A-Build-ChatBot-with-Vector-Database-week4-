"""
Prints out all vectors stored in the pdf_index.ann file
"""

from annoy import AnnoyIndex

# 指定向量维数（要与glove词向量库维数保持一致）
VECTOR_SIZE = 100

# 加载Annoy索引
index = AnnoyIndex(VECTOR_SIZE, "angular")
index.load("pdf_index.ann")

# 获取向量数量
num_vectors = index.get_n_items()

# 遍历所有向量
for i in range(num_vectors):
    # 获取向量
    vector = index.get_item_vector(i)
    # 打印向量
    print(vector)
