'''
x[i]: array of n numbers
m:clusters
D: matrix n+1 * m+1
B: matrix n * k

assignar las entradas de X a los m clusters, tales que
se minimiza la suma (withinss) de los cuadrados de las
distancias dentro del cluster de cada elemento a su
correspondiente media del cluster. =
'''
import numpy as np

def Dim(i,m):
	#0 <= i < len(x) and 1 <= m < len(x):
	minm = B[m-1][m-1] + dxjxi(m,i)
	#minm = Dim(m-1,m-1,B) + dxjxi(m,i)
	for j in range(m+1,i):
		aux = B[j-1][m-1] + dxjxi(j,i)#Dim(j-1,m-1) + dxjxi(j,i)
		if aux < minm:
			minm = aux
	B[i][m] = minm		
	return minm
	
		
def dx1xi(i):
	if i ==0:
		return 0
	else:
		return dx1xi(i-1)+ ((i-1/i)* pow(x[i]-miu(i-1),2))
	
	
def dxjxi(j,i): #j < i
	print('dxjxi: ',j,i)
	if j==i :
		return 0
	elif j < i:
		return dx1xi(i)- dx1xi(j)
	else:
		return dx1xi(j)- dx1xi(i)
	
		
def miu(i):
	if i == 0:
		return 0
	else:
		return (x[i]+(i-1)*miu(i-1))/i
	
#def Bim(i,m):
	#arrayD = []
	#for j in range(m,i):
		#arrayD.append(Dim(j-1,m-1)+ dxjxi(j,i))
	#if arrayD ==[]:
		#return 0
	#else:
		#return np.argmin(arrayD, axis=0)	

	

x=[]
B=[]
	
def main():
	global x
	X = [25, 1 ,20, 1, 10, 10]
	x = X
	x.sort()
	print ('x:',x)
	
	k = 2 #clusters
	n = len(x)
	
	for r in range(len(x)):
		B.append([0]*k) 
	
	
	for i in range(n):
		for m in range(1,k):
			Dim(i,m)
			
	for i in B:
		print(i)
	
main()	
	
#j el indice de menor numero en el cluster m, en una solución opcional D[i,m].
#Es evidente que D[j-1,m-1]
