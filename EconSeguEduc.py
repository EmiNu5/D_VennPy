# -*- coding: utf-8 -*-
"""
En una zona del país, se realizó una encuesta de opinión a 1000 personas sobre 3 (tres)
categorías: Economía, Educación y Seguridad, y otras sub-categorías especificadas
sólo para Economía. Los datos se recolectaron en las siguientes estructuras:
    
En relación a los datos obtenidos:
    1) realizar las operaciones correspondientes
    2) realizar el gráfico en networkx
    3) Responder en el gráfico las siguientes preguntas:
        a. cuántos opinaron sobre Seguridad, Educación y Economía.
        b. cuántos opinaron sobre sólo Economía y Educación?
        c. cuántos opinaron sobre sólo Economía?
        d. cuántos opinaron sobre solo Seguridad?
        e. cuántos opinaron sobre sólo Educación? 
        f. cuántos opinaron sobre 2 de las 3 categorías?
"""
# In[ ]:

# 680 opinaron sobre Ecomomía.
Economia = {"Gasto_público": 40, "Impuestos": 118, "Política_y_gobierno": 50, "Deuda_externa": 95,
              "Privilegios": 56, "Corrupción":  131, "Obra_pública": 103, "Planes": 87}
# 320 opinaron sobre Seguridad.
Seguridad = (40, 50, 60, 75, 34, 61)
# 490 opinaron sobre Educación
Educacion = [34, 40, 61, 75, 87, 90, 103]



set_econ=set(Economia.values())
set_segu=set(Seguridad)
set_educ=set(Educacion)

# def suma(arg):
#     acum = 0
#     for i in arg:
#         acum = acum + i
#     return acum

print(f"{set_econ}\n Total {sum(set_econ)}")
print(f"{set_segu}\n Total {sum(set_segu)}")
print(f"{set_educ}\n Total {sum(set_educ)}")
def las_tres(conj1,conj2,conj3):
    intersec =(conj1 & conj2 & conj3 )
    return intersec

def las_dos(conj1,conj2,conj3):
    intersec= ((conj1 & conj2) - conj3)
    return intersec

def solo_uno(arg1,arg2,arg3):
    solo = ((arg1 - arg2)-arg3)
    return solo 
def dos_de_tres(cat1_si, cat2_si, cat_no):
    dos_tercios = (cat1_si | cat2_si) - cat_no
    return dos_tercios
def una_de_tres(cat1_si, cat2_no, cat_no):
    un_tercio = (cat1_si - cat2_no - cat_no)
    return un_tercio
# a. cuántos opinaron sobre Seguridad, Educación y Economía.
eco_seg_edu = las_tres(set_econ, set_segu,set_educ)
print(f"Opinaron sobre Seguridad, Educación y Economía \n Set:{eco_seg_edu} Total {sum(eco_seg_edu)}")
# b. cuántos opinaron sobre sólo Economía y Educación?
eco_edu = las_dos(set_econ,set_educ,eco_seg_edu)
print(f"Opinaron sobre solo Economía y Educación \n Set:{eco_edu} Total {sum(eco_edu)}")
# inventado: Cuantos opinaron sore educacion y seguridad?
edu_seg= las_dos(set_segu, set_educ, eco_seg_edu)
print(f"Opinaron sobre solo seguridad y Educación \n Set:{edu_seg} Total {sum(edu_seg)}")
# inventado: Cuantos opinaron sore economia y seguridad?
eco_seg= las_dos(set_econ, set_segu, eco_seg_edu)
print(f"Opinaron sobre solo seguridad y economia \n Set:{eco_seg} Total {sum(eco_seg)}")
# c. cuántos opinaron sobre sólo Economía?
solo_econ = solo_uno(set_econ,set_segu,set_educ)
print(f"Opinaron sobre solo sobre sólo Economia \n Set:{solo_econ} Total {sum(solo_econ)}")
# d. cuántos opinaron sobre solo Seguridad?
solo_seg = solo_uno(set_segu,set_econ,set_educ)
print(f"Opinaron sobre solo sobre solo Seguridad \n Set:{solo_seg} Total {sum(solo_seg)}")
# e. cuántos opinaron sobre sólo Educación? 
solo_educ = solo_uno(set_educ,set_segu,set_econ)
print(f"Opinaron sobre solo sobre solo Educacion \n Set:{solo_educ} Total {sum(solo_educ)}")
# f. cuántos opinaron sobre 2 de las 3 categorías?
dos_d_tres = dos_de_tres(set_econ, set_segu, set_educ) | dos_de_tres(set_segu, set_educ, set_econ) | dos_de_tres(set_educ, set_econ, set_segu)
print(f"Opinaron sobre 2 de las 3 categorias \n Set:{dos_d_tres} Total {sum(dos_d_tres)}")
# inventado cuántos opinaron sobre 1 de las 3 categorías?
una_d_tres = una_de_tres(set_econ, set_segu, set_educ) | una_de_tres(set_segu, set_educ, set_econ) | una_de_tres(set_educ, set_econ, set_segu)
print(f"Opinaron sobre 1 de las 3 categorias \n Set:{una_d_tres} Total {sum(una_d_tres)}")
# inventado cuantos estan afuera del universo?
union_conjuntos= (solo_econ)

