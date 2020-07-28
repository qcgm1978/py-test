from ip_address import (
    ip_address,
    get_ipaddress,
    get_num_addresses,
    getHosts,
    get_hostmask,
    AddressValueError
)
import unittest,ipaddress,itertools
class TDD_fails_detail(unittest.TestCase):
    def setUp(self):
        def validate(error,errorType,func):
            with self.assertRaises(errorType) as cm:
                func() 
            the_exception = cm.exception
            self.assertEqual(str(the_exception), error)
        self.raises=validate
    def test__fails_detail(self):
        self.raises(error="'192.168.0.256' does not appear to be an IPv4 or IPv6 address", errorType=ValueError, func=lambda: ipaddress.ip_address("192.168.0.256"))
        self.raises(error="'192.168.0.256' does not appear to be an IPv4 or IPv6 address", errorType=ValueError, func=lambda: get_ipaddress.ip_address("192.168.0.256"))
        self.raises(error="Octet 256 (> 255) not permitted in '192.168.0.256'",func=lambda:ipaddress.IPv4Address("192.168.0.256"),errorType=ipaddress.AddressValueError)
        self.raises(error="Octet 256 (> 255) not permitted in '192.168.0.256'",func=lambda:get_ipaddress.IPv4Address("192.168.0.256"),errorType=get_ipaddress.AddressValueError)
        self.raises(func=lambda:ipaddress.ip_network("192.168.0.1/64"),errorType=ValueError,error="'192.168.0.1/64' does not appear to be an IPv4 or IPv6 network")
        self.raises(func=lambda:get_ipaddress.ip_network("192.168.0.1/64"),errorType=ValueError,error="'192.168.0.1/64' does not appear to be an IPv4 or IPv6 network")
        self.raises(func=lambda:ipaddress.IPv4Network("192.168.0.1/64"),error="'64' is not a valid netmask",errorType=ipaddress.NetmaskValueError)
        self.raises(func=lambda: get_ipaddress.IPv4Network("192.168.0.1/64"), error="'64' is not a valid netmask", errorType=get_ipaddress.NetmaskValueError)
    def test_parent_err(self):
        address="192.168.0.1/64"
        try:
            network = ipaddress.IPv4Network(address)
        except ValueError:
            print('address/netmask is invalid for IPv4:', address)
        try:
            network = get_ipaddress.IPv4Network(address)
        except ValueError:
            print('address/netmask is invalid for IPv4:', address)
        self.assertIn(ValueError,ipaddress.NetmaskValueError.__bases__)
        self.assertIn(ValueError,get_ipaddress.NetmaskValueError.__bases__)

if __name__ == '__main__':
    unittest.main()

                