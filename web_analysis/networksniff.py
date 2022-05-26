"""
Initial idea is to test and work on sniffing http traffic. While the end goal may involve more request types, http seems
like a good place to start with.
"""

import socket
import struct
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket. htons(0x0800))
