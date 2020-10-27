import os

base_path = os.path.dirname(os.path.abspath(__file__))

def get_tushare_token():
    return open(os.path.join(base_path, ".tushare_token")).read()


if __name__ == '__main__':
    print(get_tushare_token())
    