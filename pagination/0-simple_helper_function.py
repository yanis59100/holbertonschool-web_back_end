#!/usr/bin/env python3
'''Pagination file'''


def index_range(page: int, page_size: int) -> tuple:
    '''index range'''
    return ((page * page_size - page_size), (page * page_size))
