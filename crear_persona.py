from persona import persona 

esteban = persona("esteban", "calderon", 16)
esteban.mostrarPersona()

leidy = persona("Leidy", "perez", 18)
leidy.mostrarPersona()

leidy.apellidos = "perez"
leidy.mostrarPersona()

juan = leidy 

juan.mostrarPersona()
