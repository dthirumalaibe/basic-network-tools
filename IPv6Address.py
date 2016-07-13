#!/usr/bin/python

###############################################################################
# File: IPv6Address.py
# Author: Nicholas Russo
# Description: This file includes a class that represents an IPv4 address.
#  Specific IPv6 operations, such as testing unicast/multicast or printing
#  string versions of the address are supported. More basic operations such as 
#  retrieving an octet or measuring the number of octets are defined in the
#  parent class (NetAddress).
###############################################################################

from NetAddress import NetAddress

# Defines an IPv6 address, inheriting from NetAddress
class IPv6Address(NetAddress):

    # Return the IPv6 address in fully extended EUI format 
    # (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx)
    def toString(self): 
        
        # Start with an empty string
        octetLength = len( self._octet )
        ipv6String = ""
        
        # Iterate over all of the octets
        for i in range( 0, octetLength ):
            
            # Build the octet in "xx" format an append it to the main string
            ipv6String += str( hex( self._octet[i] )[2:].zfill(2) )
            
            # Be sure to add the colon every other time an octet is added
            #  The only exception is not adding a trailing colon
            if( i % 2 == 1 and ( i < octetLength - 1 ) ):
                ipv6String += ":"
                
        return ipv6String
    
    # Test for unicast addressing; returns true if the first octet is not 0xFF
    def isUnicast(self):   
        return self._octet[0] != 0xff
          
    # Test for multicast addressing; returns true if the first octet is 0xFF  
    def isMulticast(self):
        return self._octet[0] == 0xff
