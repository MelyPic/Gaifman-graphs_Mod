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
	if 0 <= i < len(x) and 1 <= m < len(x): 
		#j in (m, i) Dim(j-1,m-1) +dxjxi(j,i)
		minm = Dim(m-1,m-1) + dxjxi(m,i)
		for j in range(m+1,i):
			aux = Dim(j-1,m-1) + dxjxi(j,i)
			if aux < minm:
				minm = aux
		return minm
	elif m == 0:
		return 0
	else:		
		print('Sale de rango, i,m: ', i,m)
		return -1	
		
def dx1xi(i):
	#print('dx1xi: ',i)
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
	
def Bim(i,m):
	arrayD = []
	for j in range(m,i):
		arrayD.append(Dim(j-1,m-1)+ dxjxi(j,i))
	print (arrayD)
	if arrayD ==[]:
		return 0
	else:
		return np.argmin(arrayD, axis=0)	
	#argmin = Dim(m-1,m-1) + dxjxi(m-1,i)
	#print ('argmin: ',argmin)
	#for j in range(m+1,i):
	#	aux = Dim(j-1,m-1) + dxjxi(j,i)
	#	if aux < argmin:
	#		argmin = aux
	#return argmin
	

x=[]	
def main():
	global x
	X = [25, 1 ,20, 1, 10, 10]
	x = X
	x.sort()
	print ('x:',x)
	k = 2 #clusters

	n = len(x)
	#minaux= Dim[1,1]
	#for i in (1,n):
	#	for m in (1,k):
	#		aux = Dim[i,m]
	#		if aux < minaux:
	#			minaux = aux
				
	#llena matrix B
	B = []
	D = []
	for i in range(1,n):
		B.append([])
		D.append([])
		for m in range(1,k):
			#B[i-1].append(m) 
			#print('i,m: ',i,m)
			D[i-1].append(Dim(i,m))
			B[i-1].append(Bim(i,m))
	print ('X: ',X)		
	print ('D: ',D)
	print ('B: ')
	for i in B:
		print(i)
	#print(Dim(n,k))
	
main()	
	
#j el indice de menor numero en el cluster m, en una solución opcional D[i,m].
#Es evidente que D[j-1,m-1]
