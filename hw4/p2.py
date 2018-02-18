str = raw_input ("Please enter your full name")

reverse = str[::-1]
upfirlet = str.title()
upper_str = str.upper()

s = str.split()
s1 = s[0]
s2 = s[1]
s3 = s[2]
backfirst = s1[::-1]
backmiddle = s2[::-1]
backlast = s3[::-1]

length = len(str)
firsthalf = str[:len(str)/2]
secondhalf = str[len(str)/2:]

print upfirlet
print upper_str
print backfirst +" "+ backmiddle +" "+ backlast
print firsthalf +"-BOB-"+ secondhalf
