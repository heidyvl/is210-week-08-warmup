#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""
from decimal import Decimal


def lexicographics(to_analyze):
    """Retunrs max, min and average"""
    temp = []
    number = to_analyze.split('\n')
    for item in number:
        temp.append(len(item.split()))
    return max(temp), min(temp), Decimal(sum(temp))/Decimal(len(temp))
