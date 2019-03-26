import matplotlib.pyplot as plt
import math
import numpy as np

dt=0.001
size=10
interval=10000

diag=[[0,0,0,0,0,0,0,0,0,1],\
	  [0,0,0,0,0,0,0,0,1,0],\
	  [0,0,0,0,0,0,0,1,0,0],\
	  [0,0,0,0,0,0,1,0,0,0],\
	  [0,0,0,0,0,1,0,0,0,0],\
	  [0,0,0,0,1,0,0,0,0,0],\
	  [0,0,0,1,0,0,0,0,0,0],\
	  [0,0,1,0,0,0,0,0,0,0],\
	  [0,1,0,0,0,0,0,0,0,0],\
	  [1,0,0,0,0,0,0,0,0,0]]

diag1=[[0,0,0,0,0,0,0,0,1,0],\
	   [0,0,0,0,0,0,0,1,0,0],\
	   [0,0,0,0,0,0,1,0,0,0],\
	   [0,0,0,0,0,1,0,0,0,0],\
	   [0,0,0,0,1,0,0,0,0,0],\
	   [0,0,0,1,0,0,0,0,0,0],\
	   [0,0,1,0,0,0,0,0,0,0],\
	   [0,1,0,0,0,0,0,0,0,0],\
	   [1,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0]]

diag2=[[0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,1],\
	   [0,0,0,0,0,0,0,0,1,0],\
	   [0,0,0,0,0,0,0,1,0,0],\
	   [0,0,0,0,0,0,1,0,0,0],\
	   [0,0,0,0,0,1,0,0,0,0],\
	   [0,0,0,0,1,0,0,0,0,0],\
	   [0,0,0,1,0,0,0,0,0,0],\
	   [0,0,1,0,0,0,0,0,0,0],\
	   [0,1,0,0,0,0,0,0,0,0]]

diag3=[[0,1,0,0,0,0,0,0,0,0],\
	   [1,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0]]

adiag=[[1,0,0,0,0,0,0,0,0,0],\
   	   [0,1,0,0,0,0,0,0,0,0],\
	   [0,0,1,0,0,0,0,0,0,0],\
	   [0,0,0,1,0,0,0,0,0,0],\
	   [0,0,0,0,1,0,0,0,0,0],\
	   [0,0,0,0,0,1,0,0,0,0],\
	   [0,0,0,0,0,0,1,0,0,0],\
	   [0,0,0,0,0,0,0,1,0,0],\
	   [0,0,0,0,0,0,0,0,1,0],\
	   [0,0,0,0,0,0,0,0,0,1]]

test=[[0,0,0,0,1,0,0,0,0,0],\
	  [0,0,0,0,0,1,0,0,0,0],\
	  [0,0,0,0,0,0,1,0,0,0],\
	  [0,0,0,0,0,0,0,1,0,0],\
	  [0,0,0,0,0,0,0,0,1,0],\
	  [0,0,0,0,0,0,0,0,0,1],\
	  [0,0,0,0,0,0,0,0,0,0],\
	  [0,0,0,0,0,0,0,0,0,0],\
	  [0,0,0,0,0,0,0,0,0,0],\
	  [0,0,0,0,0,0,0,0,0,0]]

test1=[[0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [1,1,1,1,1,1,1,1,1,1],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0],\
	   [0,0,0,0,0,0,0,0,0,0]]


class LIF():
	def __init__(self,thresh,reset,c,r):
		self.V_t=thresh
		self.V_r=reset
		self.V=reset
		self.cap=c
		self.res=r
		self.values=[]
		self.train=[]

	def signal(self,I,dt):
		self.V+=(I/self.cap+self.V/self.res)*dt
		self.values.append(self.V)
		if self.V>=self.V_t:
			self.V=self.V_r
			self.train.append(1)
			return
		self.train.append(0)
		return

def convert(train):
	output=[]
	t0=0
	for i in range(len(train)):
		I=0
		if t0!=0:
			I=5*math.exp(-(dt*i-t0)/0.05)
		if train[i]==1:
			t0=i*dt
		output.append(I)
	return output

if __name__=="__main__":
	time=[]
	I=10
	neurons=np.ndarray(shape=(size,size),dtype=object)
	weights=np.ndarray(shape=(size,size),dtype=float)
	detector=LIF(-40,-80,0.01,1)
	picture=adiag
	#initialize weights depending on size of grid
	for i in range(1,size+1):
		for j in range(1,size+1):
			if i+j>size+1:
				weights[i-1,j-1]=1/float(abs(size-((i+j-1)-size)))
				continue
			weights[i-1,j-1]=1/float(i+j-1)
	#initialize LIF neurons
	for i in range(size):
		for j in range(size):
			neurons[i,j]=LIF(-40,-80,0.01,1)
	for t in range(interval):
		time.append(t*dt)
		for i in range(size):
			for j in range(size):
				neurons[i,j].signal(I*picture[i][j],dt)
	for i in range(size):
		for j in range(size):
			neurons[i,j].train=convert(neurons[i,j].train)
	for t in range(interval):
		current=0
		for i in range(size):
			for j in range(size):
				current+=weights[i,j]*neurons[i,j].train[t]
		detector.signal(current,dt)
	count=0
	for i in range(len(time)):
		if detector.train[i]==1:
			count+=1
	print "Fire rate is: ",count/float(interval*dt),"spikes/second"
	plt.plot(time,detector.train,markersize=2)
	plt.show()

