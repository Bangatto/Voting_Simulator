# COMP 202 A3 Part 1
# Name: GATTUOCH KUON
# Student ID: 260-877-635

import doctest
import random

def flatten_lists(nested):
    '''
    (list)-> list
    we want to replace the lists with their values and return the new version.
    >>> flatten_lists([[1, 2],[3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> flatten_lists([[1,5],4])
    [1, 5, 4]
    '''
    new_list=[]
    for elem in nested:
        if type(elem) == list: # i check if my nested list is made of list only
           for subelem in elem: # knowing it is made up of list only, i loop through the sub-elements of the elements
               new_list.append(subelem)
        else:
            new_list.append(elem) # i append the element if it`s of  type string or integer
    return new_list


def flatten_dict(d):
    '''
    (dict)-> list
    want to make a list out of a dictionary and return the keys repeated as its value
    >>> flatten_dict ({'LIBERAL':4})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL']
    >>> flatten_dict ({'NDP':2, 'LIBERAL':1, 'GREEN':3})
    ['NDP', 'NDP', 'LIBERAL', 'GREEN', 'GREEN', 'GREEN']
    '''
    new_list=[]
    #iterate through the keys of the dictionary
    for key in d: 
        for i in range(d[key]):# Want the number of keys in the dict and append the keys each time i iterate.
            new_list.append(key)
    return new_list

def add_dicts(d1, d2):
    '''
    (dict)-> dict
    want to merge two dictionaries and add theirs values if the key is the same
    and return the updated dict
    >>> add_dicts({'1': 4, '0': 1}, {'1': 4, '2': 3})
    {'1': 8, '0': 1, '2': 3}
    >>> add_dicts({'3':5,'2':2}, {'1':4})
    {'3': 5, '2': 2, '1': 4}
    '''
    new_dict = d1.copy() # i copied all the dict1 into a an empty new dict
    for key, val in d2.items(): # i loop through to get both the key and the value
        if key in d1: # if my key is in d1, i added the key values
            new_dict[key] += val
        else:
            new_dict[key]= val # if the key is not in d1, i assign it the new value

    return new_dict


def get_all_candidates(ballots):
    '''
    (list)-> list
    Return all the unique strings in the list and its nested content
    >>> get_all_candidates([{'Green': 3, 'NDP':5}, {'BLOC':7},['liberal','NDP'] ])
    ['Green', 'NDP', 'BLOC', 'liberal']
    >>> get_all_candidates([{'liberal':4, 'NDP':5}, ['liberal','NDP'] ])
    ['liberal', 'NDP']
    '''
    new_dict =  {}
    #iterate through the lists in ballots
    for element in ballots:
        if type(element) == dict: #check if the inside the list is a dict we assifn the dict the elements
            dict_to_add = element
        elif type(element)== list: # check if its a list of list, assign the key
            dict_to_add = dict.fromkeys(element, 1)
        else:
            dict_to_add = {element,1}
        new_dict = add_dicts(new_dict, dict_to_add)
    return list(new_dict.keys())



###################################################### winner/loser

def get_candidate_by_place(result, func):
    '''
    (dict)-> str
    Want to evaluate the function by its value and return the key associated to it.
    if we get the max or min value, we return its key and break a tie randomly.
    >>> result = {'LIBERAL':4, 'NDP':7, 'CPC':6, 'GREEN':4} 
    >>> random.seed(0)
    >>> get_candidate_by_place(result, min)
    'LIBERAL'
    >>> random.seed(1) 
    >>> get_candidate_by_place(result, min)
    'GREEN'
    >>> random.seed(12) 
    >>> get_candidate_by_place(result, max)
    'NDP'
    '''
    if(result):
        val = func(result.values()) # pass in the value into the func
        keys = list(result.keys()) # convert the dict into list
        random.shuffle(keys)
        for key in keys:
            #the function return either max or min and the key is return
            if val == result[key]:
                return key
    else:
        return ""
def get_winner(result):
    '''
    (dict)-> str
    We want to get the greatest value in the dict and return the key associated to it.
    if there is a tie break them randomly.
    >>> get_winner({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0}) 
    'NDP'
    >>> get_winner({'GREEN': 2, 'LIBERAL': 3, 'NDP': 4, 'BLOC': 9}) 
    'BLOC'
    '''
    # pass in the result and max to get the winner
    return get_candidate_by_place(result, max) 

def last_place(result):
    '''
    (dict)-> str
    We want to get the lowest value in the dict and return the key associated to it.
    if there is a tie break them randomly.
    >>> last_place({'NDP': 2, 'GREEN': 1, 'BLOC': 0, 'LIBERAL': 0,}) 
    'BLOC'
    >>> last_place({'GREEN': 2, 'LIBERAL': 3, 'NDP': 0, 'BLOC': 9}) 
    'NDP'
    '''
    # pass in result and min to gte the last place
    return get_candidate_by_place(result, min)


###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
