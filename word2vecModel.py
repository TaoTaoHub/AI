#生成词向量
import word2vec

word2vec.word2vec('word.txt', 'Word2VecModel.bin', size=300,verbose=True)
