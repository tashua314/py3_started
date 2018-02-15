# -*- coding: utf-8 -*-


class CountUpDict:

    def __init__(self, filepath):
        self.__filepath = filepath
        self.__words = {}
        self.__make_dict()
        print(dir(self))

    @property
    def words(self):
        return self.__words

    # 辞書作成
    def __make_dict(self):
        f = open(self.__filepath)

        for line in self.__readline(f):
            for word in line.split():
                if word in self.words:
                    self.__words[word] += 1
                else:
                    self.__words[word] = 1

    # ファイルを1行読む
    def __readline(self, f):
        while True:
            line = f.readline()  # 1行を文字列として読み込む(改行文字も含まれる)
            if not line:
                f.close
                break
            yield line


if __name__ == '__main__':
    d = CountUpDict('test.txt')
    print(d.words)
