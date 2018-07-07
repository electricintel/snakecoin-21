# -*- coding:utf-8 -*-
import datetime as date
from Block import Block

def create_genesis_block():
    """
    返回创世区块
    创世区块索引为0，此外，它所包含的数据以及前一个区块的哈希值都是一个任意的值
    :param self:
    :return: 创始区块
    """
    genesis_data = {
        "proof-of-work": 1,
        "transactions": "Hey! I'm genesis block "
    }
    return Block(0, date.datetime.now(), genesis_data, "0")

def next_block(last_block):
    """
    生成链上更多的区块
    :param self:
    :param last_block: 上一个区块
    :return: 新区块
    """
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = {
        "proof-of-work": this_index,
        "transactions": "Hey! I'm block " + str(this_index)
    }
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

def proof_of_work(last_proof):

    # Create a variable that wewill use to find
    # our next proof of work

    incrementor = last_proof + 1

    # Keep incrementing the incrementor until
    # it's equal to a number divisible by 9
    # and the proof of work of the previous
    # block in the chain

    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1

    # Once that number is found,
    # we can return it as a proof
    # of our work

    return incrementor


# Create the blockchain and add the genesis block
blockchain=[create_genesis_block()]

previous_block=blockchain[0]


# # How many blocks should we add to the chain
# #after the genesis block
# num_of_blocks_to_add=20
#
#
# # Addblocks to the chain
# for i in range(0,num_of_blocks_to_add):
#     block_to_add=next_block(previous_block)
#     blockchain.append(block_to_add)
#     previous_block=block_to_add
#     # Telleveryone about it!
#     print "Block #{} has been added to theblockchain!".format(block_to_add.index)
#     print "{}\n".format(block_to_add.toString())

