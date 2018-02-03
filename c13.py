# -*- coding: utf-8 -*-


class CountUpDict:

    def __init__(self, filepath):
        self.filepath = filepath
        self.words = {}

        self.__make_dict(filepath)

    def __make_dict(self, filepath):
        f = open(filepath)
        line = f.readline()  # 1行を文字列として読み込む(改行文字も含まれる)

        while line:
            for word in line.split():
                if word in self.words:
                    self.words[word] += 1
                else:
                    self.words[word] = 1
            line = f.readline()
            f.close


if __name__ == '__main__':
    d = CountUpDict('test.txt')
    print(d.words)
