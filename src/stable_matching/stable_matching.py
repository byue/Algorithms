def get_stable_matches(proposer_to_preferences, receiver_to_preferences):
    """Returns a list of (proposer, receiver) matches given ordered proposer
       and receiver preferences, where index 0 of preferences list is most preferred.
       Runtime is O(N^2) where N is the number of receivers and the number of proposers.
    """
    proposer_matches = {}
    receiver_matches = {}

    # Receivers that proposer has already attempted to propose to.
    proposals = {proposer: set() for proposer in proposer_to_preferences.keys()}

    # Receivers and proposers that have not been matched
    free_proposers = {proposer for proposer in proposer_to_preferences.keys()}
    free_receivers = {receiver for receiver in receiver_to_preferences.keys()}

    # O(N^2): Precompute proposer to ranking for a receiver for faster ranking lookups.
    receiver_to_proposer_rankings = {}
    for receiver, proposers in receiver_to_preferences.items():
        receiver_to_proposer_rankings[receiver] = {proposer: rank for rank, proposer in enumerate(proposers)}

    # O(N^2): For each of N proposers have to look through N receivers to find candidate receiver.
    while free_proposers:
        candidate_proposer = next(iter(free_proposers))
        proposed_receivers = proposals[candidate_proposer]
        proposer_preferences = proposer_to_preferences[candidate_proposer]
        candidate_receiver = next(filter(lambda receiver: receiver not in proposed_receivers, proposer_preferences), None)
        proposer_ranking = receiver_to_proposer_rankings[candidate_receiver]

        proposed_receivers.add(candidate_receiver)
        if candidate_receiver in free_receivers:
            # Case 1: Receiver and proposer have not been matched before and matches.
            proposer_matches[candidate_proposer] = candidate_receiver
            receiver_matches[candidate_receiver] = candidate_proposer
            free_proposers.remove(candidate_proposer)
            free_receivers.remove(candidate_receiver)
        else:
            # Case 2: Receiver has been matched before but prefers new proposer to old proposer.
            # Receiver unmatches with older proposer and matches with new proposer.
            old_proposer = receiver_matches[candidate_receiver]
            if proposer_ranking[candidate_proposer] < proposer_ranking[old_proposer]:
                old_proposer = receiver_matches[candidate_receiver]
                proposer_matches[candidate_proposer] = candidate_receiver
                receiver_matches[candidate_receiver] = candidate_proposer
                free_proposers.remove(candidate_proposer)
                free_proposers.add(old_proposer)

    return {(proposer, receiver) for proposer, receiver in proposer_matches.items()}
