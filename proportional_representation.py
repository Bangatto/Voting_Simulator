# COMP 202 A3
# Name: GATTUOCH KUON
# Student ID: 260-877-635

from instant_run_off import *

################################################################################

def irv_to_stv_ballot(ballots, num_winners):
    '''
    (list, int)-> list
    Want to replace each party with the number of winners from that party 
    starting from 0.
    >>> irv_to_stv_ballot([['NDP', 'CPC'], ['GREEN']], 3)
    [['NDP0', 'NDP1', 'NDP2', 'CPC0', 'CPC1', 'CPC2'], ['GREEN0', 'GREEN1', 'GREEN2']]
    >>> irv_to_stv_ballot([['LIBERAL', 'BLOC'], ['NDP']], 2)
    [['LIBERAL0', 'LIBERAL1', 'BLOC0', 'BLOC1'], ['NDP0', 'NDP1']]
    >>> irv_to_stv_ballot([['GREEN', 'CPC'], ['LIBERAL']], 4)
    [['GREEN0', 'GREEN1', 'GREEN2', 'GREEN3', 'CPC0', 'CPC1', 'CPC2', 'CPC3'], ['LIBERAL0', 'LIBERAL1', 'LIBERAL2', 'LIBERAL3']]
    '''
    ballots_list = []
    for ballot in ballots: # i loop through the list of ranked ballots 
        party_list = []
        for party in ballot: # i loop through each ballot to get individual party
            for index in range(num_winners):
                party_list.append(party + str(index)) # i concaternate the index at the end of each party
        ballots_list.append(party_list) # i append back the party list into my ballot list
    return ballots_list

################################################################################


def eliminate_n_ballots_for(ballots, to_eliminate, n):
    '''(lst, str) -> lst
    Remove n of the ballots in ballots where the first choice is for the candidate to_eliminate.

    Provided to students. Do not edit.

    >>> ballots = [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 2)
    [['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3', 'GREEN1'], 5)
    [['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> b = [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    >>> eliminate_n_ballots_for(b, ['GREEN1'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    '''
    quota = n
    new_ballots = []
    elims = 0
    for i,b in enumerate(ballots):
        if (elims >= quota) or  (len(b) > 0 and b[0] not in to_eliminate):
            new_ballots.append(b)
        else:
            elims += 1
    return new_ballots



def stv_vote_results(ballots, num_winners):
    '''(lst of list, int) -> dict

    From the ballots, elect num_winners many candidates using Single-Transferable Vote
    with Droop Quota. Return how many votes each candidate has at the end of all transfers.
    
    Provided to students. Do not edit.

    >>> random.seed(3) # make the random tie-break consistent
    >>> g = ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1']
    >>> n = ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 2, 'NDP3': 0}
    >>> random.seed(0)
    >>> #pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    #{'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 0, 'NDP3': 0}
    >>> green = ['GREEN', 'NDP', 'BLOC', 'LIBERAL', 'CPC']
    >>> ndp = ['NDP', 'GREEN', 'BLOC', 'LIBERAL', 'CPC']
    >>> liberal = ['LIBERAL', 'CPC', 'GREEN', 'NDP', 'BLOC']
    >>> cpc = ['CPC', 'NDP', 'LIBERAL', 'BLOC', 'GREEN']
    >>> bloc = ['BLOC', 'NDP', 'GREEN', 'CPC', 'LIBERAL']
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 2))
    {'BLOC': 32, 'CPC': 34, 'GREEN': 0, 'LIBERAL': 0, 'NDP': 34}
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 3))
    {'BLOC': 26, 'CPC': 26, 'GREEN': 0, 'LIBERAL': 22, 'NDP': 26}
    '''
    quota = votes_needed_to_win(ballots, num_winners)
    
    to_eliminate = []
    result = {}
    final_result = {}

    for i in range(num_winners):
        # start off with quasi-IRV
        result = count_first_choices(ballots)

        while (not has_votes_needed(result, quota)) and len(result) > 0:
            to_eliminate.append( last_place(result) ) 
            ballots = eliminate_candidate(ballots, to_eliminate)
            result = count_first_choices(ballots)

        # but now with the winner, reallocate ballots above quota and keep going
        winner = get_winner(result)
        if winner:
            final_result[winner] = quota # winner only needs quota many votes
            ballots = eliminate_n_ballots_for(ballots, final_result.keys(), quota)
            ballots = eliminate_candidate(ballots, final_result.keys())
            result = count_first_choices(ballots)

    # remember the candidates we eliminated, their count should be 0
    for candidate in to_eliminate:
        final_result[candidate] = 0
    final_result.update(result)
    return final_result


 ###############################################################################


def count_stv(ballots, num_winners):
    '''
    (list, int)-> list
    >>> random.seed(0) # make the random tie-break consistent 
    >>> g = ['GREEN', 'NDP', 'BLOC'] 
    >>> n = ['NDP', 'GREEN', 'BLOC'] 
    >>> pr_dict(count_stv([g]*5 + [n]*3, 4))
    {'BLOC': 0, 'GREEN': 3, 'NDP': 1}
    '''
    #want to convert irv votes to stv then the results counted through stv count
    stv_votes = irv_to_stv_ballot(ballots, num_winners)
    counted_votes = stv_vote_results(stv_votes, num_winners)
    votes_needed = votes_needed_to_win(ballots,num_winners)
    winner = []
    loser = []
    for key in counted_votes: #loop through the counted results
        if counted_votes[key] == votes_needed: # if the result is equal to the quota, i append the key
            winner.append(key)
        elif counted_votes[key] < votes_needed: # if the results is less than the quota, the i append it as a loser
            loser.append(key)
        else:
            continue
    winner_candidate =[] # i want to get a list of winners only
    for wc in winner:
        winner_candidate.append(wc[:-1])
    loser_candidate = []  # i want to get losers only
    for ls in loser:
        loser_candidate.append(ls[:-1])
    loser_last_place = {} # Those at last place only
    for lser in loser_candidate:
        loser_last_place[lser] = 0
    return add_dicts(count_plurality(winner_candidate), loser_last_place)

  ################################################################################


def count_SL(results, num_winners):
    '''
    (dict, int)-> dict
    want to return the number of seats each party won using the  Sainte-Lagu¨e Method.
    >>> count_SL({'LIBERAL':100000, 'GREEN': 80000, 'NDP':30000, 'BLOC':20000}, 8) 
    {'LIBERAL': 3, 'GREEN': 3, 'NDP': 1, 'BLOC': 1}
    '''
    # get the total votes each party got
    # assign votes according to the popularity the party with Max get the highest number of vote
    # get_winner to select winner each time
    # loop through until all the seats have been assigned.
    seats_won = {}
    for party in results.keys():
        seats_won[party] = 0
    while num_winners > 0:
        #calculate quotient for each party
        #find the party with max quotient
        max_quotient = 0
        seat_allocated_to = ""
        for party in seats_won:
            quotient = (results[party])//((2*seats_won[party]) + 1)
            if quotient > max_quotient:
                seat_allocated_to = party
                max_quotient = quotient
        #Allocate seat to party with max
        seats_won[seat_allocated_to] +=1
        #Decrease number of seats available
        num_winners -=1
    return seats_won
    


################################################################################


if __name__ == '__main__':
    doctest.testmod()