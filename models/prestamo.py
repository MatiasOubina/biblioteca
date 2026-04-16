from datetime import datetime, date

class Prestamo:
    def __init__(self, nombre_persona, documento_persona, fecha_prestamo, fecha_devolucion, id_libro, libro_devuelto = False):
        self.nombre_persona = nombre_persona
        self.documento_persona = documento_persona
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.id_libro = id_libro
        self.libro_devuelto = libro_devuelto
    
    def __str__(self):
        devuelto = 'Sí' if self.libro_devuelto else 'No'
        return f"Prestamo(nombre_persona='{self.nombre_persona}', documento_persona='{self.documento_persona}', fecha_prestamo='{self.fecha_prestamo}', fecha_devolucion='{self.fecha_devolucion}', id_libro='{self.id_libro}', libro_devuelto={devuelto})"
    
    def dias_demorado(self):

        if self.libro_devuelto:
            return "El libro ya ha sido devuelto"
        
        fecha_devolucion = datetime.strptime(self.fecha_devolucion, "%Y-%m-%d").date()
        fecha_actual = date.today()
        dias_demorado = (fecha_actual - fecha_devolucion).days
        mensaje = f"Lleva {dias_demorado} días demorado" if dias_demorado > 0 else "No hay demora en la devolución"
        return mensaje