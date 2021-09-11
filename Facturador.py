#Facturador
'''codigo= int(input("Ingrese código de artículo:"))
cantidad= int(input("Cantidad:"))
valor= int(input("Valor Unitario:"))
info = int (input("Desea ingresar otro artículo?: 1. si , 2. no "))


while info==1:
    codigo2= int(input("Ingrese código del segundo artículo:"))
    cantidad2= int(input("Cantidad:"))
    valor2= int(input("Valor Unitario:"))
    break
else:
    *****
          
if codigo==1010:
          total1= round (cantidad* valor)
          subtotal1= round (total1/(1+(16/100)))
          iva1= round (total1-subtotal1)
          
elif codigo2==1020:
          total2= round (cantidad2* valor2)
          subtotal2= round(total2/(1+(19/100)))
          iva2= round (total2-subtotal2)
          print  ("Total: ",(total1+total2), "\nSubtotal: ",(subtotal1 + subtotal2), "\nIva: ", (iva1 + iva2))'''

#CONTRASEÑA
pasword=(input("INGRESE SU CONTRASEÑA\n"))
confirm_pasword=(input("CONFIRME SU CONTRASEÑA\n"))
count=0
if pasword ==(confirm_pasword):
    print("A INICIADO SECION\n")
    exit(0)
while count<=2:
    pasword=input("*** SU CONTRASEÑA NO COINCIDE *** \n INGRESAR SU CONTRASEÑA\n")
    confirm_pasword=(input("CONFIRME SU CONTRASEÑA\n"))
    count= count+1
    if pasword ==(confirm_pasword):
        print("A INICIADO SECION\n")
        break
    else:
        print ("ERROR: SU CONTRASEÑA NO COINCIDE \n *** HASTA PRONTO ***")
        break