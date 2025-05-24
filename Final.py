def revisar_chocolate():
    # ---------------------------INCIO DE LOS CONTADORES-----------------#
    aprobados = 0
    rechazados = 0
    rechazo_tamaño = 0
    rechazo_forma = 0
    rechazo_sabor = 0

    #---------- PEDIMOS CUÁNTOS CHOCOLATES SE REVISARAN-------------------#
    cantidad = int(input("¿Cuántos chocolates se revisarán? "))

    #---------- INICIAR UN CONTADOR MANUAL--------------------------------#
    contador = 1

    #----------INCICIAR REVISION DE CHOCOLATES----------------------------#
    while contador <= cantidad:
        print("Chocolate", contador)

        tamaño = input("¿El tamaño es correcto? (si/no): ")
        forma = input("¿La forma es correcta? (si/no): ")
        sabor = input("¿El sabor es correcto? (si/no): ")

        if tamaño == "si" and forma == "si" and sabor == "si":
            print("Chocolate Aprobado ✅")
            aprobados = aprobados+ 1
        else:
            print("Chocolate Rechazado ❌")
            rechazados = rechazados+ 1

            if tamaño == "no":
                rechazo_tamaño = rechazo_tamaño + 1
            if forma == "no":
                rechazo_forma =rechazo_forma+ 1
            if sabor == "no":
                rechazo_sabor =rechazo_sabor+ 1

        contador = contador+ 1
    #----------------CALCULAR LOS PORCENTAJES------------------------=
    
    if cantidad>0 :
        porcentaje_tamaño   = (rechazo_tamaño / cantidad) *100
        porcentaje_forma    = (rechazo_forma  / cantidad) *100
        porcentaje_sabor    = (rechazo_sabor / cantidad ) *100
        
    else:
        porcentaje_tamaño = porcentaje_forma = porcentaje_sabor=0
    
   #-----------------------------------------------------------------#
   # ---------------------- MOSTRAR RESULTADOS ----------------------
    print("\n------------------ RESUMEN FINAL ------------------")
    print("Chocolates Aprobados:", aprobados)
    print("Chocolates Rechazados:", rechazados)
    print("Motivos de Rechazo:")
    print("- Tamaño incorrecto:" , rechazo_tamaño,"chocolates",round(porcentaje_tamaño),"%")
    print("- Forma incorrecta:" , rechazo_forma,"chocolates",round(porcentaje_forma),"%" )
    print("- Sabor incorrecto:" , rechazo_sabor, "chocolates",round(porcentaje_sabor),"%")
    
    
        # ---------------------- ALERTA SI HAY MUCHOS RECHAZOS ----------------------
    if cantidad > 0 and rechazados / cantidad > 0.5:
        print("\n⚠️  Alerta: Más del 50% del lote fue rechazado.")
        print("   Se recomienda revisar urgentemente el proceso de producción.")



    #---------------LLAMAR A LA FUNCION----------------#
revisar_chocolate()
