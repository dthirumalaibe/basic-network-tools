#!/usr/bin/python

###############################################################################
# File: NetAddress_Test.py
# Author: Nicholas Russo
# Description: This file includes an abstract class that represents a test case
#  to be extended by specific network address test case implementations. 
#  This class includes test setup/teardown, as well as some highly-generic
#  test cases which are relevant for any network address type. A static method
#  is supplied to construct a test suite for each child class for execution.
###############################################################################

import abc
import unittest
from NetAddress import NetAddress

# Defines a generic network address object
class NetAddress_Test(unittest.TestCase):
    
    # Automatically run before the test starts. Initializes the 
    #  network address list, then populates it based on the child-specific
    #  population method (polymorphism).    
    def setUp(self):
        # Toggle debugging
        #print("setup")
        self._netAddressList = []
        self.populateNetAddressList()
    
    # Automatically runs after the test is complete (or an error occurs).
    #  The array is set to None (null) which deallocates it from memory.
    def tearDown(self):
        # Toggle debugging
        #print("teardown")  
        self._netAddressList = None
    
    # Returns the list of network addresses. The children could simply use the
    #  _netAddressList "private" variable but the get() function is "safer".           
    def getNetAddressList(self):
        return self._netAddressList
    
    # Implemented by children nodes; Rather than allocate/deallocate objects
    #  for each test, it is created once and retained in memory for the
    #  duration of the object's life. As more test methods are added to a
    #  test case in the future, the same set of address objects can be used.
    @abc.abstractmethod
    def populateNetAddressList(self):
        return
    
    # Class-wide method that builds a TestSuite by dynamically collecting
    #  all methods defined within the specified TestCase.    
    @staticmethod
    def buildTestSuite( childClassName ):
        return unittest.TestLoader().loadTestsFromTestCase( childClassName )
    
    # Tests the getOctet() function within the IPv4Address class.
    #  This test is common for all network addresses.
    #  Note that invalid fields are tested (one octet before and after
    #  the proper range) for completeness.    
    def test_getOctet( self ):
        
        # Iterate over the list of octets
        for address in self.getNetAddressList():
        
            # Test octets which count from 1 to n (not canonical).
            #  Octets are tested from 0 (invalid) to len+1 (also invalid)
            for i in range( 0, len(address) + 2 ):
                
                # Test invalid octets 0 and n+1; everything 0<i<n should at 
                #  least be 0<i<255 (unsigned 8 bit integer)
                if( i == 0 or i == len(address) + 1 ):
                    self.assertTrue( address.getOctet(i) == -1 )
                    continue
                else:
                    self.assertTrue( address.getOctet(i) >= 0 
                    and address.getOctet(i) <= 255 )
