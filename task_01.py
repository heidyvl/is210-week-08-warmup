#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


def fibonacci(maxint):
    """Fibonacci"""
    listfib = [0]
    numa, numb = 0, 1
    while numb < maxint:
        listfib.append(numb)
        numa, numb = numb, numa+numb
    return listfib
