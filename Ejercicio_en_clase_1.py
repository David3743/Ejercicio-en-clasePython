#Primer ejercicio, aca se guardan las listas de los paises
paises = ["Turquia", "Japon", "Korea del sur", "Korea del norte", "Brazil", "Estados Unidos", "Panama", "Jamaica"]
print(paises)
#Aca de odenan de manera alfabetica
A=sorted(paises)
print(A)
#Aca se imprime en orden alfabetico inverso
A.sort(reverse=True)
print(A)
#Aca se utiliza reverse en la lista original
paises.reverse()
print(paises)
#Aca se vuelve al estado original
paises.reverse()
print(paises)
#Aca se utiliza el sort
paises.sort()
print(paises)
#Aca se utiliza sort para guardar en orden alfabetico inverso
paises.sort(reverse=True)
print(paises)

