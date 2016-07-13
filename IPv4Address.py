#!/usr/bin/python

###############################################################################
# File: IPv4Address.py
# Author: Nicholas Russo
# Description: This file includes a class that represents an IPv4 address.
#  Specific IPv4 operations, such as testing unicast/multicast or printing
#  string versions of the address are supported. More basic operations such as 
#  retrieving an octet or measuring the number of octets are defined in the
#  parent class (NetAddress).
###############################################################################

from NetAddress import NetAddress

# Defines an IPv4 address, inheriting from NetAddress
class IPv4Address(NetAddress):

    # Return the IPv4 address in dotted-decimal format (xx.xx.xx.xx)
    def toString(self): 
        return "%d.%d.%d.%d" % (
            self._octet[0], self._octet[1], self._octet[2], self._octet[3] )
            
    # Return the IPv4 address in contiguous hexadecimal format 
    #  which includes the leading "0x" string (0xaabbccdd)
    def toStringHex(self): 
        ipString = "0x"
        ipStringLen = len( self._octet )
        for i in range( 0, ipStringLen ):
            ipString += str( hex( self._octet[i] )[2:].zfill(2) )
        
        return ipString
    
    # Test for Class A, B, or C addressing   
    def isUnicast(self):   
        return ( self._octet[0] < 224 )  
          
    # Test for Class D addressing    
    def isMulticast(self):
        return ( self._octet[0] >= 224 and self._octet[0] <= 239 )
    
    # Test for Class E addressing    
    def isExperimental(self):
        return ( self._octet[0] > 239 )