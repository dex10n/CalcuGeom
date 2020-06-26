from tkinter import * 
from tkinter import ttk
  
root = Tk() 
root.title("CalcuGeom") 
tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
  
tabControl.add(tab1, text ='Recta') 
tabControl.add(tab2, text ='Circunferencia') 
tabControl.pack(expand = 1, fill ="both") 
  
class Recta:
    def __init__(self,coord1,coord2):
        self.coord1=coord1
        self.coord2=coord2

    def pendiente(self):
        x1,y1=self.coord1
        x2,y2=self.coord2
        return round((y2-y1)/(x2-x1),2)

    def ordenada(self):
        x1,y1=self.coord1
        m=self.pendiente()
        return round(y1-m*x1,2)

    def ecuacion_recta(self):
        m=self.pendiente()
        n=self.ordenada()
        return f'y = {m}x + {n}'

#labels y entry boxes para las coordenadas de los puntos
a1 = ttk.Entry(tab1,width=21)
a1.grid(column=0,row=0)

b1 = ttk.Entry(tab1,width=21)
b1.grid(column=0,row=1)

c1 = ttk.Entry(tab1,width=21)
c1.grid(column=2,row=0)

d1 = ttk.Entry(tab1,width=21)
d1.grid(column=2,row=1)

text_coords1 = ttk.Label(tab1,text='<--X1                       X2-->',padding=15)
text_coords1.grid(row=0,column=1)
text_coords2 = ttk.Label(tab1,text='<--Y1                       Y2-->')
text_coords2.grid(row=1,column=1)


#labels para los resultados
ecuacion_result = ttk.Label(tab1)
ecuacion_result.grid(column=2,row=3)

ordenada_resul = ttk.Label(tab1)
ordenada_resul.grid(column=1,row=3)

pendiente_resul = ttk.Label(tab1)
pendiente_resul.grid(column=0,row=3)


def mos_res_recta(opcion):
    a=float(a1.get())
    b=float(b1.get())
    c=float(c1.get())
    d=float(d1.get())
    r=Recta((a,b),(c,d))

    if opcion == 'ecu':
        ecuacion_result.configure(text=r.ecuacion_recta())
        return ecuacion_result
    elif opcion == 'ord':
        ordenada_resul.configure(text=r.ordenada())
        return ordenada_resul
    elif opcion == 'pen':
        pendiente_resul.configure(text=r.pendiente())
        return pendiente_resul

#botones
boton = ttk.Button(tab1, text='Ecuación de r', command = lambda:mos_res_recta('ecu'))
boton.grid(column=2 ,row=2, padx=30, pady=20)

boton2 = ttk.Button(tab1, text='Ordenada en el origen',command = lambda:mos_res_recta('ord'))
boton2.grid(column=1 ,row=2, padx=30, pady=20)

boton3 = ttk.Button(tab1, text='Pendiente',command = lambda:mos_res_recta('pen'))
boton3.grid(column=0 ,row=2, padx=30, pady=20)

class Circunferencia:
    def __init__(self,coord_centro,radio):
        self.coord_centro=coord_centro
        self.radio=radio

    def ecua_circ(self):
        alfa,beta=self.coord_centro
        r=self.radio
        return f'x^2 + y^2 - {2*alfa}x - {2*beta}y + {alfa**2+beta**2-self.radio**2} = 0'

#labels y entry boxes para las coordenadas y el radio
e1 = ttk.Entry(tab2,width=21)
e1.grid(column=0,row=0)

f1 = ttk.Entry(tab2,width=21)
f1.grid(column=0,row=1)

g1 = ttk.Entry(tab2,width=21)
g1.grid(column=2,row=0)

text_coords3 = ttk.Label(tab2,text='<--α                       r-->', padding=15)
text_coords3.grid(row=0,column=1)
text_coords4 = ttk.Label(tab2,text='<--β                             ')
text_coords4.grid(row=1,column=1)


#labels para los resultados
ecuacion_result2 = ttk.Label(tab2)
ecuacion_result2.grid(column=1,row=2)

def mos_res_circ():
    e = float(e1.get())
    f = float(f1.get())
    g = float(g1.get())
    c = Circunferencia((e,f),g)
    ecuacion_result2.configure(text=c.ecua_circ())
    return ecuacion_result2

boton = ttk.Button(tab2, text='Ecuación de la \ncircunferencia', command = mos_res_circ)
boton.grid(column=2 ,row=1, padx=30, pady=20)

root.mainloop()   



'''
p=r.pendiente()
o=r.ordenada()
def interseccion(p1,o1,e1,f1,r1):
    a=1+p1**2
    b=2*p1*o1-2*e1-2*f1*p1
    c=-2*f1*o1+o1**2+e1**2+f1**2-r1**2
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    y1=p1*x1+o1
    y2=p1*x2+o1
    return f'Intersección: P1={(x1,y1)}, P2={(x2,y2)}'

print(interseccion(p,o,e,f,ra))
'''

