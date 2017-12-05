import numpy as np
from scipy import sparse
import random

def save_sparse_csr(filename, array):
    np.savez(filename,data = array.data ,indices=array.indices,
             indptr =array.indptr, shape=array.shape )

def xblog():
    data = np.zeros((10312, 10312))
    m,n = data.shape
    for i in range(m):
        data[i][i] = 1
    # list(range(0, 10312)) #[0,1,2...10311]
    np.random.shuffle(data)
    # print data
    # index = list(range(0, 10312)) 
    # final =[]
    # for i in range(10312):
    #     final.append([index[i],data[i]])
    # final = np.array(final)
    # final = sparse.csr_matrix(final)
    # print final,final.shape
    # data = random.sample(data,10312/10)
    x = data[:int(10312*0.1)]
    vx = data[int(10312*0.1):int(10312*0.2)]
    tx = data[int(10312*0.2):]
    xData = sparse.csr_matrix(x)
    txData =sparse.csr_matrix(tx)
    print xData, xData.shape
    print txData, txData.shape
    save_sparse_csr('trans.blog.x', xData)
    save_sparse_csr('trans.blog.tx', txData)

    # xData.tofile('trans.blog.x')
    # txData.tofile('trans.blog.tx')
    # sData.save

def blogy():
    blog = np.load('blog_labels.npy')
    random.shuffle(blog)
    yblog = blog[:int(10312*0.1)]
    vy = blog[int(10312*0.1):int(10312*0.2)]
    tyBlog = blog[int(10312*0.2):]
    np.save('trans.blog.y',yblog)
    np.save('trans.blog.ty',tyBlog)
    # yblog.tofile('train.blog.y')
    # tyBlog.tofile('train.blog.ty')

    print blog,'hahahahah', blog.shape

def graph():
    graph = {}
    with open('blog_adj_undirected.txt') as fin:
        for line in fin:
            ls = line.rstrip().split('\t')
            print ls
            if int(ls[0]) in graph:
                graph[int(ls[0])].append(int(ls[1]))
            else:
                graph[int(ls[0])] = []
        print graph
    np.save('train.blog.graph',graph)

blogy()
# graph()