## ejemplo ciclo for 
nombre = str(input("Ingrese su nombre: ")); 
edad = int(input("Ingrese su edad: ")); 
edad_lista = []; 
aux = 0; 

while aux < edad:
    aux = aux + 1; 
    edad_lista.append(aux); 


for i in edad_lista: 
    print(i); 


## ejemplo con range 

lista_range = list(range(10));
print(lista_range[0]);
print(lista_range); 

lista_dos = list(range(2,6)); 
print(lista_dos); 