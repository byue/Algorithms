from collections import deque

def get_stable_matches(proposer_prefs, receiver_prefs):
    """Returns a list of (proposer, receiver) matches given ordered proposer
       and receiver preferences, where index 0 of preferences list is most preferred.
       Runtime is O(N^2) where N is the number of receivers and the number of proposers.
    """
    # input validation
    for receivers in proposer_prefs.values():
        if set(receivers) != receiver_prefs.keys():
            raise ValueError("Receiver Preference list of proposers must include all receivers")

    for proposers in receiver_prefs.values():
        if set(proposers) != proposer_prefs.keys():
            raise ValueError("Proposer Preference list of receivers must include all proposers")

    engagements = {}
    proposer_rank = {}
    
    # initialize free proposers, initially all proposers
    free_proposers = deque([p for p in proposer_prefs.keys()])

    # initialize index of next receiver for each proposer to 0
    next_receiver = {proposer: 0 for proposer in proposer_prefs.keys()}

    # receiver to proposer to proposer index (rank), needed to speed up rank comparisions
    for receiver, preferences in receiver_prefs.items():
        proposer_rank[receiver] = {proposer: i for i, proposer in enumerate(preferences)}
    
    while free_proposers:
        # get the next free proposer
        new_proposer = free_proposers.popleft()

        # get next receiver proposer has not proposed to yet and increment next receiver
        receiver = proposer_prefs[new_proposer][next_receiver[new_proposer]]
        next_receiver[new_proposer] += 1

        if receiver not in engagements:
            # tenatively match new proposer with receiver if receiver is not engaged
            engagements[receiver] = new_proposer
        elif proposer_rank[receiver][new_proposer] < proposer_rank[receiver][engagements[receiver]]:
            # new proposer is more favored by receiver than old proposer, engage receiver with new proposer
            # and free old proposer
            old_proposer = engagements[receiver]
            engagements[receiver] = new_proposer
            free_proposers.append(old_proposer)
        else:
            # receiver rejects new proposer, new proposer remains free
            free_proposers.append(new_proposer)

    return set([(proposer, receiver) for receiver, proposer in engagements.items()])