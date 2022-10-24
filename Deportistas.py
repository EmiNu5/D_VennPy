# -*- coding: utf-8 -*-
"""
En una comunidad de 100 deportistas se sabe que 30 de ellos entrenan fútbol, 50 entrenan squash 
y 60 entrenan tenis. 22 entrenan tenis y fútbol, 30 entrenan squash y tenis y 15 entrenan squash y fútbol. 
Si 10 deportistas entrenan los tres deportes 
1-¿cuántos entrenan sólo tenis?
2-¿cuántos entrenan sólo fútbol?
3-¿cuántos entrenan sólo squash?
4-¿cuántos entrenan tenis o fútbol?
"""


lista_futbol = [3, 5, 10, 12]
tupla_squash = (10, 20, 15, 5)
diccio_tenis = {"infantil": 12,  "juniors": 10,
                "adolescentes": 20, "adultos": 18}



# Controlamos que la lista de fulbol contenga 30 personas
# Controlamos que la lista de squash contenga 50 personas
# Controlamos que la lista de tenis  contenga 60 personas

set_futbol = set(lista_futbol)
set_squash = set(tupla_squash)
set_tenis = set(diccio_tenis.values())
    
print(f"Conj futbol: {set_futbol}\n Total {sum(set_futbol)}")
print(f"Conj squash: {set_squash}\n Total {sum(set_squash)}")
print(f"Conj tenis: {set_tenis}\n Total {sum(set_tenis)}")

# 22 entrenan tenis y fútbol
# 30 entrenan squash y tenis 
# 15 entrenan squash y fútbol

tyf = (set_tenis & set_futbol)
print(f"Entrenan tenis y futbol: set:{tyf} {sum(tyf)}")
syt = (set_squash & set_tenis)
print(f"Entrenan squash y tenis: set:{syt} {sum(syt)}")
syf = (set_squash & set_futbol)
print(f"Entrenan squash y futbol: set:{syf} {sum(syf)}")
# 10 deportistas entrenan los tres deportes 
def los_tres(conj1,conj2,conj3):
    intersec = (conj1 & conj2 & conj3)
    return intersec
f_s_t = los_tres((set_futbol), (set_squash), (set_tenis))
print(f"Entrenan los 3 deportes: set:{f_s_t} {sum(f_s_t)}")
print("\n")
# 1-¿cuántos entrenan sólo tenis?
# 2-¿cuántos entrenan sólo fútbol?
# 3-¿cuántos entrenan sólo squash?
# 4-¿cuántos entrenan tenis o fútbol?   
 
def solo_uno(conj1,conj2,conj3):
    intersec = ((conj1 - conj2) - conj3)
    return intersec
def las_dos(conj1,conj2,conj3):
    intersec= ((conj1 & conj2) - conj3)
    return intersec
solo_t = solo_uno(set_tenis, set_squash, set_futbol)
print(f"Entrenan solo tenis: set:{solo_t} {sum(solo_t)}")
solo_f = solo_uno(set_futbol, set_squash, set_tenis)
print(f"Entrenan solo futbol: set:{solo_f } {sum(solo_f )}")
solo_s = solo_uno(set_squash, set_futbol, set_tenis)
print(f"Entrenan solo squash: set:{solo_s  } {sum(solo_s )}")

def conj1_o_conj2(conj1, conj2):
     union = (conj1 ^ conj2)
#  Retorna un nuevo conjunto el cual contiene los elementos 
#  que pertenecen a alguno de los dos conjuntos que participan
 # en la operación pero no a ambos
     return union
t_o_f = conj1_o_conj2(set_futbol,set_tenis)
print(f"Entrenan tenis o fútbol:{t_o_f } {sum(t_o_f )}") 

# Definir
Universo = 100
ninguno = Universo -(sum(solo_f) + sum(solo_s) + sum(solo_t) +sum(tyf) -sum(f_s_t)+ sum(syf)-sum(f_s_t) + sum(syt)-sum(f_s_t)+ sum(f_s_t))
                     
# In[ ] 
# GRAFICO
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles  
# importamos de matplotlib_venn, el módulo venn3, que
# tiene implementado clases, funciones, métodos, etc,
# para generar diagramas de Venn para 3 conjuntos. 

# BASE DE FIGURA: 

fig = plt.figure(figsize=(10,5), facecolor='ivory')

# ETIQUETAS:

diagram = venn3((1, 1, 1, 1, 1, 1, 1),set_labels=('Tenis', 'Futbol','Squash'))
diagram.get_label_by_id('100').set_text(sum(solo_t))
diagram.get_label_by_id('010').set_text(sum(solo_f))
diagram.get_label_by_id('001').set_text(sum(solo_s))
diagram.get_label_by_id('110').set_text(sum(tyf) -sum(f_s_t))
diagram.get_label_by_id('011').set_text(sum(syf)-sum(f_s_t))
diagram.get_label_by_id('101').set_text(sum(syt)-sum(f_s_t))
diagram.get_label_by_id('111').set_text(sum(f_s_t))

# ESCRITURA EN GRAFICO:

plt.text(-1.10, -0.20,s="RESPUESTAS " + str(), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.3),))
plt.text(-1.10, -0.40,s="Entrenan solo tenis: "+ str(sum(solo_t)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.10, -0.60,s="Entrenan solo squash: "+ str(sum(solo_s )), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.10, -0.50,s="Entrenan sólo fútbol: " + str(sum(solo_f)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.10, -0.70,s="Entrenan tenis o fútbol: "+str(sum(t_o_f )), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.6, 0.,s="Universo: " + str(Universo), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.3),))
plt.text(0.6, -0.10,s="Sin Categoria: " + str(ninguno), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.3),))


# LINEAS DE CONJUNTOS:

c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1),color="grey", alpha=1, linestyle="-",linewidth=3)
c[0].set_lw(1.0)
c[1].set_lw(1.0)
c[2].set_lw(1.0)

# TITULO:

plt.title("Comunidad deportistas")

# RECUADRO:

plt.axis('on')
# FIN:
plt.show()





 
 
 
 
 
 
 
 
