
import unittest, ipaddress
from ip_address import ip_address
class TDDaddress_network_interface(unittest.TestCase):
    def test_address_network_interface(self):
        i=ipaddress.ip_address('192.0.2.1')
        self.assertEqual(i,ipaddress.IPv4Address('192.0.2.1'))
        i1=ipaddress.ip_address('2001:DB8::1')
        self.assertEqual(i1,ipaddress.IPv6Address('2001:db8::1'))
    def test_by_int(self):
        integer=3221225985
        i = ipaddress.ip_address(integer)
        ip='192.0.2.1'
        self.assertEqual(i, ipaddress.IPv4Address(ip))
        i2 = ip_address(integer)
        self.assertEqual(i2, ip)
        integer1=42540766411282592856903984951653826561
        i1 = ipaddress.ip_address(integer1)
        i2 = ip_address(integer1)
        self.assertEqual(i1, ipaddress.IPv6Address('2001:db8::1'))
        self.assertNotEqual(i2,'2001:db8::1')
if __name__ == '__main__':
    unittest.main()

                