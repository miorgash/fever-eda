# -*- coding: utf-8 -*-

def get_unique_evidences(nested_list):
    ls = [innest[-2:] for inner in nested_list for innest in inner]
    ls = [tuple(inner) for inner in ls]
    ls = list(set(ls))
        
    return ls
