import bisect

'''
官方api联系 https://www.apiref.com/python-zh/library/index.html
'''


#二分法查找
# 注意：bisect 模块要求输入序列必须是已排序的，否则结果可能不准确。
sorted_list = [1, 3, 4, 6, 8, 9]
index = bisect.bisect_left(sorted_list, 4, 0, len(sorted_list))
print(index)

index2 = bisect.bisect_left(sorted_list, 8, 0, len(sorted_list))
print(index2)

bisect.insort_left(sorted_list,5)
print(sorted_list)


import csv
#csv
with open('source\\eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


#hash
import hashlib
seed = hashlib.sha256()
seed.update(b"Nobody inspects the spammish repetition")
print(seed.hexdigest())