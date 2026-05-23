def most_frequent_word(s):
    words=s.lower().split()
    freq={}

    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    max_count=max(freq.values())

    result=[]
    for word in freq:
        if freq[word]==max_count:
            result.append(word)
    return sorted(result)[0]
s=input("enter text: ")
print(most_frequent_word(s))