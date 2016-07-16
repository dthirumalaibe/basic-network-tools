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
    
    # Invokes the parent constructor to build the network address, which
    #  performs most of the heavy lifting. Performs upper-bound checking
    #  on the address length to ensure it is not greater than 32. Note
    #  that the parent constructor performs lower-bound checking already.
    def __init__(self, inputString, addrLen = 32):
        if ( addrLen > 32 ):
            raise ValueError("addrLen is greater than 32: " + str( addrLen ) )
        NetAddress.__init__(self, inputString, addrLen)
    
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
                raise ValueError( "current out of range: " + str( current ) )
            
            # Range valid; add current to list    
            integerOctets.append( current )
            
        # Final sanity check; there should be exactly 4 octets in the list
        if( len( integerOctets ) != 4 ):
            raise ValueError( "len( integerOctets ) is not 4:" + 
            str( len( integerOctets ) ) )
            
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
    
    # Test for link local addressing (LLA), used for link-level communications
    #  Returns true if the address begins with 169.254.0.0 for unicast
    #  or 224.0.0.x for multicast
    def isLinkLocalAddress(self):
         
        if( self._octet[0] == 169 and self._octet[1] == 254 ):
            return True
            
        elif( self._octet[0] == 224 and self._octet[1] == 0 
        and self._octet[2] == 0 ):
            return True
            
        return False
    
    # Tests for private addressing defined in RFC 1918. Also tests for
    #  administratively-scoped multicast addressing. Private addresses:
    #  10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 239.0.0.0/8    
    def isPrivateAddress(self):
        
        # Test for 10.x.x.x
        if( self._octet[0] == 10):
            return True
        
        # Test for 172.16.x.x - 172.31.x.x
        elif( self._octet[0] == 172 and 
        (self._octet[1] >= 16 and self._octet[1] <= 31) ):
            return True
        
        # Test for 192.168.x.x
        elif( self._octet[0] == 192 and self._octet[1] >= 168 ):
            return True
            
        # Test for 239.x.x.x (multicast admin range)
        elif( self._octet[0] == 239 ):
            return True
        
        # All tests were false; address is not private
        return False
        
        