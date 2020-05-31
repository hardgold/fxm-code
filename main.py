import os
import json
from collections import Counter
import hashlib
import time
import numpy as np
class SSE:
    # file rename so that we can use 'with open command'to read dataset
    def file_rename(self,dataset_dictionary):
        # 使用os.walk遍历所有的目录和文件
        for root, dirs, files in os.walk(dataset_dictionary):
            for file in files:
                os.rename(os.path.join(root,file),os.path.join(root,file)+'.txt')

    def message_ID_list(self,dataset_dictionary,message_ID_filename):
        # 使用os.walk遍历所有的目录和文件
        message_ID_list = []
        for root, dirs, files in os.walk(dataset_dictionary):
            for file in files:
                # to get first line (message_ID) of each file
                with open(os.path.join(root, file), 'r', encoding='ISO-8859-1') as lines:
                    for line in lines:
                        line = line.split('\\', 1)[0]
                        message_ID_list.append(line)
                        break
        # save message_ID to json file
        with open('./output/'+message_ID_filename+'.json', 'w',encoding='ISO-8859-1') as f2w:
            json.dump(message_ID_list, f2w, indent=4)

    def e_message_ID(self,message_ID_file,e_message_ID_filename,average_number,keyword_number):
        message_ID_file = message_ID_file
        average_number = average_number
        error_number = 0
        keyword_number = keyword_number
        e_message_ID = []
        # encryption
        encryption_time = []
        for j in range(int(average_number)):
            number = keyword_number
            keyword_number_time_start = time.time()
            for message_ID in message_ID_file:
                try:
                    if(j == 0):
                        e_message_ID.append(hashlib.md5(message_ID.encode('utf-8')).hexdigest())
                    #print(message_ID)
                    number -= 1
                    if (number <= 0):
                        break
                except:
                    error_number += 1
                    continue
            keyword_number_time_end = time.time()
            encryption_time.append(keyword_number_time_end - keyword_number_time_start)
            #print(encryption_time)
        # print(encryption_time)
        print('Average time:', np.average(encryption_time))
        print('Minimun time:', np.min(encryption_time))
        print('error_number:',error_number)
        with open('./output/' + e_message_ID_filename + '.json', 'w', encoding='utf-8') as f2w:
            json.dump(e_message_ID, f2w, indent=4)

    def ID2word(self, dataset_dictionary,ID2word_filename):
        # 使用os.walk遍历所有的目录和文件
        word_dic = {}
        for root, dirs, files in os.walk(dataset_dictionary):
            for file in files:
                with open(os.path.join(root, file), 'r', encoding='ISO-8859-1') as lines:
                    for line in lines:
                        line = line.split('\\', 1)[0]
                        break
                    file_content = lines.read().split()
                    top_one = Counter(file_content).most_common(1)
                    #print(os.path.join(root, file))
                    word_dic[line] = top_one
        # save word_dic to json file:
        with open('./output/'+ID2word_filename+'.json', 'w', encoding='ISO-8859-1') as f2w1:
            json.dump(word_dic, f2w1, indent=4)

    def e_ID2word(self, ID2word_file,e_message_ID2word_filename,average_number,keyword_document_pairs):
        # get message_ID2word and save it to json file
        average_number = average_number
        message_ID2word = ID2word_file
        error_number = 0
        keyword_document_pairs = keyword_document_pairs

        e_message_ID2word = {}
        # encryption
        encryption_time = []
        for j in range(int(average_number)):
            number = keyword_document_pairs
            keyword_document_time_start = time.time()
            for message_ID in message_ID2word:
                try:
                    e_document = hashlib.md5(message_ID.encode('utf-8')).hexdigest()
                    e_keyword = hashlib.md5(message_ID2word[message_ID][0][0].encode('utf-8')).hexdigest()
                    e_message_ID2word[e_document] = e_keyword
                    # print(message_ID)
                    number -= 1
                    if (number <= 0):
                        break
                except:
                    error_number += 1
                    continue
            keyword_document_time_end = time.time()
            encryption_time.append(keyword_document_time_end - keyword_document_time_start)
        # print(encryption_time)
        print('Average time:', np.average(encryption_time))
        print('Minimun time:', np.min(encryption_time))
        print('error_number:',error_number)
        with open('./output/' + e_message_ID2word_filename + '.json', 'w', encoding='utf-8') as f2w:
            json.dump(e_message_ID2word, f2w, indent=4)

    def search_on_message_ID2word(self,message_ID2word_file,keyword,average_number,keyword_document_pairs):
        message_ID2word = message_ID2word_file
        average_number = average_number
        error_number = 0
        keyword_document_pairs = keyword_document_pairs

        search_time = []
        #count number of keyword
        keyword_number=0
        for j in range(int(average_number)):
            number = keyword_document_pairs
            keyword_document_time_start = time.time()
            for message_ID in message_ID2word:
                try:
                    #print(message_ID2word[message_ID])
                    if(keyword == message_ID2word[message_ID][0][0] ):
                        keyword_number += message_ID2word[message_ID][0][1]
                    number -= 1
                    if (number <= 0):
                        break
                except:
                    error_number += 1
                    continue
            keyword_document_time_end = time.time()
            search_time.append(keyword_document_time_end - keyword_document_time_start)
        # print(search_time)
        print('Average time(search):', np.average(search_time))
        print('Minimun time(search):', np.min(search_time))
        print('count number of keyword:',keyword_number/int(average_number))
