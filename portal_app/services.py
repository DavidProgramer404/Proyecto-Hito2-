from .models import TipoUsuario, Comuna, Region, TipoInmueble, Usuario, Inmueble


# tipoUsuario
def get_tipo_usuarios():
    return TipoUsuario.objects.all()
    


def get_usuarios():
    return Usuario.objects.all()


def crear_tipo_usuario(tipo):
    tipo_usuario = TipoUsuario(tipo_usuario=tipo)
    tipo_usuario.save()
    return tipo_usuario


def actualizar_tipo_usuario(id, nuevo_tipo):
    tipo_usuario = tipo_usuario(id)
    tipo_usuario.tipo_usuario = nuevo_tipo
    tipo_usuario.save()
    return tipo_usuario


def eliminar_tipo_usuario(id):
    tipo_usuario = tipo_usuario(id)
    tipo_usuario.delete()
    return tipo_usuario


# comuna
def get_comunas():
    return Comuna.objects.all()
    


def comuna(id):
    return Comuna.objects.get(id_comuna=id)


def crear_comuna(comuna):
    comuna = Comuna(comuna=comuna)
    comuna.save()
    return comuna


def actualizar_comuna(id, nueva_comuna):
    comuna = comuna(id)
    comuna.comuna = nueva_comuna
    comuna.save()
    return comuna


def eliminar_comuna(id):
    comuna = comuna(id)
    comuna.delete()
    return comuna


# region
def get_regiones():
    return Region.objects.all()
    


def region(id):
    return Region.objects.get(id)
    


def crear_region(region):
    region = Region(region=region)
    region.save()
    return region


def actualizar_region(id, region):
    region = region(id)
    region.region = region
    region.save()
    return region


def eliminar_region(id):
    region = region(id)
    region.delete()
    return region


# tipo inmueble
def get_tipo_inmuebles():
    return TipoInmueble.objects.all()



def tipo_inmueble(id):
    return TipoInmueble.objects.get(id_tipo_inmueble=id)
    


def crear_tipo_inmueble(tipo_inmueble):
    tipo_inmueble = TipoInmueble(tipo_inmueble=tipo_inmueble)
    tipo_inmueble.save()
    return tipo_inmueble


def actualizar_tipo_inmueble(id, inmueble):
    tipo_inmueble = tipo_inmueble(id)
    tipo_inmueble.tipo_inmueble = inmueble
    tipo_inmueble.save()
    return tipo_inmueble


def eliminar_tipo_inmueble(id):
    tipo_inmueble = tipo_inmueble(id)
    tipo_inmueble.delete()
    return tipo_inmueble


# usuario
def get_usuarios():
    return Usuario.objects.all()
    


def usuario(id):
    return Usuario.objects.get(id_usuario=id)



def crear_usuario(nombre, apellido, rut, direccion, telefono, correo, id_tipo_usuario):
    tipo = TipoUsuario(id_tipo_usuario)
    usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        rut=rut,
        direccion=direccion,
        telefono=telefono,
        correo=correo,
        id_tipo_usuario=tipo,
    )
    usuario.save()
    return usuario


def actualizar_usuario(
    id,
    nombre=None,
    apellido=None,
    rut=None,
    direccion=None,
    telefono=None,
    correo=None,
    id_tipo_usuario=None,
):
    usu = usuario(id)
    if nombre:
        usu.nombre = nombre
    if apellido:
        usu.apellido = apellido
    if rut:
        usu.rut = rut
    if direccion:
        usu.direccion = direccion
    if telefono:
        usu.telefono = telefono
    if correo:
        usu.correo = correo
    if id_tipo_usuario:
        tipo = TipoUsuario(id_tipo_usuario)
        usu.id_tipo_usuario = tipo
    usu.save()
    return usu


def eliminar_usuario(id):
    usuario = usuario(id)
    usuario.delete()
    return usuario


# inmuebles
def get_inmuebles():
    return Inmueble.objects.all()
    


def inmueble(id):
    return Inmueble.objects.get(id)
    


def crear_inmueble(
    nombre,
    m2_contruido,
    m2_terreno,
    nro_estacionamiento,
    nro_habitaciones,
    nro_banio,
    direccion,
    precio_arriendo,
    id_usuario,
    id_comuna,
    id_tipo_inmueble,
):
    usuario = usuario(id_usuario)
    comuna = comuna(id_comuna)

    tipo_inmuebles = tipo_inmueble(id_tipo_inmueble)
    inmueble = Inmueble(
        nombre=nombre,
        m2_contruido=m2_contruido,
        m2_terreno=m2_terreno,
        nro_estacionamiento=nro_estacionamiento,
        nro_habitaciones=nro_habitaciones,
        nro_banio=nro_banio,
        direccion=direccion,
        precio_arriendo=precio_arriendo,
        id_usuario=usuario,
        id_comuna=comuna,
        id_tipo_inmueble=tipo_inmuebles,
    )
    inmueble.save()
    return inmueble


def actualizar_inmuble(
    id,
    nombre=None,
    m2_contruido=None,
    m2_terreno=None,
    nro_estacionamiento=None,
    nro_habitaciones=None,
    nro_banio=None,
    direccion=None,
    precio_arriendo=None,
    id_usuario=None,
    id_comuna=None,
    id_tipo_inmueble=None,
):
    inmueble = inmueble(id)
    usuario = usuario(id_usuario)
    comuna = comuna(id_comuna)
    tipo_inmueble = tipo_inmueble(id_tipo_inmueble)
    if nombre:
        inmueble.nombre = nombre
    if m2_contruido:
        inmueble.m2_contruido = m2_contruido
    if m2_terreno:
        inmueble.m2_terreno = m2_terreno
    if nro_estacionamiento:
        inmueble.nro_estacionamiento = nro_estacionamiento
    if nro_habitaciones:
        inmueble.nro_habitaciones = nro_habitaciones
    if nro_banio:
        inmueble.nro_banio = nro_banio
    if direccion:
        inmueble.direccion = direccion
    if precio_arriendo:
        inmueble.precio_arriendo = precio_arriendo
    if id_usuario:
        inmueble.id_usuario = usuario
    if id_comuna:
        inmueble.id_comuna = comuna
    if id_tipo_inmueble:
        inmueble.id_tipo_inmueble = tipo_inmueble
    inmueble.save()

    return inmueble


def eliminar_inmueble(id):
    inmueble = inmueble(id)
    inmueble.delete()
    return inmueble
