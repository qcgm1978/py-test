
import unittest,ipaddress
from ip_address import ip_address
class TDDdefine_networks(unittest.TestCase):
    def test_define_networks(self):
        i=ipaddress.ip_network('192.0.2.0/24')
        self.assertEqual(i,ipaddress.IPv4Network('192.0.2.0/24'))
        i1=ipaddress.ip_network('2001:db8::0/96')
        self.assertEqual(i1,ipaddress.IPv6Network('2001:db8::/96'))
    def test_host(self):
        self.assertRaises(ValueError,lambda:ipaddress.ip_network('192.0.2.1/24'))
        host = ipaddress.ip_network('192.0.2.1/24', strict=False)
        self.assertEqual(host, ipaddress.IPv4Network('192.0.2.0/24'))
    def test_define_int(self):
        integer=3221225984
        host=ipaddress.ip_network(integer)
        network=ip_address(integer,isIpv6=True)
        self.assertEqual(host,ipaddress.IPv4Network('192.0.2.0/32'))
        self.assertEqual(network,('192.0.2.0/32'))
        host1=ipaddress.ip_network(42540766411282592856903984951653826560)
        self.assertEqual(host1,ipaddress.IPv6Network('2001:db8::/128'))
if __name__ == '__main__':
    unittest.main()

                