
import unittest,ipaddress
class TDDhost_interfaces(unittest.TestCase):
    def test_host_interfaces(self):
        i=ipaddress.ip_interface('192.0.2.1/24')
        self.assertEqual(i,ipaddress.IPv4Interface('192.0.2.1/24'))
        i1=ipaddress.ip_interface('2001:db8::1/96')
        self.assertEqual(i1, ipaddress.IPv6Interface('2001:db8::1/96'))
    def test_inspect_obj(self):
        addr4 = ipaddress.ip_address('192.0.2.1')
        addr6 = ipaddress.ip_address('2001:db8::1')
        self.assertEqual(addr6.version,6)
        self.assertEqual(addr4.version,4)

if __name__ == '__main__':
    unittest.main()

                