#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator(tag='h1'):
    def decorator_func(func):
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return f'<{tag}>{value}</{tag}>'

        
        return wrapper

    return decorator_func


@decorator(tag='div')
def some_func(string):
    return string.lower()


if __name__ == "__main__":
    print(some_func(input('Введите строку: ')))
