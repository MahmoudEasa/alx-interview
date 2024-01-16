#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 2
print("answer: 2")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 3
print("answer: 3")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 4
print("answer: 4")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("answer: 7")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 6
print("answer: 5")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 20
print("answer: 9")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1
print("answer: 0")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 15
print("answer: 8")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 25
print("answer: 10")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 21654876512
print("answer: 13695")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = ""
print("answer: 0")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
