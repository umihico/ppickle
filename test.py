import ppickle
import json
import pickle
import collections

filenames = {
    "ppickle": 'testdata/data.ppickle',
    "pickle": 'testdata/data.pickle',
    "json": 'testdata/data.json',
}


def write_test(data):
    ppickle.dump(filenames['ppickle'], data)
    with open(filenames['pickle'], 'wb') as f:
        pickle.dump(data, f)
    with open(filenames['json'], 'w') as f:
        json.dump(data, f)


def load_test(data):
    ppickled_data = ppickle.load(filenames['ppickle'])
    with open(filenames['pickle'], 'rb') as f:
        pickled_data = pickle.load(f)
    with open(filenames['json'], 'r', encoding='utf-8',) as f:
        jsoned_data = json.load(f)
    print('ppickle', data == ppickled_data)
    print('pickle', data == pickled_data)
    print('json', data == jsoned_data)


def test():
    testdata1 = {'ar': 'عربى', 'en': 'english', 'jp': '日本語', 'ko': '한국어'}
    testdata2 = list(testdata1.items())
    testdata3 = collections.OrderedDict()  # fails
    for k, v in testdata2:
        testdata3[k] = v
    testdatas = [testdata1, testdata2, testdata3]
    for testdata in testdatas:
        write_test(testdata)
        load_test(testdata)


if __name__ == '__main__':
    test()
