#SHWRMA Blockchain
#Mubeen Ahmed Jawad
#mubeenjawad87@gmail.com

import datetime as date
import hashlib as hasher
import random
import string
import uuid

class Block:
    def __init__(self, index, timestamp, data, previous_hash,
                 trx_id, trx_send, trx_rec, trx_amount):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.trx_id= trx_id
        self.trx_send = trx_send
        self.trx_rec = trx_rec
        self.trx_amount = trx_amount
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.trx_id) +
                    str(self.trx_send) +
                    str(self.trx_rec) +
                    str(self.trx_amount) +
                    str(self.previous_hash)).encode())  # change here
        return sha.hexdigest()


def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0", 000, 0000000000000, 0000000000000, "$$$")

def generate_random_address():
    """Generates a fake blockchain-like address"""
    return '0x' + ''.join(random.choices('abcdef' + string.digits, k=40))

def generate_transaction():
    trx_iden = str(uuid.uuid4())  # Unique transaction ID
    sender_address = generate_random_address()
    rec_address = generate_random_address()
    amount = 1  # Random amount with up to 6 decimal places

    return str(trx_iden), str(sender_address), str(rec_address), str(amount)

def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Block " + str(this_index)
  trx_id, sender, receiver, amount = generate_transaction()
  this_trx_id = trx_id
  this_trx_sender = sender
  this_trx_receiver = receiver
  this_trx_amount = amount
  this_hash = last_block.hash

  return Block(this_index, this_timestamp, this_data, this_hash, this_trx_id,
               this_trx_sender,
               this_trx_receiver,
               this_trx_amount)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]

print(" ")
print("THE SHAWARMA-COIN BLOCKCHAIN (SHWRMA)")

def get_blockchain_info():
    previous_block = blockchain[0]   #Get the Genesis Block
    num_of_blocks_to_add = 5 # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
      block_to_add = next_block(previous_block)
      blockchain.append(block_to_add)
      previous_block = block_to_add
      # Generate Blockchain Report
      print("\nBlock #{} has been added to the blockchain!".format(block_to_add.index))
      print("Timestamp: {}".format(block_to_add.timestamp))
      print("Block Description: {}".format(block_to_add.data))
      print("Transaction ID: {}".format(block_to_add.trx_id))
      print("Sender Address: {}".format(block_to_add.trx_send))
      print("Receiver Address: {}".format(block_to_add.trx_rec))
      print("Amount: {} SHWRMA".format(block_to_add.trx_amount))
      print("Previous Block Hash: {}".format(block_to_add.previous_hash))
      print("Current Block Hash: {}".format(block_to_add.hash))

get_blockchain_info()