# COMP 202 A3
# Name GATTUOCH KUON
# ID:260-877-635

from single_winner import *

################################################################################

def votes_needed_to_win(ballots, num_winners):
    '''
    (list, int)-> int
    want to return the number of votes a candidate need to win using the Droop Quota.
    >>> votes_needed_to_win([{'CPC':3, 'NDP':5}, {'NDP':2, 'CPC':4}, {'CPC':3, 'NDP':5}], 1)
    2
    >>> votes_needed_to_win(['g']*20, 2)
    7
    '''
    #the length of the ballots represent total votes which i divide number of winners plus one
    # add the floor division(// rounds the decimal down) of it to one
    return (len(ballots)//(num_winners + 1)) + 1


def has_votes_needed(result, votes_needed):
    '''
    (dict, int)-> bool
    We want to return a Boolean whether a candidate with most votes in the election,
    has at least votes needed.
    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
    True
    >>> has_votes_needed({'NDP': 5, 'LIBERAL': 8}, 6)
    True
    >>> has_votes_needed({'NDP': 2, 'LIBERAL': 3}, 4)
    False
    '''
    # if my get_winner value in the helpers function is greater or equal to votes
    # -needed i return true else i return false
    if (result):
        return result[get_winner(result)] >= votes_needed
    else:
        return False
 ################################################################################


def eliminate_candidate(ballots, to_eliminate):
    '''
    (list)-> list
    want to return a list of ranked ballots where all the candidates,
    in to_eliminate have been removed.
    If all the candidates on the ballot have eliminated the return an
    empty list.
    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]
    '''
    new_ballots = []
    #loop through each ballot in the ballots
    for ballot in ballots:
        new_ballot =[]
        #loop through each cadidate in each ballot.
        for candidate in ballot:
            if candidate not in to_eliminate:
               new_ballot.append(candidate) # if the candidate has not been eliminated, we append it to the ballot.
        new_ballots.append(new_ballot) #append all the ballot into the main ballots
    return new_ballots

    

 ################################################################################


def count_irv(ballots):
    '''
    (list)-> dict
    We want to get the winner and the number of votes the candidate get after counting with Instant Run-off Votes.
    >>> count_irv([['NDP'],['LIBERAL','NDP'],['BLOC', 'GREEN', 'NDP'], ['LIBERAL', 'CPC'], ['LIBERAL', 'GREEN']])
    {'NDP': 1, 'LIBERAL': 3, 'BLOC': 1, 'GREEN': 0, 'CPC': 0}
    >>> count_irv([['LIBERAL', 'NDP'], ['NDP', 'GREEN','LIBERAL'], ['LIBERAL', 'GREEN']])
    {'LIBERAL': 2, 'NDP': 1, 'GREEN': 0}
    >>> count_irv([['LIBERAL', 'NDP'], ['GREEN', 'NDP'], ['LIBERAL', 'GREEN', 'CPC'], ['LIBERAL', 'CPC' , 'GREEN']])
    {'LIBERAL': 3, 'NDP': 0, 'GREEN': 1, 'CPC': 0}
    '''
#   count first winners
#   if winner has majority we return the winner
#   if not we eliminate the last place and make the second place candidate the first choice
    winner_results = count_first_choices(ballots)
    winner_found = False # to keep track of While Loop to avoid infinite loop
    while not winner_found:
        if has_votes_needed(winner_results, votes_needed_to_win(ballots,1)): 
            winner_found = True
            return winner_results
        #if we have no winner yet, we remove the last place and go back to the first statement execution
        else:
            last_place_remove = last_place(winner_results)
            #update the ballots after the last place is remove
            ballots = eliminate_candidate(ballots,last_place_remove)


################################################################################

if __name__ == '__main__':
    doctest.testmod()
