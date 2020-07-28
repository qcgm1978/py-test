
import unittest,ipaddress
from ip_address import (
    ip_address,
    get_ipaddress,
    get_num_addresses,
    getHosts,
    get_hostmask,
)
class TDDnetwork_list(unittest.TestCase):
    def test_network_list(self):
        net4 = ipaddress.ip_network('192.0.2.0/24')
        net5 = get_ipaddress.ip_network('192.0.2.0/24')
        self.assertEqual(net4[1],ipaddress.IPv4Address('192.0.2.1'))
        self.assertEqual(net5[1],('192.0.2.1'))
        self.assertEqual(net4[-1],ipaddress.IPv4Address('192.0.2.255'))
        self.assertEqual(net5[-1],('192.0.2.255'))
        net6 = ipaddress.ip_network('2001:db8::0/96')
        net6_ = get_ipaddress.ip_network('2001:db8::0/96')
        self.assertEqual(net6[1],ipaddress.IPv6Address('2001:db8::1'))
        self.assertEqual(net6[2],ipaddress.IPv6Address('2001:db8::2'))
        self.assertEqual(net6_[1],('2001:db8::1'))
        self.assertEqual(net6_[2],('2001:db8::2'))
        self.assertEqual(net6[-1],ipaddress.IPv6Address('2001:db8::ffff:ffff'))
        self.assertEqual(net6_[-1], ('2001:db8::ffff:ffff'))
    def test_containment_test(self):
        addr4 = ipaddress.ip_address('192.0.2.1')
        addr4_ = get_ipaddress.ip_address('192.0.2.1')
        print(addr4_)
        self.assertTrue(addr4 in ipaddress.ip_network('192.0.2.0/24') )
        self.assertTrue(addr4_ in get_ipaddress.ip_network('192.0.2.0/24') )
        self.assertFalse(addr4 in ipaddress.ip_network('192.0.3.0/24') )
        # self.assertFalse(addr4_ in get_ipaddress.ip_network('192.0.3.0/24') )
if __name__ == '__main__':
    unittest.main()

                