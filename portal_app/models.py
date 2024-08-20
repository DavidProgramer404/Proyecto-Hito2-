from django.db import models

# Modelos de tu aplicación
class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=50, null=False)

    class Meta:
        managed = False
        db_table = 'tipo_usuarios'

    def __str__(self):
        return self.tipo_usuario

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    region = models.CharField(max_length=50, null=False)

    class Meta:
        managed = False
        db_table = 'regiones'

    def __str__(self):
        return self.region

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    comuna = models.CharField(max_length=50, null=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comunas'

    def __str__(self):
        return self.comuna

class TipoInmueble(models.Model):
    id_tipo_inmueble = models.AutoField(primary_key=True)
    tipo_inmueble = models.CharField(max_length=50, null=False)

    class Meta:
        managed = False
        db_table = 'tipo_inmuebles'

    def __str__(self):
        return self.tipo_inmueble

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    rut = models.CharField(max_length=12, null=False, unique=True)
    direccion = models.CharField(max_length=100, null=False)
    telefono_personal = models.CharField(max_length=20, null=False)
    correo_electronico = models.EmailField(unique=True, null=False)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, db_column='id_tipo_usuario')

    class Meta:
        managed = False
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    id_inmueble = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField()
    m2_construido = models.FloatField(null=False)
    m2_terreno = models.FloatField(null=False)
    nro_estacionamiento = models.IntegerField()
    nro_habitacion = models.IntegerField()
    nro_banio = models.IntegerField()
    direccion = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    precio_mensual_arriendo = models.FloatField(null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='id_comuna')
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE, db_column='id_tipo_inmueble')

    class Meta:
        managed = False
        db_table = 'inmuebles'

    def __str__(self):
        return self.nombre
