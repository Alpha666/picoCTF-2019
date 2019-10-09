#!/usr/bin/env python2

import base64,random,string

bytes = [18,25,55,252,248,230,248,246,124,43,141,211,73,205,162,187,16,223,0,142,73,3,78,227,145,65,142,127,0,50,31,182,123,59,78,196,13,253,26,63,58,66,96,116,154,53,19,231,166,201,1,193,0,69,1,68,38,0,0,172,56,0,254,120,42,106,0,96,147,10,68,10,93,0,0,13,97,72,191,255,227,31,70,128,198,0,90,114,34,120,156,130,64,192,222,0,227,141,156,39,244,73,26,65,174,7,232,13,120,77,201,82,0,0,13,222,80,134,105,58,0,131,131,0,69,55,0,108,137,80,21,0,126,1,9,236,1,212,163,237,155,59,68,228,0,0,188,71,243,1,76,17,84,141,55,163,230,40,95,51,164,0,248,114,124,124,85,7,48,204,128,102,251,227,138,51,48,12,219,2,171,136,248,107,101,154,202,248,62,110,152,100,205,205,190,159,38,84,254,213,236,50,34,222,66,253,245,55,12,53,2,163,21,199,104,157,227,198,239,204,34,85,150,175,137,242,111,233,145,34,136,104,223,127,55,69,86,135,141,86,254,95,192,91,11,228,213,61,12,64,1,52,239,255,182,102,170,223,200,116,60,252,46,223,249,255,95,195,81,233,158,128,1,92,126,39,35,228,124,244,61,61,157,31,221,34,100,234,21,40,63,29,86,80,68,42,198,44,147,98,200,143,189,187,171,44,133,253,104,52,53,74,160,102,128,252,223,127,114,19,174,255,170,18,39,252,194,85,27,63,177,62,16,205,161,59,122,165,41,252,161,122,161,253,51,155,127,67,46,166,34,61,64,241,130,109,132,107,81,13,123,206,201,80,124,119,241,33,241,45,8,92,198,145,7,187,37,196,84,86,211,179,123,170,253,198,245,111,150,15,172,202,198,87,209,79,49,50,78,106,212,1,173,177,183,127,199,175,239,99,252,230,44,42,182,237,104,10,90,142,57,105,17,142,246,101,223,189,235,207,255,21,6,192,238,87,26,29,215,91,36,221,71,84,191,243,241,129,252,21,10,173,161,212,40,186,154,20,180,94,19,126,10,8,250,234,253,34,133,42,77,168,212,130,194,231,41,126,50,176,38,160,168,61,98,76,253,56,206,79,108,235,204,67,175,254,253,59,187,175,148,95,211,191,195,43,139,61,195,181,171,201,136,71,244,9,255,118,252,252,213,203,91,242,46,242,23,86,38,127,246,235,44,126,146,48,21,53,21,156,172,174,79,191,143,252,49,17,162,61,228,56,241,61,198,223,57,128,90,63,21,223,31,87,219,109,85,227,109,134,56,69,33,223,215,138,154,129,58,40,217,203,19,170,161,220,93,143,169,54,163,197,89,124,163,21,1,152,159,204,102,114,107,239,217,54,210,191,164,67,179,11,234,183,124,244,72,32,124,4,247,139,204,115,35,242,237,24,35,148,24,40,48,158,219,60,111,56,156,119,2,2,61,41,180,228,93,217,171,255,56,93,117,166,159,115,102,190,181,79,54,245,83,191,175,148,30,120,47,11,95,214,102,254,99,189,99,122,107,166,5,202,87,222,62,229,223,211,242,221,215,63,153,156,203,182,6,84,172,63,178,252,149,34,233,120,231,49,175,179,147,39,15,106,101,227,0,74,214,253]

num = 0
arr = [0x89,0x50,0x4e,0x47,0xd,0x0a,0x1a,0x0a,0,0,0,0xd,0x49,0x48,0x44,0x52]
for j in arr:
	s = []
	for i in range(len(bytes)):
		if bytes[i] == j:
			s.append(i)
	for i in s:
		if (i-num)%16 == 0:
			print(hex(j)," ",chr((i-num)//16))
	print("DONE!")
	num += 1

def randomStr():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def assemble_png(u_in):
	LEN = 16
	key = "0000000000000000"
	shifter = 0

	if(len(u_in) == 16):
		key = u_in
	result = [0]*800
	for i in range(16):
		shifter = ord(key[i])
		for j in range(47): # 720/16 - 45 blocks
			result[(j*16)+i] = bytes[(((j+shifter)*16)%720)+i]
	while result[len(result)-1] == 0:
		result = result[0:len(result)-1]
	flag = []
	for i in result:
		flag.append(i)
	return flag

arr1 = ['\x08','\x0e']
arr7 = ['\x02','\x06']
arr10 = ['\x03','\x04']
arr11 = ['\x03','\x04']
arr12 = ['\x04','\x06']
for i in range(2):
	for j in range(2):
		for k in range(2):
			for l in range(2):
				for m in range(2):
					key = arr1[i] + "\x08\x02\t\x02\x04" + arr7[j] + "\x04\x07" + arr10[k] + arr11[l] + arr12[m] + "\x00\x04\x08\x06"
					s = assemble_png(key)
					file = open('a'+randomStr()+'.png','wb')
					file.write(str(bytearray(s)))
					file.close()