# T1.3A-week4（PDF读取&存储）
## 1.代码流程简述
- 使用PyPDF2库中的PdfReader()读取pdf文件，转化为test
- 通过与glove词向量库匹配，将text转换为向量
- 将向量存储到Annoy索引中，生成.ann文件

## 2. 文件含义
### 2.1 data文件夹  
用来存放需要读取、存储的pdf，pdf需以数字序号按顺序命名（如0.pdf、1.pdf、2.pdf...）
### 2.2 pdf_storage.py
主代码
### 2.3 pdf_index.ann
pdf的向量数据存储处
### 2.4 glove.6B.xxxd.txt
glove词向量库文件，xxxd代表词向量库所使用的维数（100d表示每个词向量的维数为100），可通过修改主代码中的VECTOR_SIZE和GLOVE_FILE变量来选择
![图片](https://github.com/Hchendz/T1.3A-week4/assets/144656283/0a6f7876-a6fa-4573-8d96-35d9f974bdbb)

### 2.5 print_vectors.py
辅助工具，可打印出pdf_index.ann中存储的所有向量，第n个向量对应n.pdf，注意VECTOR_SIZE需与存储的向量维数一致

## 3. 运行方法
安装所需库————下载glove.6B.xxxd.txt、pdf_storage.py————运行pdf_storage.py
