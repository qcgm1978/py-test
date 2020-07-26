def ip_address(integer):
    #  An IP address is a 32-bit binary address
    binStr = bin(integer)[2:]
    #  "dotted decimal" format
    ip = ''
    # This 32-bit address is subdivided into four 8-bit segments called octets.
    if len(binStr)<=32:
        for i in range(4):
            # The four decimal values (4x8 = 32 bits) are then separated with periods
            start = 8 * i
            #  the segments of a dotted decimal addresses are decimal numbers with a range from 0 — 255.
            ip += str(int(binStr[start: start + 8], 2)) + '.'
    else:
        for i in range(8):
            start = 16 * i
            ip += str(hex(int(binStr[start: start + 16], 2))) + ':'
        # Part of the IP address is used for "network ID, and the rest of the address is used for the "host ID."
    return ip[0:-1].replace('0x','')