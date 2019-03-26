import matplotlib.pyplot as plt
import math

dt=0.001
w_max=10
interval=1000

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

def trace(train):
	output=[]
	x=0
	for i in range(len(train)):
		x+=(-x+50*train[i])*dt/0.07
		output.append(x)
	return output

def A_plus(w):
	return (w_max-w)*1.3

def A_minus(w):
	return w*1.3


if __name__=="__main__":
	w_a=0.1
	w_b=0.1
	I_t=8
	for z in range(10):
		for q in range(4):
			print q
			a=LIF(-40,-80,0.01,1)
			b=LIF(-40,-80,0.01,1)
			OR=LIF(-40,-80,0.01,1)
			teacher=LIF(-40,-80,0.01,1)
			time=[]
			train_a=[]
			train_b=[]
			train_or=[]
			if q==0:
				I_a=8
				I_b=8
			elif q==1:
				I_a=3
				I_b=8
			elif q==2:
				I_a=8
				I_b=3
			else:
				I_a=3
				I_b=3
				I_t=-8
			for i in range(interval):
				time.append(i*dt)
				train_a.append(a.signal(I_a,dt))
				train_b.append(b.signal(I_b,dt))
			out_a=trace(train_a)
			out_b=trace(train_b)
			for k in range(1000):
				train_or=[]
				for i in range(interval):
					train_or.append(OR.signal(w_a*out_a[i]+w_b*out_b[i]+I_t,dt))
					out_or=trace(train_or)
					w_a+=((A_plus(w_a)*out_a[i]*train_or[i])-(A_minus(w_a)*out_or[i]*train_a[i]))*dt
					w_b+=((A_plus(w_b)*out_b[i]*train_or[i])-(A_minus(w_b)*out_or[i]*train_b[i]))*dt
		
	plt.plot(time,train_or,markersize=2)	
	plt.ylabel('Current')
	plt.xlabel('Time')
	plt.show()
	print w_a
	print w_b
		
