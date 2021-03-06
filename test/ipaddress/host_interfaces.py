import unittest, ipaddress, types
from ip_address import (
    ip_address,
    get_ipaddress,
    get_num_addresses,
    getHosts,
    get_hostmask,
)


class TDDhost_interfaces(unittest.TestCase):
    def test_host_interfaces(self):
        i = ipaddress.ip_interface("192.0.2.1/24")
        self.assertEqual(i, ipaddress.IPv4Interface("192.0.2.1/24"))
        i1 = ipaddress.ip_interface("2001:db8::1/96")
        self.assertEqual(i1, ipaddress.IPv6Interface("2001:db8::1/96"))

    def test_inspect_obj(self):
        addr4 = ipaddress.ip_address("192.0.2.1")
        addr4_ = get_ipaddress("192.0.2.1")
        addr6 = ipaddress.ip_address("2001:db8::1")
        addr6_ = get_ipaddress("2001:db8::1")
        self.assertEqual(addr6.version, 6)
        self.assertEqual(addr6_.version, 6)
        self.assertEqual(addr4.version, 4)
        self.assertEqual(addr4_.version, 4)

    def test_obtain_network(self):
        host4 = ipaddress.ip_interface("192.0.2.1/24")
        self.assertEqual(host4.network, ipaddress.IPv4Network("192.0.2.0/24"))
        host6 = ipaddress.ip_interface("2001:db8::1/96")
        self.assertEqual(host6.network, ipaddress.IPv6Network("2001:db8::/96"))
        net4 = ipaddress.ip_network("192.0.2.0/24")
        self.assertEqual(net4.num_addresses, 256)
        self.assertEqual(get_num_addresses("192.0.2.0/24"), 256)
        net6 = ipaddress.ip_network("2001:db8::0/96")
        self.assertEqual(net6.num_addresses, 4294967296)
        self.assertEqual(net6.num_addresses, get_num_addresses("2001:db8::0/96"))

    def test_iter_usable(self):
        net4 = ipaddress.ip_network("192.0.2.0/24")
        it = net4.hosts()
        self.assertIsInstance(it, types.GeneratorType)
        l = list(it)
        l1 = getHosts("192.0.2.0/24")
        self.assertEqual(len(l), 254)
        self.assertEqual(len(l1), 254)
        self.assertEqual(l[0].compressed, "192.0.2.1")
        self.assertEqual(l1[0], "192.0.2.1")
        self.assertEqual(l[253].compressed, "192.0.2.254")
        self.assertEqual(l1[253], "192.0.2.254")

    def test_obtain_hostmask(self):
        net4 = ipaddress.ip_network("192.0.2.0/24")
        net5 = get_hostmask("192.0.2.0/24")
        self.assertEqual(net4.netmask, ipaddress.IPv4Address("255.255.255.0"))
        self.assertEqual(net5["netmask"], ("255.255.255.0"))
        self.assertEqual(net4.hostmask, ipaddress.IPv4Address("0.0.0.255"))
        self.assertEqual(net5["hostmask"], ("0.0.0.255"))
        net6 = ipaddress.ip_network("2001:db8::0/96")
        net7 = get_hostmask("2001:db8::0/96")
        self.assertEqual(
            net6.netmask, ipaddress.IPv6Address("ffff:ffff:ffff:ffff:ffff:ffff::")
        )
        self.assertEqual(net7["netmask"], ("ffff:ffff:ffff:ffff:ffff:ffff::"))
        self.assertEqual(net6.hostmask, ipaddress.IPv6Address("::ffff:ffff"))
        self.assertEqual(net7["hostmask"], ("::ffff:ffff"))

    def test_explode_compress(self):
        addr6 = ipaddress.ip_address("2001:db8::1")
        addr6_ = get_ipaddress("2001:db8::1")
        self.assertEqual(addr6.exploded, "2001:0db8:0000:0000:0000:0000:0000:0001")
        self.assertEqual(addr6_.exploded, "2001:0db8:0000:0000:0000:0000:0000:0001")
        self.assertEqual(addr6.compressed, "2001:db8::1")
        self.assertEqual(addr6_.compressed, "2001:db8::1")
        net6 = ipaddress.ip_network("2001:db8::0/96")
        net6_ = get_ipaddress("2001:db8::0/96")
        self.assertEqual(net6.exploded, "2001:0db8:0000:0000:0000:0000:0000:0000/96")
        self.assertEqual(net6_.exploded, "2001:0db8:0000:0000:0000:0000:0000:0000/96")
        self.assertEqual(net6.compressed, "2001:db8::/96")
        self.assertEqual(net6_.compressed, "2001:db8::/96")


if __name__ == "__main__":
    unittest.main()

