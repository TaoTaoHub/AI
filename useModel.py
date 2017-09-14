#使用训练好的model
import word2vec

#300维向量
model = word2vec.load('Word2VecModel.bin')
words = model.cosine('努力')
vec = model['网']
print(vec.dot(vec))
#print(model['努力'])
#print(words)
#for x in words[0]:
    #print(model.vocab[x])