if __name__=='__main__':
    test = SSE()
    #input
    dataset_dictionary = r"C:\Users\lenovo\Desktop\fxm-experiment\dataset\maildir"
    message_ID_filename = "message_ID"
    e_message_ID_filename = "e_message_ID"
    ID2word_filename = "message_ID2word"
    e_message_ID2word_filename = "e_message_ID2word"

    #rename
    test.file_rename(dataset_dictionary)

    #init message_ID and message_ID2word
    # message_ID_file = test.message_ID_list(dataset_dictionary,message_ID_filename)
    # message_ID2word = test.ID2word(dataset_dictionary,ID2word_filename)


    #fig 2
    # print('fig 2:')
    # average_number = input('input number to average:')
    # average_number = int(average_number)
    # keyword_number = input('input number of keyword_number:')
    # keyword_number = int(keyword_number)
    # fig2_read_start = time.time()
    # with open('./output/' + e_message_ID_filename + '.json', 'r', encoding='utf-8') as f2r:
    #     message_ID_file=json.load(f2r)
    # fig2_read_end = time.time()
    # print('fig2_read_time:',fig2_read_end-fig2_read_start)
    # fig2_encryption_start = time.time()
    # test.e_message_ID(message_ID_file,e_message_ID_filename,average_number,keyword_number)
    # fig2_encryption_end = time.time()
    # print('fig2_encryption:',fig2_encryption_end-fig2_encryption_start)


    #fig 3
    # print('fig 3:')
    # average_number = input('input number to average:')
    # average_number = int(average_number)
    # keyword_document_pairs = input('input number of keyword_document_pairs:')
    # keyword_document_pairs = int(keyword_document_pairs)
    # fig3_read_start = time.time()
    # with open('./output/' + ID2word_filename + '.json', 'r', encoding='utf-8') as f2r:
    #     message_ID2word=json.load(f2r)
    # fig3_read_end = time.time()
    # print('fig2_read_time:',fig3_read_end-fig3_read_start)
    # fig3_encryption_start = time.time()
    # test.e_ID2word(message_ID2word,e_message_ID2word_filename,average_number,keyword_document_pairs)
    # fig3_encryption_end = time.time()
    # print('fig3_encryption_time',fig3_encryption_end-fig3_encryption_start)



    #fig 4 in vmware



    #fig 5
    # print('fig 5:')
    # average_number = input('input number to average:')
    # average_number = int(average_number)
    # keyword_document_pairs = input('input number of keyword_document_pairs:')
    # keyword_document_pairs = int(keyword_document_pairs)
    # keyword = input('input the keyword for search:')
    # fig5_read_start = time.time()
    # with open('./output/' + ID2word_filename + '.json', 'r', encoding='utf-8') as f2r:
    #     message_ID2word=json.load(f2r)
    # fig5_read_end = time.time()
    # print('fig5_read_time:',fig5_read_end-fig5_read_start)
    # fig5_search_start = time.time()
    # test.search_on_message_ID2word(message_ID2word, keyword, average_number, keyword_document_pairs)
    # fig5_search_end = time.time()
    # print('fig5_search_time:',fig5_search_end-fig5_search_start)
