# -*- coding:utf-8 -*-

import hashlib as hasher
import json


"""
 块
 在区块链中，
 每个区块上都有一个时间戳，有时还会有一个索引。
 在SnakeCoin 中，我们两个都有。
 同时，为了保证整个区块链的完整性，
 每一个区块都有一个唯一的哈希值，用于自我标识
"""

class Block(object):

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    # 每一个区块的哈希值是由区块的索引、时间戳、数据以及前一个区块的哈希，经过加密后得到的
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdigest()

    def toString(self):
        return " index:{}\n timestamp:{}\n data={}\n hash={}\n previous_hash={} \n"\
            .format(self.index,self.timestamp,self.data,self.hash,self.previous_hash)