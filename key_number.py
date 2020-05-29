import json

#load the word_dic json file
read_word_dic={}
key_number={}
with open('word_dic.json','r',encoding='ISO-8859-1') as f2r:
    read_word_dic=json.load(f2r)
key_list=[]
for key in read_word_dic.keys():
    #top three
    for i in range(3):
        key_list.append(read_word_dic[key][i])

#print(key_list[0])
for keyword in key_list:
    if(keyword[0] not in key_number):
        key_number[keyword[0]]=keyword[1]
    else:
        key_number[keyword[0]]+=keyword[1]



with open('key_number.json','w',encoding='ISO-8859-1') as f2r:
    json.dump(key_number,f2r,indent=4)

