#分词
import jieba

filePath = 'corpus.txt'
resultPath = 'word.txt'

saveFile = open(resultPath, 'wb')
count = 0
with open(filePath, encoding='utf-8') as content:
    for line in content:
        if not line:
            continue
        temp = ' '.join(jieba.cut(line[9:-11]))
        saveFile.write(temp.encode('utf-8'))
        saveFile.write('\n'.encode('utf-8'))
        count += 1
        if count % 1000 == 0:
            print(str(count)+'条分词：success')
        if count == 40000:
            break
saveFile.close()




