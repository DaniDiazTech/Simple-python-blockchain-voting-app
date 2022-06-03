from voting import Candidate, Voter, Block, Blockchain

def main():
    print("BLOCKCHAIN VOTING SYSTEM")

    print("Preparing candidates ...\n")

    c1 = Candidate("Jennifer", 21, "The best outta the best")
    c2 = Candidate("Oscar", 27, "The unrealistic one", ["Make a pool", "No more homework"])
    c3 = Candidate("Kevin", 24, "Probably the best option", ["Implement a better academic criteria", "Give tutorships"])
    blank = Candidate("Protest vote")


    candidates = [c1, c2, c3, blank]
    
    d = {}
    for i, c in enumerate(candidates, 1):
        d[i] = c
        print(f"{i} -- {str(c)}")
    
    print("\n\n")

    blockchain = Blockchain()

    i = 1
    while i not in ["quit", "stop"]:
        name = input("Please introduce your name")
        id = input("Now your ID")
        vote = None
        while True:
            try:
                vote = int(input("Your choice from the above")) 
                if vote in d:
                    vote = d[vote]
                else:
                    continue
            except:
                print("Try a valid option from above")

        voter = Voter(name, id, vote)
        print("\n\n")
        blockchain.add_block(Block(datetime.now(), voter))
        
        i = input("To stop voting, type 'stop' or 'quit'")

    blockchain.display_chain()

main()