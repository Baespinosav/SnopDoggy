from urllib import request
from django.shortcuts import redirect, render
from .models import Vehiculo, Categoria, categoriaProducto, manProducto
from .forms import VehiculoForm, ManProdForm

# Create your views here.

def index(request):
    return render(request, "core/index.html")



def login(request):
    return render(request, "core/login.html")

def loginadmin(request):
    return render(request, "core/login_admin.html")    


def registro(request):
    return render(request, "core/registro.html")

def about(request):
    return render(request, "core/about.html")

def all_facturas(request):
    return render(request, "core/all_facturas.html")

def all_products(request):
    return render(request, "core/all_products.html")

def carrito(request):
    return render(request, "core/carrito.html")

def contact(request):
    return render(request, "core/contact.html")

def edit_product(request):
    return render(request, "core/edit_product.html")

def editadmin(request):
    return render(request, "core/editadmin.html")

def facture(request):
    return render(request, "core/facture.html")

def ficha_product1_admin(request):
    return render(request, "core/ficha_product1_admin.html")

def ficha_product1_client(request):
    return render(request, "core/ficha_product1_client.html")

def ficha_product2_admin(request):
    return render(request, "core/ficha_product2_admin.html")

def ficha_product2_client(request):
    return render(request, "core/ficha_product2_client.html")

def ficha_product3_admin(request):
    return render(request, "core/ficha_product3_admin.html")

def ficha_product3_client(request):
    return render(request, "core/ficha_product3_client.html")

def ficha_product4_admin(request):
    return render(request, "core/ficha_product4_admin.html")

def ficha_product4_client(request):
    return render(request, "core/ficha_product4_client.html")

def ficha_product5_admin(request):
    return render(request, "core/ficha_product5_admin.html")

def ficha_product5_client(request):
    return render(request, "core/ficha_product5_client.html")

def ficha_product6_admin(request):
    return render(request, "core/ficha_product6_admin.html")


def ficha_product6_client(request):
    return render(request, "core/ficha_product6_client.html")


def Historial_de_compra(request):
    return render(request, "core/Historial_de_compra.html")


def historial_ventas(request):
    return render(request, "core/historial_ventas.html")


def impFactura(request):
    return render(request, "core/impFactura.html")


def index_admin(request):
    return render(request, "core/index_admin.html")


def index(request):
    return render(request, "core/index.html")


def login_admin(request):
    return render(request, "core/login_admin.html")


def login(request):
    return render(request, "core/login.html")


def man_bod(request):
    return render(request, "core/man_bod.html")



def mon_compra(request):
    return render(request, "core/mon_compra.html")


def perfil(request):
    return render(request, "core/perfil.html")


def price(request):
    return render(request, "core/price.html")


def product_admin(request):
    return render(request, "core/product_admin.html")


def product_anon(request):
    return render(request, "core/product_anon.html")


def product_client(request):
    return render(request, "core/product_client.html")


def registro_usuarios(request):
    return render(request, "core/registro_usuarios.html")


def home(request):
    return render(request, "core/home.html")
    
def poblar_bd(request):
    return render(request, "core/poblar_bd.html")

def vehiculo(request):
    return render(request, "core/vehiculo.html")

def vehiculo_tienda(request):
    return render(request, "core/vehiculo_tienda.html")

def vehiculo_ficha(request):
    return render(request, "core/vehiculo_ficha.html")

def index(request):
    return render(request, "core/index.html")

def man_prod(request):
    return render(request, "core/man_prod.html")

def useradmin(request):
    return render(request, "core/useradmin.html")



#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#----------------------------MANTENEDOR-----------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

def mockadmin(request, action, id):
    data = {"mesg": "", "form": ManProdForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = ManProdForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El Producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos Productos con la misma patente!"

    elif action == 'upd':
        objeto = manProducto.objects.get(id=id)
        if request.method == "POST":
            form = ManProdForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El Producto fue actualizado correctamente!"
        data["form"] = ManProdForm(instance=objeto)

    elif action == 'del':
        try:
            manProducto.objects.get(id=id).delete()
            data["mesg"] = "¡El Producto fue eliminado correctamente!"
            return redirect(mockadmin, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El Producto ya estaba eliminado!"

    data["list"] = manProducto.objects.all().order_by('id')
    return render(request, "core/mockadmin.html", data)

    #---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------




def vehiculo_tienda(request):
    data = {"list": Vehiculo.objects.all().order_by('patente')}
    return render(request, "core/vehiculo_tienda.html", data)

def vehiculo_ficha(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    data = {"vehiculo":  vehiculo}
    return render(request, "core/vehiculo_ficha.html", data)

def vehiculo(request, action, id):
    data = {"mesg": "", "form": VehiculoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = VehiculoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El vehículo fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos vehículos con la misma patente!"

    elif action == 'upd':
        objeto = Vehiculo.objects.get(patente=id)
        if request.method == "POST":
            form = VehiculoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El vehículo fue actualizado correctamente!"
        data["form"] = VehiculoForm(instance=objeto)

    elif action == 'del':
        try:
            Vehiculo.objects.get(patente=id).delete()
            data["mesg"] = "¡El vehículo fue eliminado correctamente!"
            return redirect(vehiculo, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El vehículo ya estaba eliminado!"

    data["list"] = Vehiculo.objects.all().order_by('patente')
    return render(request, "core/vehiculo.html", data)


def poblar_bd(request):
    Vehiculo.objects.all().delete()
    Vehiculo.objects.create(patente="ALAN67", marca='Volvo', modelo="Volvo Station Wagon", imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="BILL88", marca='Saleen', modelo="S7", imagen="images/saleen.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="ELVI54", marca='Shelby', modelo="Cobra de 1967", imagen="images/cobra.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="FEDE84", marca='Mercedes-Benz', modelo="Pagoda de 1972", imagen="images/pagoda.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="JEFF46", marca='Ford', modelo="Wolf WR1 Ford Race Car", imagen="images/wolf.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="JOHN80", marca='Ford', modelo="Flathead Roadster de 1932", imagen="images/flathead.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="PAUL62", marca='Rolls-Royce', modelo="Phantom", imagen="images/phantom.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="SCAR47", marca='Mustang', modelo="Mustang de 1970", imagen="images/mustang.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="TIRO98", marca='Mercedes-Benz', modelo="Iron Bike de 1998", imagen="images/motoiron.jpg", categoria=Categoria.objects.get(idCategoria=3))
    Vehiculo.objects.create(patente="UVAM20", marca='Silver Plus', modelo="Silver de 2000", imagen="images/silver.jpg", categoria=Categoria.objects.get(idCategoria=3))
    return redirect(vehiculo, action='ins', id = '-1')
