import os, re, time


def absp(path: str):
    if path[0] != '/':
        path = f'/{path}'
    return f'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}{path}'

def containsChinese(elem):
    return bool(re.search(r'[\u4e00-\u9fff]+', elem))
