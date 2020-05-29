import os
import json
from collections import Counter
# 使用os.walk遍历所有的目录和文件
message_ID_list=[]
word_dic={}
for root,dirs,files in os.walk(r"C:\Users\lenovo\Desktop\fxm\email_dataset\maildir"):
    for file in files:
        #file rename so that we can use 'with open command'
        #os.rename(os.path.join(root,file),os.path.join(root,file)+'.txt')
        #print('join:',os.path.join(root,file))

        # to get first line (message_ID) of each file
        with open(os.path.join(root,file),'r',encoding='ISO-8859-1') as lines:
            for line in lines:
                line=line.split('\\',1)[0]
                message_ID_list.append(line)
                break
            file_content=lines.read().split()
            top_three=Counter(file_content).most_common(3)
            print(os.path.join(root,file))
            word_dic[line]=top_three
            #print('word_dic',word_dic)



#save message_ID to json file
with open('message_ID.json','w') as f2w:
    json.dump(message_ID_list,f2w,indent=4)


#save word_dic to json file:
with open('word_dic.json','w',encoding='ISO-8859-1') as f2w1:
    json.dump(word_dic,f2w1,indent=4)



#for search
# keyword=input('please input the keyword:')
#
# #load the word_dic json file
# with open('word_dic.json','r',encoding='utf-8') as f2r:
#     read_word_dic=json.load(f2r)
#
# # count number of keyword
# key_number=0
# for key in read_word_dic.keys():
#     #top three
#     for i in range(3):
#         if(keyword == read_word_dic[key][i][0]):
#             key_number+=read_word_dic[key][i][1]
#
# print('key_number:',key_number)




