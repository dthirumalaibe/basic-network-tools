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
    
    # Constructor stores each byte separately in an array after parsing the
    #  input string according to a child-defined method. Perform lower-bound
    #  error-checking on the address length to ensure it is non-negative.
    def __init__(self, inputString, addrLen):
        self._octet = self._parseInputString( inputString )
        if ( addrLen < 0 ):
            raise ValueError("addrLen is negative: " + str( addrLen ) )
        self._addrLen = addrLen
        
    # Consumes the "inputString" parameter and turns it into a list of octets
    #  for use with arithmetic functions. Implemented by child classes since
    #  network addresses have variable formatting
    @abc.abstractmethod
    def _parseInputString( self, inputString ):
        return
    
    # Splits the specified string "inputString" using delimeter "delim"
    #  and expects to see a list of strings of length "numOctets". This
    #  method includes built-in error checking for null references
    #  and malformed network addresses. Child constructors can use this
    #  to validate input before building the objects. Method returns
    #  the list of substrings, assuming there are no errors.
    def _splitInputString(self, inputString, delim, numOctets):
        
        # Test for a null reference; raise error
        if( inputString is None or len( inputString ) == 0 ):
            raise AttributeError( "inputString is None or empty" )
        
        # Split the string into pieces based on    
        stringOctets = inputString.split( delim )      
            
        # There should be exactly "numOctets" octets in the address
        if( len( stringOctets ) != numOctets ):
            raise ValueError( "Incorrect number of octets: " + 
            str ( len( stringOctets ) ) )
        
        # Method success; return the list of substrings    
        return stringOctets
            
    
    # If a valid index, return the non-canonically referenced result
    def getOctet(self, octet):
        
        # Test validity of the octet index    
        if ( octet >= 1 and octet <= len( self._octet ) ):
            return self._octet[octet - 1]
        else:
            # Index out of bounds condition, return -1 to signal error
            # FUTURE: Could raise an error alternatively
            return -1
    
    # Returns the address length (aka prefix length) of the given address        
    def getAddrLen(self):
        return self._addrLen     

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
        
    # Defines the action taken when this object is treated like a string.
    #  In this case, invokes the abstract toString() method implemented
    #  in the child classes.
    def __str__(self):
        return self.toString()

    # Test for unicast addressing; returns true if the address is unicast
    @abc.abstractmethod
    def isUnicast(self):   
        return
          
    # Test for multicast addressing; returns true if the address is multicast   
    @abc.abstractmethod
    def isMulticast(self):
        return