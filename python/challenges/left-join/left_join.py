def left_join(hash1,hash2):
    left_join_result =[]
	
    for word in hash1:
        temp = []
        temp.append(word)
        temp.append(hash1[word])
        if word in hash2:
            temp.append(hash2[word])
        else:
            temp.append('NULL')
        left_join_result.append(temp)

    return left_join_result

hashy_1 = {'happy': 'ecstatic', 'tall': 'high', 'down': 'below', 'fast': 'quick'}

hashy_2 = {'happy': 'sad', 'tall': 'short', 'down': 'up'}

print(left_join(hashy_1,hashy_2))
# for word in hashy_1:
#     print(hashy_1[word])