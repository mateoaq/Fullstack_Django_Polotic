class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def add(self, producto):
        if str(producto.id) not in self.carrito.keys():
            self.carrito[producto.id] = {
                "producto_id": producto.id,
                "titulo": producto.titulo,
                "cantidad": 1,
                "precio": str(producto.precio),
                "imagen": producto.imagen.url,
                "subtotal": str(producto.precio)
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["subtotal"] = value["cantidad"] * int(value["precio"])
                    break
        
        self.save()

    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.save()

    def decrementar(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["subtotal"] = value["cantidad"] * int(value["precio"])
                self.save()
                if value["cantidad"] < 1:
                    self.remove(producto)
                break
            else:
                print('No hay producto que eliminar')

    def total(self):
        total = 0
        for key, value in self.carrito.items():
            total = int(value["subtotal"]) + total 

        
        return total

    def clear(self):
        self.session['carrito'] = {}
        self.session.modified = True








