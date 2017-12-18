import numpy as np
from scipy import sparse
import random
import scipy.sparse
import cPickle

def save(obj, filename):
    cPickle.dump(obj, open(filename, 'wb'))

def save_sparse_csr(filename, array):
    np.savez(filename,data = array.data ,indices=array.indices,
             indptr =array.indptr, shape=array.shape )

def blogx():
    # sparse.coo_matrix((data, (row, col)), shape = (len(ents), f_num), dtype = np.float32).tocsr()
    data = np.zeros((10312, 10312),dtype = np.float32)
    m,n = data.shape
    for i in range(m):
        data[i][i] = 1
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
    xData = sparse.csr_matrix(x, dtype = 'float32')
    txData =sparse.csr_matrix(tx, dtype = 'float32')
    print xData, xData.shape
    print txData, txData.shape
    # scipy.sparse.save_npz('trans.blog.x', xData)
    # scipy.sparse.save_npz('trans.blog.tx', txData)
    save(xData, '../data/trans.blog.x')
    save(txData, '../data/trans.blog.tx')
    # np.save('trans.blog.x', xData)
    # np.save('trans.blog.tx', txData)
    # save_sparse_csr('trans.blog.x', xData)
    # save_sparse_csr('trans.blog.tx', txData)


def blogy():
    blog = np.load('blog_labels.npy')
    random.shuffle(blog)
    yblog = blog[:int(10312*0.1)]
    vy = blog[int(10312*0.1):int(10312*0.2)]
    tyBlog = blog[int(10312*0.2):]
    # yblog = sparse.csr_matrix(yblog)
    # tyBlog =sparse.csr_matrix(tyBlog)
    # scipy.sparse.save_npz('trans.blog.y',yblog)
    # scipy.sparse.save_npz('trans.blog.ty',tyBlog)

    save(yblog.astype(np.int32),'../data/trans.blog.y')
    save(tyBlog.astype(np.int32), '../data/trans.blog.ty')
    # np.save('trans.blog.y',yblog)
    # np.save('trans.blog.ty',tyBlog)


    print blog,'hahahahah', blog.shape
    print yblog.astype(np.int32).dtype

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
                graph[int(ls[0])].append(int(ls[1]))
        print graph
        save(graph, '../data/trans.blog.graph')
    # np.save('trans.blog.graph',graph)


# blogx()
blogy()
# graph()