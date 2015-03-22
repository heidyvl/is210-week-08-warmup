#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""
from decimal import Decimal


def lexicographics(to_analyze):
    """Retunrs max, min and average"""
    temp = []
    i = 0
    number = to_analyze.split('\n')
    for number[i] in number:
        temp.append(len(number[i].split()))
        i += 1
    return max(temp), min(temp), Decimal(sum(temp))/Decimal(len(temp))
