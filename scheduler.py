"""
Scheduler

Prompt
Plaid is a financial data aggregator. End users connect their bank accounts to the Plaid platform, Plaid aggregates their financial data, and allows authorized apps to access that data.

Guaranteeing data freshness

Account Identifiers: Username + Bank Name

Each bank has a set update interval specified in seconds
e.g if "Chase" has an update interval of "5" if a user was updated at `T=0` then they should be updated again at `T=5`



"""

# Milestone 1 
# Given the following API that adds accounts for a given bank and it's update interval
# add_bank(bank, accounts, interval) -> None
# accounts_to_update(timestamp) => Map<Bank, Array<Account>>
# Timestamp starts at 0

#The solution at this point should simply consist of looping over all banks on every call to `accounts_to_update`, and returning a concatenated list of accounts of all banks for which`timestamp % bank.update_interval == 0

def scheduler_1(timestamp):
    # accounts_to_update should return a bank and a list of corresponding accounts {'chase': ['username1', 'username2', 'username3']}
    #Suppose we have two banks, “Chase” and “Wells Fargo”. “Chase” has an update interval of 10 seconds, and “Wells Fargo” 
    valid_banks = ['Chase', "Wells Fargo"]

    # assuming the count starts at 0
    bank_accounts = accounts_to_update(timestamp)
    for bank in bank_accounts:
        if timestamp % bank.update_interval == 0:    
            for valid_bank in valid_banks:
                accounts = []
                accounts.extend(valid_bank)
                add_bank(bank, accounts, interval)


# Milestone 2
# Update the implementation from using an Array to using a queue or deque

# This system will be used to generate outgoing traffic to banks (that is, load on bank servers)
# The current implementation takes all the traffic and loops through all the banks and accounts and updates everything at the same time
# Ideally traffic should be split or staggered

        

def scheduler_2(timestamp):
    valid_banks = [{'Chase': 10}, {"Wells Fargo": 5}]
    # dequeue includes a popleft() function to remove items from the front of the list
    partition_1 = []
    partition_2 = []
    # assuming the count starts at 0
    bank_accounts = accounts_to_update(timestamp)
    for bank in bank_accounts:
        if timestamp % bank.update_interval == 0:    
            for valid_bank in valid_banks:
                accounts = bank.get(valid_bank)
                partition_1 = accounts[::2] # slice beginning and every other 2 accounts
                partition_2 = accounts[1::2] # slice starting at index 1 and get every other 2 accounts
                add_bank(bank=bank, accounts=partition_1, interval=valid_bank[bank])
                add_bank(bank=bank, accounts=partition_2, interval=(valid_bank[bank] + 1))

    return pq

# More accounts are added? Further partition?
def scheduler_3(timestamp):
    valid_banks = ['Chase', "Wells Fargo"]
    # dequeue includes a popleft() function to remove items from the front of the list
    partition_1 = []
    partition_2 = []
    partition_3 = []
    # assuming the count starts at 0
    bank_accounts = accounts_to_update(timestamp)
    for bank in bank_accounts:
        if timestamp % bank.update_interval == 0:    
            for valid_bank in valid_banks:
                accounts = bank.get(valid_bank)
                partition_1 = accounts[::3] # slice beginning and every other 3 accounts
                partition_2 = accounts[1::3] # slice starting at index 1 and get every other 3 accounts
                partition_3 = accounts[2::3] # slice starting at index 1 and get every other 3 accounts
                add_bank(bank=bank, accounts=partition_1, interval=valid_bank[bank])
                add_bank(bank=bank, accounts=partition_2, interval=(valid_bank[bank] + 1))
                add_bank(bank=bank, accounts=partition_3, interval=(valid_bank[bank] + 2))
    return None

# More accounts are added? Further partition?
# New API functionality // Updates the given’s interval. Returns nothing. update_interval(bank, interval) => void
# add a updated_at timestamp (it has to have one)

# Does 
def scheduler_4(timestamp):
    valid_banks = ['Chase', "Wells Fargo"]
    # dequeue includes a popleft() function to remove items from the front of the list
    partition_1 = []
    partition_2 = []
    partition_3 = []
    # assuming the count starts at 0
    bank_accounts = accounts_to_update(timestamp)
    for bank in bank_accounts:
        if timestamp % bank.update_interval == 0:    
            for valid_bank in valid_banks:
                accounts = bank.get(valid_bank)
                partition_1 = accounts[::3] # slice beginning and every other 3 accounts
                partition_2 = accounts[1::3] # slice starting at index 1 and get every other 3 accounts
                partition_3 = accounts[2::3] # slice starting at index 1 and get every other 3 accounts
                pq.put({valid_bank: partition_1}, 1)
                pq.put({valid_bank: partition_2}, 2)
                pq.put({valid_bank: partition_3}, 3) 

    return pq


if __name__ == "__main__":
    # test valid banks with several accounts, does it create a partitioned Priority Queue

    # test valid banks with several accounts