Universo = 1000
Sin_grupo = Universo - sum(solo_econ)-sum(solo_educ)-sum(solo_seg) -sum(edu_seg)-sum(eco_edu)-sum(eco_seg)-sum(eco_seg_edu)

# In[ ]:

# IMPORTS:   
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles  
# importamos de matplotlib_venn, el módulo venn3, que
# tiene implementado clases, funciones, métodos, etc,
# para generar diagramas de Venn para 3 conjuntos.  !!

# BASE DE FIGURA: 

fig = plt.figure(figsize=(10,5), facecolor='ivory')

# ETIQUETAS:

diagram = venn3((1, 1, 1, 1, 1, 1, 1),set_labels=('Economia', 'Seguridad','Educacion'))
diagram.get_label_by_id('100').set_text(sum(solo_econ))
diagram.get_label_by_id('010').set_text(sum(solo_seg))
diagram.get_label_by_id('001').set_text(sum(solo_educ))
diagram.get_label_by_id('110').set_text(sum(eco_seg))
diagram.get_label_by_id('011').set_text(sum(edu_seg))
diagram.get_label_by_id('101').set_text(sum(eco_edu))
diagram.get_label_by_id('111').set_text(sum(eco_seg_edu))

# ESCRITURA EN GRAFICO:

plt.text(-1.70, -0.20,s="RESPUESTAS " + str(), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.3),))
plt.text(-1.70, -0.40,s="Opinaron sobre Seguridad, Educación y Economía " + str(sum(eco_seg_edu)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.70, -0.50,s="Opinaron sobre solo Economía y Educación " + str(sum(eco_edu)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.70, -0.60,s="Opinaron sobre solo seguridad y Educación " + str(sum(edu_seg)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.70, -0.70,s="Opinaron sobre solo seguridad y economia " + str(sum(eco_seg)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.70, -0.80,s="Opinaron sobre solo sobre sólo Economia " + str(sum(solo_econ)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.70, -0.90,s="Opinaron sobre solo sobre solo Seguridad  " + str(sum(solo_seg)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.70, -1.00,s="Opinaron sobre solo sobre solo Educacion" + str(sum(solo_educ)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.70, -1.10,s="Opinaron sobre 2 de las 3 categorias" + str(sum(dos_d_tres)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(-1.70, -1.20,s="Opinaron sobre 1 de las 3 categorias" + str(sum(una_d_tres)), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.8),))
plt.text(0.6, 0.,s="Total escuestados: " + str(Universo), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.3),))
plt.text(0.6, -0.10,s="Sin Categoria: " + str(Sin_grupo), size=10, ha="left", va="bottom",bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5),fc=(1.0, 0.9, 0.3),))


# LINEAS DE CONJUNTOS:

c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1),color="grey", alpha=1, linestyle="-",linewidth=3)
c[0].set_lw(1.0)
c[1].set_lw(1.0)
c[2].set_lw(1.0)

# TITULO:

plt.title("Encuesta de opinión:")

# RECUADRO:

plt.axis('on')
# FIN:
plt.show()




