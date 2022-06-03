from voting import Candidate, Voter, Block, Blockchain


def main():
    print("BLOCKCHAIN VOTING SYSTEM")

    print("Preparing candidates")

    c1 = Candidate("Jennifer", 21, "The best outta the best")
    c2 = Candidate("Oscar", 27, "The unrealistic one", ["Make a pool"], ["No more homework"])
    c3 = Candidate("Kevin", 24, "Probably the best option", ["Implement a better academic criteria", "Give tutorships"])
    blank = Candidate("Protest vote")


    candidates = [c1, c2, c3, blank]

    for c in candidates:
        print(c)

main()