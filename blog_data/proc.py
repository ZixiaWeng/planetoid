import numpy as np

def blog():
    with open('blog_adj_directed.csv') as fin, open('blog_adj_undirected.txt', 'w') as fout:
        for line in fin:
            ls = line.rstrip().split(',')
            print '@@@',ls
            assert(len(ls)==2)
            id0 = int(ls[0]) -1
            id1 = int(ls[1]) -1
            line = line.replace(",", "\t")
            line = line + '\t1'
            fout.write('%s\t%s\n' % (id0, id1))
            fout.write('%s\t%s\n' % (id1, id0))
            # print ('(%s, %s)\t%s\n' % (id0, id1, '1.0'))

def blogx():
    with open('blog_adj_directed.csv') as fin, open('train.blog.x', 'w') as fout:
        for line in fin:
            ls = line.rstrip().split(',')
            print '@@@',ls
            assert(len(ls)==2)
            id0 = int(ls[0]) -1
            id1 = int(ls[1]) -1
            line = line.replace(",", "\t")
            line = line + '\t1'
            fout.write('(%s, %s)\t%s\n' % (id0, id1, '1.0'))
            fout.write('(%s, %s)\t%s\n' % (id1, id0, '1.0'))
            # print ('(%s, %s)\t%s\n' % (id0, id1, '1.0'))

def blogy():
    blog = np.load('blog_labels.npy')
    blog.tofile('train.blog.y')

  #   with open('blog_labels.npy') as fin, open('train.blog.y', 'w') as fout:
		# row = 0 
  #       num_rows, num_cols = blog.shape
  #       x = 0
  #       print('$$$$',num_rows)
  #       for row in range(num_rows):
  #           col = 0
  #           for i in blog[row]:
  #               if i != 0:
  #                   line = str(row) +','+str(col)
  #                   if col > x:
  #                       x = col
  #                   # print line
  #                   #fout.write(line)
  #                   # fout.write('%s\t%s\n' % (row,col))
  #               else:
  #                   col+=1

    print blog,'hahahahah'

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
# blogy()
graph()