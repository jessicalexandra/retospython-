from datetime import datetime
fecha = input("ingresa la fecha (año/mes/dia): ")
fecha = datetime.strptime(fecha, "%Y/%m/%d")
dia = fecha.day
mes = fecha.month
anio=fecha.year


if (mes==3 and dia >=20) or mes==4 or mes==5 or  (mes==6 and dia<=20) :
    print("Es primavera")
if (mes==6 and dia >=21) or mes==7 or mes==8 or (mes==9 and dia<=22) :
    print("Es verano")
if (mes==9 and dia >=23) or mes==10 or mes==11 or (mes==12 and dia<=21) :
    print("Es otoño")
if (mes==12 and dia >=22) or mes==1 or mes==2 or (mes==3 and dia<=19) :
    print("Es invierno")
    
    
    
    
    
    
