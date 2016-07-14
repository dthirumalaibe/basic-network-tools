#!/usr/bin/python

###############################################################################
# File: MACAddress.py
# Author: Nicholas Russo
# Description: This file includes a class that represents a MAC address.
#  Specific MAC operations, such as testing unicast/multicast or printing
#  string versions of the address are supported. More basic operations such as 
#  retrieving an octet or measuring the number of octets are defined in the
#  parent class (NetAddress).
###############################################################################

from NetAddress import NetAddress

# Defines a MAC address, inheriting from NetAddress
class MACAddress(NetAddress):

    # Return the MAC address in EUI format (xx:xx:xx:xx:xx:xx)
    def toString(self): 
        
        # Start with an empty string
        macString = ""
        macStringLen = len( self._octet )
        
        # Iterate over all of the octets
        for i in range( 0, macStringLen ):
            
            # Build the octet in "xx" format an append it to the main string
            macString += str( hex( self._octet[i] )[2:].zfill(2) )
            
            # Be sure to add the colon every time an octet is added
            #  The only exception is not adding a trailing colon
            if i < ( macStringLen - 1):
                macString += ":"
        
        return macString
        
    # Return the MAC address in Cisco format (xxxx.xxxx.xxxx)
    def toStringCisco(self): 
        
        # Start with an empty string
        octetLength = len( self._octet )
        macString = ""
        
        # Iterate over all of the octets
        for i in range( 0, octetLength ):
            
            # Build the octet in "xx" format an append it to the main string
            macString += str( hex( self._octet[i] )[2:].zfill(2) )
            
            # Be sure to add the period every other time an octet is added
            #  The only exception is not adding a trailing period
            if( i % 2 == 1 and ( i < octetLength - 1 ) ):
                macString += "."
                
        return macString
        
    # Defines the action taken when this object is treated like a string.
    #  In this case, invokes the toString() method    
    def __str__(self):
        return self.toString()
    
    # Return true if the seventh bit of the first byte is set
    def isULset(self):
        return self._isBitset( 6, 0 )
    
    # Return true if the eigth bit of the first byte is set
    def isIGset(self):
        return self._isBitset( 7, 0 )
            
    # Test for multicast MAC addressing (I/G clear)  
    def isUnicast(self):   
        return not self.isIGset()
          
    # Test for multicast MAC addressing (I/G set)  
    def isMulticast(self):
        return self.isIGset()