#Inventario de mapas para Primaria y Profesorado de Geografía e Historia
class Mapa:
    """
    #Clase que representa un mapa educativo.
    Aplica encapsulamiento mediante atributos privados y métodos getters/setters.
    """
    def __init__(self, titulo, fecha, autor, tipo, enlace):
        self.__titulo = titulo      
        self.__fecha = fecha
        self.__autor = autor
        self.__tipo = tipo
        self.__enlace = enlace

    # Aplicar el método getter
    def get_titulo(self):
        return self.__titulo

    def get_fecha(self):
        return self.__fecha

    def get_autor(self):
        return self.__autor

    def get_tipo(self):
        return self.__tipo

    def get_enlace(self):
        return self.__enlace

    # Aplicar el método setter
    def set_titulo(self, nuevo_titulo):
        if len(nuevo_titulo) > 0:
            self.__titulo = nuevo_titulo

    def set_fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha

    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def set_tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    def set_enlace(self, nuevo_enlace):
        self.__enlace = nuevo_enlace

    # Representar el mapa 
    def mostrar_info(self):
        print(f" {self.__titulo} ({self.__fecha})")
        print(f"Autor/a: {self.__autor}")
        print(f"Tipo: {self.__tipo}")
        print(f"Enlace: {self.__enlace}")
        print("-" * 40)
# Clase para el inventario.
class InventarioMapas:
    
    def __init__(self):
        self.__mapas = [] 
     # lista privada

    def agregar_mapa(self, mapa):
        self.__mapas.append(mapa)
        print(f"Mapa '{mapa.get_titulo()}' agregado al inventario.")

    def buscar_por_titulo(self, palabra):
        print(f" Buscando mapas que contengan '{palabra}'...")
        encontrados = [m for m in self.__mapas if palabra.lower() in m.get_titulo().lower()]
        if encontrados:
            for m in encontrados:
                m.mostrar_info()
        else:
            print(" No se encontraron resultados.")

    def listar_todos(self):
        print(" Inventario de mapas:")
        if not self.__mapas:
            print("No hay mapas registrados todavía.")
        for m in self.__mapas:
            m.mostrar_info()

#Ejemplo de uso:
if __name__ == "__main__":
    inventario = InventarioMapas()

    mapa1 = Mapa("Mapa político de Uruguay", "2010", "El uruguayo.com", "Político", "https://www.mapasdeluruguay.eluruguayo.com/mapa-politico.htm")
    mapa2 = Mapa("Uruguay en la Cuenca del Plata", "2025", "Observatorio de la Cuenca del Plata", "Físico-Político", "https://cicplata.org/es/observatorio-de-la-cuenca-del-plata/")
    mapa3 = Mapa("Uruguay de 1936", "1936", "Mapas de Uruguay.com", "Histórico", "https://mapasdeuruguay.com/mapa-tematico-ilustrado-de-uruguay-1936-gigante/")
    mapa4 = Mapa("Red ferroviaria del siglo XIX en Uruguay", "1897", " Biblioteca Nacional de Uruguay", "Histórico", "http://bibliotecadigital.bibna.gub.uy:8080/jspui/handle/123456789/32190?mode=full")
    inventario.agregar_mapa(mapa1),
    inventario.agregar_mapa(mapa2),
    inventario.agregar_mapa(mapa3),
    inventario.agregar_mapa(mapa4)

    inventario.listar_todos()
    inventario.buscar_por_titulo("Uruguay")