import matplotlib.pyplot as plt
import math

class LIF():
	def __init__(self,thresh,reset,c,r):
		self.V_t=thresh
		self.V_r=reset
		self.V=reset
		self.cap=c
		self.res=r
		self.values=[]

	def signal(self,I,dt):
		self.V+=(I/self.cap+self.V/self.res)*dt
		self.values.append(self.V)
		if self.V>=self.V_t:
			self.V=self.V_r
			return 1
		return 0

if __name__=="__main__":
	print "Enter first input (0 or 1):"
	a=input()
	print "Enter second input (0 or 1):"
	b=input()
	if a==1:
		a=8
	else:
		a=3
	if b==1:
		b=8
	else:
		b=3
	#two input neurons 
	in1=LIF(-40,-80,0.01,1)
	in2=LIF(-40,-80,0.01,1)
	#two neurons in hidden layer, one for OR and one for NAND
	OR=LIF(-40,-80,0.01,1)
	NAND=LIF(-40,-80,0.01,1)
	#one output neuron, AND the two outputs from the hiddern layer
	AND=LIF(-40,-80,0.01,1)
	#teacher neurons
	t_or=LIF(-40,-80,0.01,1)
	t_nand=LIF(-40,-80,0.01,1)
	t_and=LIF(-40,-80,0.01,1)
	#spike trains
	in1_train=[]
	in2_train=[]
	or_train=[]
	nand_train=[]
	and_train=[]
	for i in range(1000):
		
	
