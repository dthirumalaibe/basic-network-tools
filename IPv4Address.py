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
    
    # Implements the abstract method defined in NetAddress. Breaks a
    #  dotted decimal IPv4 address into a list of 4 integers; this
    #  list is returned from the method
    def _parseInputString( self, inputString ):
        
        # Split the input string into 4 separate octets; any errors
        #  raised by this method are passed up the recursion stack
        ipStringOctets = self._splitInputString( inputString, ".", 4 )
        
        # Iterate over all of the substrings, which should be 
        #  8-bit unsigned integers
        integerOctets = []
        for ipStringOctet in ipStringOctets:
            
            # Test for valid range 0 <= x <= 255
            current = int( ipStringOctet )
            if( current < 0 or current > 255 ):
                # Range invalid; raise error
                raise ValueError( "current out of range: " + current )
            
            # Range valid; add current to list    
            integerOctets.append( current )
            
        # Final sanity check; there should be exactly 4 octets in the list
        if( len( integerOctets ) != 4 ):
            raise ValueError( "len( integerOctets ) is not 4:" + len( integerOctets ) )
            
        # Return the list of integer octets after parsing.
        #  This typically will be returned to the parent's constructor
        return integerOctets
    
    # Return the IPv4 address in dotted-decimal format (xx.xx.xx.xx)
    def toString(self): 
        
        # Start with an empty string
        ipString = ""
        ipStringLen = len( self._octet )
        
        # Iterate over all of the octets
        for i in range( 0, ipStringLen ):
            
            # Append the plain decimal octet to the main string
            ipString += str( self._octet[i] )
            
            # Be sure to add the colon every time an octet is added
            #  The only exception is not adding a trailing colon
            if i < ( ipStringLen - 1):
                ipString += "."
        
        return ipString
        
        # Legacy implementation
        #return "%d.%d.%d.%d" % (
        #    self._octet[0], self._octet[1], self._octet[2], self._octet[3] )
            
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