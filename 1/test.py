from home_work import Stack

news = Stack(int, 5)
news.push(1)
news.push(2)
news.push(3)
news.push(4)
news.push(5)
try:
    news.push(6)
except:
    print('not added')

print(news)

print(news.pull())
print(news)
try:
    news.push('dfwefe')
except:
    print('not same type')

print(news.count())
print(news.type())
news.clear()
print(news)
print(news.type())