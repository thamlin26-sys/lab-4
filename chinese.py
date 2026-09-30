def load_chinese_file(filename):
    f = open(filename, 'br')
    bs = f.read()
    try:
        text = bs.decode('gb2312')
        print('gb2312')
    except UnicodeDecodeError:
        text = bs.decode('big5')
        print('big5')
    return text