# coding:utf-8
import codecs


class DataOutput(object):
    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_question(self):
        fout = codecs.open('baiKeTitle.txt', 'a', encoding='utf-8')
        for data in self.datas:
            fout.write(data['title'] + '\n')
            # self.datas.remove(data)
        fout.close()

    def output_answer(self):
        fout = codecs.open('baiKeSummary.txt', 'a', encoding='utf-8')
        for data in self.datas:

            fout.write(data['summary']+'\n')
            # self.datas.remove(data)
        fout.close()
