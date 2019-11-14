# COMP 202 A3
# Name: GATTUOCH KUON
# Student ID:260-877-635

from a3_helpers import *


def count_plurality(ballots):
    '''
    (list)-> dict
    want to count how many votes each candidate get given ballots list
    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL']) 
    {'LIBERAL': 3, 'NDP': 1}
    >>> count_plurality(['LIBERAL', 'BLOC', 'LIBERAL', 'NDP', 'BLOC', 'LIBERAL', 'BLOC'])
    {'LIBERAL': 3, 'BLOC': 3, 'NDP': 1}
    '''
    votes = {} # created an empty dictionary
    #iterate through the elements of the ballots
    for element in ballots:
        if element in votes:
            votes[element] += 1 # if there`s an already added element increase the count
        else:
            votes[element] = 1 # initiatlize the count for elements appearing for first time
    return votes

def count_approval(ballots):
    '''
    (list)-> dict
    want to count how many each candidate get given ballots list inside a list
    >>> count_approval([ ['LIBERAL', 'NDP', 'BLOC'], ['NDP'], ['NDP', 'GREEN', 'BLOC']] )
    {'LIBERAL': 1, 'NDP': 3, 'BLOC': 2, 'GREEN': 1}
    >>> count_approval([ ['LIBERAL','LIBERAL', 'NDP'], ['NDP', 'GREEN'], ['NDP', 'GREEN', 'BLOC']] )
    {'LIBERAL': 2, 'NDP': 3, 'GREEN': 2, 'BLOC': 1}
    '''
    votes = {}
    for element in flatten_lists(ballots): #call and iterate through the flatten_list
        if element in votes: # i check if my element is already in the dict i increase my count
            votes[element] += 1
        else:
            votes[element] = 1 # if not in votes set the value to 1
    
    return votes

def count_rated(ballots):
    '''
    (list)-> dict
    Candidates given ratings out of 5 on ballots and we want to sum up the scores each candidate
    was given.
    We then return a dictionary with the total ratings.
    >>> count_rated([{'LIBERAL': 5, 'NDP':2}, {'NDP':4, 'GREEN':5, 'LIBERAL':3}])
    {'LIBERAL': 8, 'NDP': 6, 'GREEN': 5}
    >>> count_rated([{'LIBERAL': 5, 'NDP':2}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    '''
    new_dict = {}
    for l in ballots: # loop through dicts inside the list
        for key in l:
            value = l[key] # want the value at the key 
            if key in new_dict:
                new_dict[key] += value # if my key already exist, i add the values
            else:
                new_dict[key] = value # if no key found append my new value
    return new_dict

def count_first_choices(ballots):
    '''
    (list)-> dict
    We want to return a dictionary storing ballots from which a party was first choice
    >>> count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']]) 
    {'NDP': 2, 'LIBERAL': 0, 'GREEN': 1, 'BLOC': 0}
    >>> count_first_choices([['LIBERAL', 'NDP'], ['GREEN', 'NDP'], ['NDP', 'BLOC']])
    {'LIBERAL': 1, 'NDP': 1, 'GREEN': 1, 'BLOC': 0}
    '''
    new_dict = {}
    for l in ballots: # loop through the list items.
        key = l[0] # i want to get key as the first choice
        if key not in new_dict:
            new_dict[key] = 1 # if no key found, i assign my value 1
        else:
            new_dict[key] += 1 # if i find the key, i increase my count
        for subl in l: 
            if subl not in new_dict: #if a key in the sublist is not in the dicts i assign it value 0.
                new_dict[subl] = 0
    return new_dict

if __name__ == '__main__':
   doctest.testmod()
