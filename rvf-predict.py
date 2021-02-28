wheelValues = ['700','150','verliesbeurt','450','300','800','350','550','200','750','400','verliesbeurt','200','600','1000','bankroet','50','600','450','800']


# Current seed is located at 55dc:25ac. Pause game before next wheel turn
# Wheelcounter is the location of the wheel, starting with index 0. Example: 350 -> wheelCounter = 6

currentSeed = 0x214bb6e9
wheelCounter = 14


fixedFactor = 0x8088405 # Defined by Pascal runtime library

resultNumber = 0
a=0

while(a<=30):

	newSeed = currentSeed * fixedFactor
	newSeed = newSeed & 0xFFFFFFFF
	newSeed = newSeed + 1

#	print("Seed: ",hex(newSeed))

	resultNumber = newSeed & 0xFFFF0000
	resultNumber = resultNumber * 0x12
	resultNumber = resultNumber >> 32
	resultNumber = resultNumber + 0x26

	wheelCounter = (wheelCounter + resultNumber) % 20
	print("Wheel: ", wheelValues[wheelCounter])

	currentSeed = newSeed
	a = a+1
