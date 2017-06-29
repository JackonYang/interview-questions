# -*- coding: utf-8 -*-
"""
补全 cache 函数。实现功能：

把计算过的结果，缓存在 `_cache_db` 中.
第二次调用时，读取缓存中的数据，无需重复执行 add 函数。

"""
import hashlib

_cache_db = dict()


def md5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()


def cache(f):
    pass


@cache
def add(a, b):
    return a + b


if __name__ == '__main__':
    assert add(3, 4) == 7
    assert add(3, 4) == 7
    assert add(8, 4) == 12
    assert add(4, 8) == 12
    assert add(8, 4) == 12
