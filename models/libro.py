class Libro:
    def __init__(self, titulo, autor, isbn, paginas, id= None, estado = "por leer", reseña = None):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.id = id
        self.estado = estado
        self.reseña = reseña

    def __str__(self):
        reseña_texto = 'Sin reseña' if self.reseña is None else self.reseña
        return f"Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', isbn='{self.isbn}', paginas={self.paginas}, estado='{self.estado}', reseña='{reseña_texto}'))"