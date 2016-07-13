#!/usr/bin/python

###############################################################################
# File: NetAddress.py
# Author: Nicholas Russo
# Description: This file includes a class that represents a generic network
#  address. Basic operations such as retrieving an octet or measuring the 
#  number of octets are defined here. Specific implementations of network
#  addresses can use these basic functions.
###############################################################################

import abc

# Defines a generic network address object
class NetAddress(object):
    __metaclass__ = abc.ABCMeta
    
    # Constructor stores each byte separately in an array
    def __init__(self,octets):
        self._octet = []
        for octet in octets:
            self._octet.append(octet)
    
    # If a valid index, return the non-canonically referenced result
    def getOctet(self, octet):
        
        # Test validity of the octet index    
        if ( octet >= 1 and octet <= len( self._octet ) ):
            return self._octet[octet - 1]
        else:
            # Index out of bounds condition, return -1 to signal error
            return -1

    # Return true if the "bitIndex" bit of the "byteIndex" byte is set 
    # The parameters must be canonical (bits 0-7, bytes 0-5)   
    def _isBitset(self, bitIndex, byteIndex):
        byteValue = self._octet[byteIndex]
        bitValue = pow( 2, 7 - bitIndex )
        return ( byteValue & bitValue == bitValue )
    
    # Implements the len() function for a NetAddress by returning
    #  the number of octets (bytes) in the address    
    def __len__ (self):
        return len( self._octet )

    # Return the network address in an easy-to-read format.
    #  Note that some protocols may have multiple accesspable types 
    #  of human-readable representations, but at a minimum, one must
    #  be implemented by every child class
    @abc.abstractmethod
    def toString(self):
        return

    # Test for unicast addressing; returns true if the address is unicast
    @abc.abstractmethod
    def isUnicast(self):   
        return
          
    # Test for multicast addressing; returns true if the address is multicast   
    @abc.abstractmethod
    def isMulticast(self):
        return