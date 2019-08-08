import hashlib
import requests

import sys


# Implement functionality to search for a proof 
# Both functions below were moved from basic blockchain
#Removed self since it's no longer a class function
# Added some print statements
def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm
    Find a number p such that hash(last_block_string, p) contains 6 leading
    zeroes
    """
    print("Starting")
    proof = 0
    # for block 1, hash(1,p) = 000000x
    while valid_proof(last_proof, proof) is False :
        proof += 1
    print("Sending to server...")    
    return proof   

def valid_proof(last_proof, proof):
    """
    Validates the Proof:  
    Does hash(block_string, proof)
    contain 6 leading zeroes?
    """
    #build string to hash
    guess = f'{last_proof}{proof}'.encode()
    #use hash function
    guess_hash = hashlib.sha256(guess).hexdigest()
    # check if 6 leading 0's
    beg = guess_hash[0:6] # [:6]
    if beg == "000000":
        return True
    else:
        return False

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # Get the last proof from the server a

        # generate request with /last_proof
        # Will probably need a get request
       
        # Look for next proof based on results from above request
        new_proof = proof_of_work(last_proof)

        #When next proof found, POST it to the server {"proof": new_proof}
        
        #The server will validate our results to make sure proof has not already been submitted
        #If valid, it will create a new block and reward with a coin.

        #Research POST in python
        #Research requests and remamber we're sending data as JSON
        
        # Assign our new_proof to 'proof'
        proof_data = {'proof': new_proof}

        # requests.post to /mine endpoint
        r = requests.post(url = node + '/mine', data = data)
        data = r.json()

        #If the server responds with 'New Block Forged, add one coin
        if r.message == 'New Block Forged':
            coins_mined += 1
            print('Coines mined: ', coins_mined)
        print(data.get('message'))
        
        #Our infinite loop will repeate until user does keyboard interupt in the client terminal.
