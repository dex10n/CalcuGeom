from tkinter import *

root = Tk()
root.title('CalcuGeom')

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
a1 = Entry(root,borderwidth=4,width=21)
a1.grid(column=0,row=0)

b1 = Entry(root,borderwidth=4,width=21)
b1.grid(column=0,row=1)

c1 = Entry(root,borderwidth=4,width=21)
c1.grid(column=2,row=0)

d1 = Entry(root,borderwidth=4,width=21)
d1.grid(column=2,row=1)

text_coords1 = Label(root,text='<--X1                       X2-->')
text_coords1.grid(row=0,column=1)
text_coords2 = Label(root,text='<--Y1                       Y2-->')
text_coords2.grid(row=1,column=1)


#labels para los resultados
ecuacion_result = Label(root)
ecuacion_result.grid(column=2,row=3)

ordenada_resul = Label(root)
ordenada_resul.grid(column=1,row=3)

pendiente_resul = Label(root)
pendiente_resul.grid(column=0,row=3)

#mostrar resultados para la recta
def mostrar_resultados(opcion):
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
boton = Button(root, text='Ecuación de r', command = lambda:mostrar_resultados('ecu'),padx=27,pady=20)
boton.grid(column=2 ,row=2)

boton2 = Button(root, text='Ordenada en el origen',command = lambda:mostrar_resultados('ord'),padx=3.5,pady=20)
boton2.grid(column=1 ,row=2)

boton3 = Button(root, text='Pendiente',command = lambda:mostrar_resultados('pen'),padx=36,pady=20)
boton3.grid(column=0 ,row=2)


root.mainloop()




'''
print('Ingrese las coordenadas del primer punto:')
a=float(x1)
b=float(input('Y: '))
print('Ingrese las coordenadas del segundo punto:')
c=float(input('X: '))
d=float(input('Y: '))
r=Recta((a,b),(c,d))
print('Pendiente:',r.pendiente(),'\nOrdenada:', r.ordenada(),r.ecuacion_recta())


class Circunferencia:
    def __init__(self,coord_centro,radio):
        self.coord_centro=coord_centro
        self.radio=radio

    def ecua_circ(self):
        alfa,beta=self.coord_centro
        r=self.radio
        return f'x^2 + y^2 - {2*alfa}x - {2*beta}y + {alfa**2+beta**2-self.radio**2} = 0'
    

print('Ingrese las coordenadas del punto central de la circunferencia:')
e=float(input('α: '))
f=float(input('β: '))
print('Ingrese el radio de la circunferencia:')
ra=float(input('r: '))
c=Circunferencia((e,f),ra)
print(c.ecua_circ())
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

