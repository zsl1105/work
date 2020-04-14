"""
python 典型例题，经典集锦！！！！
"""

"""
1,写一个单例模式：单例模式是一种常见的软件设计模式，该模式主要目的确保该类中只有一个实例存在
"""


# 装饰器方法实现
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton
