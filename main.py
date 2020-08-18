from textblob import TextBlob


a = open("a.txt", "r")

def return_polarity(text):
    tex = TextBlob(text)
    if tex.sentiment.polarity > 0:
        return 0
    elif tex.sentiment.polarity < 0:
        return 1
    else:
        return 2

pos = 0
neg = 0
png = 0
count = 0

for i in a.read().split('\n'):
    a = return_polarity(i)
    if a == 0:
        pos += 1
    elif a == 1:
        neg +=1
    else:
        png +=1
    count +=1

print(f"Positive {pos/count*100}")
print(f"Negative {neg/count*100}")
print(f"Neutral {png/count*100}")
