import re, itertools,socket, struct

MAX_FIELD=255
def get_hostmask(ip):
    version = get_ipaddress(ip).version
    netmask = "%s.%s.%s.0" % MAX_FIELD if version == 4 else "ffff:ffff:ffff:ffff:ffff:ffff::"
    hostmask = "0.0.0.%s" % MAX_FIELD if version == 4 else "::ffff:ffff"
    return {"netmask": netmask, "hostmask": hostmask}


def getHosts(ip,start=0,end=254):
    pre = ip.split("/")[0][:-1]
    l = []
    version = get_ipaddress(ip).version
    if version==4:
        for i in range(start,end):
            l.append(pre + str(i + 1))
    else:
        for i in range(start,0xffffffff):
            l.append(pre + hex(i + 1)[2:])
    return l


def get_num_addresses(net):
    # each part of an IP address can have a value between 0-255. So the fourth part of the IP address permits for 256 different addresses (zero up to 255) that can be used for computers, IP phones, routers, laptops, printers and other devices.
    version = get_ipaddress(net).version
    return 2 ** 8 if version == 4 else 2 ** 32
class AddressValueError(Exception):

    def __init__(self, ip,l):
        self.ip = ip
        self.message = "Octet %s (> %s) not permitted in '%s'" % (l[0],MAX_FIELD, ip)
        super().__init__(self.message)
class NetmaskValueError(ValueError):
    """a netmask, where the address description is either a string, a 32-bits integer, a 4-bytes packed integer

    Attributes:
        ip -- network ip to validate
    """

    def __init__(self, ip,l):
        self.ip = ip
        self.message = "'%s' is not a valid netmask" % (l)
        super().__init__(self.message)

def hasError(ip,detail):
    l = ip.split('.')
    i = itertools.filterfalse(lambda x: int(x) < MAX_FIELD, l)
    val=list(i)
    if (len(val) > 0):
        if detail:
            raise AddressValueError(ip,val)
        else:
            raise ValueError("'%s' does not appear to be an IPv4 or IPv6 address" % ip)
def hasNetworkError(ip,detail=False):
    l = ip.split('/')
    if (int(l[1]) >= 32):
        if detail:
            raise NetmaskValueError(ip,int(l[1]))
        else:
            raise ValueError("'%s' does not appear to be an IPv4 or IPv6 network" % ip)
def ip_address(ip, isIpv6=False, isNetwork=False,detail=False):
    if (hasError(ip,detail)):
        return
    if isinstance(ip, str):
        return ip
    #  An IP address is a 32-bit binary address
    binStr = bin(ip)[2:]
    #  "dotted decimal" format
    ip = ""
    # This 32-bit address is subdivided into four 8-bit segments called octets.
    length = len(binStr)
    isIpv4 = length <= 32
    isVersion4 = isIpv4 and not isIpv6
    if isVersion4:
        zeroLen = 32 - length
        zeroStr = "0" * zeroLen
        binStr = zeroStr + binStr
        for i in range(4):
            # The four decimal values (4x8 = 32 bits) are then separated with periods
            start = 8 * i
            #  the segments of a dotted decimal addresses are decimal numbers with a range from 0 — 255.
            ip += str(int(binStr[start : start + 8], 2)) + "."

    else:
        zeroLen = 128 - length
        zeroStr = "0" * zeroLen
        binStr = zeroStr + binStr
        for i in range(8):
            start = 16 * i
            ip += str(hex(int(binStr[start : start + 16], 2))) + ":"
        # Part of the IP address is used for "network ID, and the rest of the address is used for the "host ID."
    ret = ip[0:-1].replace("0x", "")
    ret = ret.replace("0:", ":").replace("::", ":").replace("::", ":")
    if isNetwork:
        ret += "/" + str(length if length <= 32 else 128)
    return ret

class get_ipaddress(object):

    class ip_network(object):
        # return getHosts(ip,-1,255)
        def __init__(self, ip):
            self.ip = ip
            if (hasNetworkError(ip)):
                return
        def getHost(self,i):
            pre = self.ip.split("/")[0][:-1]
            version = get_ipaddress(self.ip).version
            maxNum=256 if version==4 else 0xffffffff+1
            index=i if i>=0 else maxNum+i
            if version==4:
                    l=pre + str(index )
            else:
                post = hex(index)[2:]
                if len(post) > 4:
                    post=post[0:4]+':'+post[4:]
                l=pre + post
            return l
        def __getitem__(self, x):
            return self.getHost(x)
    class IPv4Network(object):
        # return getHosts(ip,-1,255)
        def __init__(self, ip):
            self.ip = ip
            if (hasNetworkError(ip,detail=True)):
                return
        def getHost(self,i):
            pre = self.ip.split("/")[0][:-1]
            version = get_ipaddress(self.ip).version
            maxNum=256 if version==4 else 0xffffffff+1
            index=i if i>=0 else maxNum+i
            if version==4:
                    l=pre + str(index )
            else:
                post = hex(index)[2:]
                if len(post) > 4:
                    post=post[0:4]+':'+post[4:]
                l=pre + post
            return l
        def __getitem__(self, x):
            return self.getHost(x)
    def addZero(self, string):
        length = 4 - len(string)
        return "".join(list(itertools.repeat("0", length))) + string

    def __init__(self, ip=''):
        self.compressed = ip.replace(":0", ":")
        prepost = ip.split("/")
        l = prepost[0].split(":")
        if "" in l:
            l.remove("")
        fourZero = 8 - len(l)
        for i in range(fourZero):
            l.insert(-1, "0000")
        l = list(map(self.addZero, l))
        pre = ":".join(l)
        if len(prepost) == 2:
            self.exploded = pre + "/" + prepost[1]
        else:
            self.exploded = pre
        if isinstance(ip, int):
            binStr = bin(ip)[2:]
            length = len(binStr)
            isIpv4 = length <= 32
            self.version = 4 if isIpv4 else 6
        else:
            self.version = 4 if "." in ip else 6
    class IPv4Address(object):
        def __init__(self,ip):
                super().__init__()
                self.ip = ip
                ip_address(ip,detail=True)
    class ip_address(object):
        def __init__(self,ip):
                super().__init__()
                self.ip = ip
                ip_address(ip)
        def __str__(self):
            return self.ip
        def __int__(self):
            # l = self.ip.split('.')
            # l = list(map(self.addBits, l))
            # ip=''.join(l)
            # return int(ip,2)
            return self.ip2long(self.ip)
        def __lt__(self, other):
            return self.ip < other.ip
        def ip2long(self,ip):
            """
            Convert an IP string to long
            """
            packedIP = socket.inet_aton(ip)
            return struct.unpack("!L", packedIP)[0]
        def addBits(self, field):
            field=bin(int(field))[2:]
            length=len(field)
            zeroLen = 4 - length
            zeroStr = "0" * zeroLen if zeroLen>0 else ''
            return zeroStr + field

    AddressValueError = AddressValueError
    NetmaskValueError=NetmaskValueError