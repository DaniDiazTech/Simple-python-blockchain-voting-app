# Timestamp
import datetime

# Calc the hash
import hashlib


def hash_wrapper(self, data):
    return hashlib.sha256(data.encode()).hexdigest()

class Candidate:
    def __init__(self, name: str, age = None, description = None, proposals = None):
        self.name = name
        self.age = age
        self.description = description
        self.proposals = proposals

    def __str__(self):
        s = self.name

        if self.age:
            s +=  f", {self.age} y/o"
        
        if self.description:
            s += f" {self.description}"

        if self.proposals:
            s += f", {' '.join(self.proposals)}"
        else:
            s += " No proposals"


        return s


class Voter:
    def __init__(self, name: str, id_: int, choice):
        self.name = name
        self.id  = id_
        self.choice = choice

    def __str__(self):
        return self.name

class Block:
    def __init__(self, timestamp, voter: Voter, previous_block_hash=''):
        
        self.nonce = 0
        
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.voter = voter
        self.block_data = f"{self.nonce} - {self.timestamp} - {self.voter.name} {self.voter.id} {self.vote.choice.name} - {self.previous_block_hash}"
        self.block_hash = self.calculate_hash

    # Proof of work
    # Difficulty less than 256
    def mine_block(self, difficulty):
        while(self.hash[:difficulty] != str('').zfill(difficulty)):
            self.nonce += 1
            self.hash = self.calculate_hash(self.block_data)
    
    @property
    def calculate_hash(self):
        return hash_wrapper(self.block_data)

    def __str__(self):
        s = f"Block Nonce: {self.nonce}\n"
        s += "Voter info: " + str(self.voter.name)+"\n"
        s += "Old hash: " + str(self.previous_block_hash)+"\n"
        s += "New hash :" + str(self.block_hash)+"\n"

        return s






genesis_candidate = Candidate('')
genesis_voter = Voter('', '', genesis_candidate)

class Blockchain:
    def __init__(self):
        self.chain = [Block(0, genesis_voter, datetime.now()),]
        self.difficulty = 4

    def add_block(self, new_block):
        new_block.previous_block_hash = self.last_block.block_hash

        # Appends new block to the chain
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    # Validates chain
    def validate_chain(self):
        
        for i in range(1, len(self.chain)):

            previous = self.chain[i - 1]
            current = self.chain[i]
            if(current.hash != current.calculate_hash()):
                print("Invalid Block")
                return False
            if(current.previoushash != previous.hash):
                print("Invalid Chain")
                return False
        return True
    
    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Block: {Block}")

    @property
    def last_block(self):
        return self.chain[-1]

        
