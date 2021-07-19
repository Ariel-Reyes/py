## Arreglos 

numero = ["Ariel",20,"Santa Barbara", 1.70, 1601, ["Fernando",21]]; 
print(numero[0]*2); 
print(numero[5][0]);
print(numero+["A",2]); 



print(1601 in numero); 


if "Ariel" in numero:
    print("Si esta");
else: 
    print("No esta"); 
    

print("Ariel" not in numero);  


## con append se agrega 
numero.append("oz"); 
print(numero); 
## con len se le saca la longitud a la lista 
print(len(numero)); 

numero.insert(2,22);
print(numero); 

print(numero.index("Ariel")); 