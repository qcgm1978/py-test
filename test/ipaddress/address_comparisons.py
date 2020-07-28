from ip_address import (
    ip_address,
    get_ipaddress,
    get_num_addresses,
    getHosts,
    get_hostmask,
)
import unittest,ipaddress
class TDDaddress_comparisons(unittest.TestCase):
    def test_address_comparisons(self):
        self.assertTrue(ipaddress.ip_address('192.0.2.1') < ipaddress.ip_address('192.0.2.2'))
        ip1 = get_ipaddress.ip_address('192.0.2.1')
        ip2=get_ipaddress.ip_address('192.0.2.2')
        self.assertTrue(ip1 < ip2)
    def test_modules(self):
        addr4 = ipaddress.ip_address('192.0.2.1')
        addr4_ = get_ipaddress.ip_address('192.0.2.1')
        self.assertEqual(str(addr4),'192.0.2.1')
        self.assertEqual(str(addr4_),'192.0.2.1')
        self.assertEqual(int(addr4), 3221225985)
        # print(int(get_ipaddress().compressed))
        self.assertEqual(int(addr4_),3221225985)

if __name__ == '__main__':
    unittest.main()

                