
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
        print(i2)
        self.assertEqual(i1, ipaddress.IPv6Address('2001:db8::1'))
        self.assertEqual(i2,'2001:db8::1')
    def test_small_int(self):
        i = ipaddress.ip_address(1)
        i3=ip_address(1)
        self.assertEqual(i,ipaddress.IPv4Address('0.0.0.1'))
        self.assertEqual(i3,'0.0.0.1')
        i1=ipaddress.IPv4Address(1)
        self.assertEqual(i1,ipaddress.IPv4Address('0.0.0.1'))
        i2=ipaddress.IPv6Address(1)
        i4=ip_address(1,isIpv6=True)
        self.assertEqual(i2,ipaddress.IPv6Address('::1'))
        self.assertEqual(i4,'::1')
if __name__ == '__main__':
    unittest.main()

                