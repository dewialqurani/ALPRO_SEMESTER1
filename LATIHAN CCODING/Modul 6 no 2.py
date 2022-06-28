def expNumber(x,n):
      if n== 0:
      	return 1
      elif n==1:
      	return x
      else:
      	return x * expNumber(x,n-1)

x = int(input("Masukan angka : "))
n = int(input("Masukan pangkat : "))
hasil=expNumber(x,n)
print(x," pangkat ",n," = ",hasil)