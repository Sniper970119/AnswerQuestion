# -*-coding:utf-8 -*-
import pickle
import pprint


def add():
    global dict_question
    dict_question = check()
    que = input("input:")
    answer = input("answer")
    dict_question[que] = answer
    # f = open('./DataBase/DataBase.txt', 'ab')
    # pickle.dump(dict_question, f)
    f = open('./DataBase/DataBase.txt', 'w')
    f.write(str(dict_question))
    f.close()
    print("success")
    # print(dict_question)
    # while True:
    #     que = input("input:")
    #     answer = input("answer")
    #     dict_question = {que: answer}
    #     # f = open('./DataBase/DataBase.txt', 'ab')
    #     # pickle.dump(dict_question, f)
    #     f = open('./DataBase/DataBase1.txt', 'a')
    #     f.write(str(dict_question))
    #     f.close()
    #     print(dict_question)


def check():
    # f = open('./DataBase/DataBase.txt', 'rb')
    # dict_question = pickle.load(f)
    # dict_question = pickle.load(f)
    # #print(dict_question)
    # pprint.pprint(dict_question)
    f = open('./DataBase/DataBase.txt', 'r')
    dict_question = eval(f.read())
    print(dict_question)
    return dict_question
    f.close()


def find(words):
    global dict_question
    dict_question = check()
    result = ""
    try:
        result = dict_question[words]
        return True
    except Exception as err:
        return False


if __name__ == '__main__':
    # add()
    # print(find('aff'))
    check()
