"""
打印pdf_index.ann文件中储存的所有向量
"""

from annoy import AnnoyIndex

# 加载Annoy索引
index = AnnoyIndex(10, "angular")
index.load("pdf_index.ann")

# 获取向量数量
num_vectors = index.get_n_items()

# 遍历所有向量
for i in range(num_vectors):
    # 获取向量
    vector = index.get_item_vector(i)
    # 打印向量
    print(vector)
