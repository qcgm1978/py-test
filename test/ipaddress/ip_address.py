import re
def getHosts(ip):
    pre = ip.split('/')[0][:-1]
    l=[]
    for i in range(254):
        l.append(pre + str(i+1))
    return l
def get_num_addresses(net):
        # each part of an IP address can have a value between 0-255. So the fourth part of the IP address permits for 256 different addresses (zero up to 255) that can be used for computers, IP phones, routers, laptops, printers and other devices.
    ver=get_version(net)
    return 2**8 if ver==4 else 2**32
def get_version(integer):
    if isinstance(integer,int):
        binStr = bin(integer)[2:]
        length = len(binStr)
        isIpv4 = length <= 32
        return 4 if isIpv4 else 6
    else:
        return 4 if '.' in integer else 6

def ip_address(integer,isIpv6=False,isNetwork=False):
    #  An IP address is a 32-bit binary address
    binStr = bin(integer)[2:]
    #  "dotted decimal" format
    ip = ''
    # This 32-bit address is subdivided into four 8-bit segments called octets.
    length = len(binStr)
    isIpv4 = length <= 32
    isVersion4=isIpv4 and not isIpv6
    if isVersion4 :
        zeroLen = 32 - length
        zeroStr = '0' * zeroLen
        binStr=zeroStr+binStr
        for i in range(4):
            # The four decimal values (4x8 = 32 bits) are then separated with periods
            start = 8 * i
            #  the segments of a dotted decimal addresses are decimal numbers with a range from 0 — 255.
            ip += str(int(binStr[start: start + 8], 2)) + '.'
        
    else:
        zeroLen = 128 - length
        zeroStr = '0' * zeroLen
        binStr=zeroStr+binStr
        for i in range(8):
            start = 16 * i
            ip += str(hex(int(binStr[start: start + 16], 2))) + ':'
        # Part of the IP address is used for "network ID, and the rest of the address is used for the "host ID."
    ret = ip[0:-1].replace('0x', '')
    ret=ret.replace('0:',':').replace('::',':').replace('::',':')
    if isNetwork:
            ret+='/'+str(length if length <= 32 else 128)
    return ret