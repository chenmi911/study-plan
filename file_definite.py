from data_definite import Record
import json

class FileReader:

    def read_data(self) -> list[Record]:
        pass


class TextReader(FileReader):

    def __init__(self, path):
        self.path = path


    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"],data_dict["money"], data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_data = TextReader("D:/python练习文件/一月.txt")
    list1 = text_file_data.read_data()
    json_file_reader = JsonFileReader("D:/python练习文件/二月.json")
    list2 = json_file_reader.read_data()

    for i in list1:
        print(i)
    for i in list2:
        print(i)
