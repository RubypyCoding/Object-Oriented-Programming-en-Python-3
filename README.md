
## Atributos de una clase

Cuando se trabajan con clases es recomendable crear atributos ocultos y utilizar métodos específicos para acceder a los mismos para establecer, obtener o borrar la información. 

Los métodos `getters` y `setters` son responsables de obtener o retornar el valor de una variable (getter) y de asignar un valor a una variable (setter).


#### Atributo privado

Un guión bajo `_` al principio es usado para denotar `variables privadas` en Python. El uso de este guión bajo `_` es solo por convención, por si solo no restringe que se pueda acceder el atributo desde afuera de la clase. Nos sugiere la idea de que el atributo debería ser oculto, pero no hace engorroso poder accederlo en caso de necesitarlo, asimismo también nos indica que no deberíamos acceder a esas variables, aunque técnicamente no haya nada que nos lo impida.

```python
class Car:

  def __init__(self, brand, color, year):
      #variable privada
  	  self._year = year


car_1 = Car("MiniCooper", "Blue", "2017")

print(car_1._year)
#>> 2017
```

#### Atributo oculto

El uso de doble guión bajo `__` al principio es usado para denotar `variables ocultas` en Python. Aún usando atributos ocultos sigue siendo posible acceder a la variable. Tan sólo se ha hecho un poco más difícil. Podemos acceder a ella a tráves de `_clase__attr`, donde `clase` es el nombre de la clase actual y `attr` el nombre de la variable.

```python
class Car:

  def __init__(self, brand, color, year):
      #variable privada
  	  self._year = year
  	  #variable oculta
  	  self.__brand = brand
  	  self.__color = color


car_1 = Car("MiniCooper", "Blue", "2017")

print(car_1._year)
print(car_1._Car__brand)

```

Es importante hacer notar que en Python no existen técnicamente atributos privados u ocultos. Los atributos de un objeto sólo pueden ocultarse (superficialmente) para que no sean accedidos desde fuera de la definición de una clase.

Por buenas prácticas es recomendable el uso de propiedades `@property` para crear interfaces `getter` y `setter` y manipular los atributos que se consideren necesarios. Los `getters` y `setters` evitan el uso de los guiones bajos al momento de acceder a la variable.

#### @Property

En Python, `property()` es una función nativa `built-in function` que crea y retorna un objeto de property (property object).

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

Donde `fget` es una función para obtener el valor del atributo, `fset` es una función para colocar un valor al atributo y `fdel` es una función para borrar el atributo. `doc`es un string, como un comentario.


```python
class Car:

  def __init__(self, brand, color):
  	  self.__brand = brand
  	  self.__color = color

  #métodos getter
  def get_brand(self):
      return self.__brand

  def get_color(self):
      return self.__color

  #métodos setter
  def set_brand(self, value):
      self.__brand = value

  def set_color(self, value):
      self.__color = value

  brand = property(get_brand, set_brand)
  color = property(get_color, set_color)

car_1 = Car("MiniCooper", "Blue")

#método getter `brand` para obtener marca
print(car_1.brand)
#>>"MiniCooper"

#método getter `color` para obtener color
print(car_1.color)
#>>"Blue"

#método setter `color` para asignar nuevo valor al color 
car_1.color = "Red"

print(car_1.color)
#>>"Red"
```

Otro ejemplo:

```python
class C:
	def __init__(self, x):
		self.__x = x

	def getx(self):
		return self.__x

	def setx(self, value):
		self.__x = value

	def delx(self):
		del self.__x

	x = property(getx, setx, delx)

c = C(2)
print(c.x)
#>> 2
c.x = 4
print(c.x)
#>> 4
del c.x	
```

Para evitar el uso de `get_...` y `set_...` en el nombre de los métodos, usamos el decorador `@property`. Por convención es recomendable usar los mismos nombres de las variables que nos interesan poder leer o modificar desde afuera de la clase.

El uso del decorador `@property` nos permite que un atributo sea un objeto de property que proveerá una interface a esta variable privada.

```python

class Car:

  def __init__(self, brand, color):
      self.__brand = brand
      self.__color = color

  #uso de property
  @property
  def brand(self):
      return self.__brand

  #uso de property
  @property
  def color(self):
      return self.__color

  @brand.setter
  def brand(self, value):
      self.__brand = value
  
  @color.setter
  def color(self, value):
      self.__color = value

  @brand.deleter
  def brand(self):
      raise AttributeError("do not delete")

  @color.deleter
  def color(self):
      raise AttributeError("do not delete")


car_1 = Car("MiniCooper", "Blue")

#método getter `brand` para obtener marca
print(car_1.brand)
#>>"MiniCooper"

#método getter `color` para obtener color
print(car_1.color)
#>>"Blue"

#método setter `color` para asignar nuevo valor al color 
car_1.color = "Red"

print(car_1.color)
#>>"Red"

#método deleter `color` para borrar el valor al color
del car_1.color
#>> AttributeError: do not delete

```

#### Otras ventajas del uso de '@property'


- No duplicar el propósito de los dos métodos speciales: `__setattr__` y `__getattr__`.


`__getattr__(self, name)`. Es posible definir comportamiento cuando un usuario
intenta acceder a un atributo que no existe. Este método puede ser útil para
capturar o redirigir una llamada del atributo, dando mensajes, advertencias,
retornar el atributo o simplemente manejando un `AttributeError`. Este método
especial solamente es llamado cuando se trata de acceder al atributo que no existe.

Ejemplo del uso de '__getattr__':


```python
class C:
	def __init__(self, x):
		self.__x = x

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		self.__x = value

	@x.deleter
	def x(self):
		raise AttributeError("do not delete")

	def __getattr__(self, name):
		if name == "y":
			return "3 sigue después de " + str(self.__x)
		else:
			raise AttributeError("Attribute " + name + " Does not exist")

c = C(2)
print(c.x)
print(c.y)
print(c.z)
```

`__setattr__(self, name, value)`. Permite definir comportamiento al momento de
asignarle valores a los atributos ya sea que exista o no, lo que significa
que puedes definir reglas para cualquier cambio en los valores de los
atributos.

Forma incorrecta de usar `__setattr__`:

```python
def __setattr__(self, name, value):
	self.name = value
```

Cada vez que un atributo es asignado, `__setattr__` es llamado, lo que genera una recursión (el método se mantiene llamándose a sí mismo), causando una falla.

```python
self.__setattr__('name', value)
```

Forma correcta de usarlo:

```python
def __setattr__(self, name, value):
	# asignando al diccionario de nombres en la clase
    self.__dict__[name] = value
    # definir el comportamiento deseado aquí
    ...
```

Un ejemplo de su uso:

```python
class Test:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        self.__dict__[name] = value

        #comportamiento deseado
        if name in ('a', 'b'):
        	print(name, " already is in dict of the class")
        else:
        	print(name, " has been assigned to dict of the class")

t = Test()
t.a = "F"
t.c = 'z'
print(t.__dict__)
```

- Otra ventaja es no duplicar las funciones nativas `setattr` y `getattr`:

```python
setattr(object, 'property_name', value)
getattr(object, 'property_name', default_value)
```
```python
class C:
	def __init__(self, x):
		self.__x = x

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		self.__x = value

	@x.deleter
	def x(self):
		raise AttributeError("do not delete")

c = C(2)
print(getattr(c, 'x'))
setattr(c, 'x', 4)
print(getattr(c, 'x'))
```

Es recomendable usar la notación de atributo punteado para acceder a lo atributos. Es importante conocer otras maneras para gestionar los atributos y saber que sucede con `getattr`, `setattr`, `__setattr__ y `__getattr__`, ya que es esencial para dominar el poder de Python.


## Ejercicio - Clase Door 1

Crea la clase `Door` con los métodos de instancia `open` y `close`. Esta clase tendrá los atributos `color`, `size`, asimismo se deberá poder cambiar el estado `status` de la puerta `Cerrado` y `Abierto`. 


Restricción:

- Si el status de la puerta es cerrado entonces no es posible abrir la puerta.
- Si el status de la puerta es abierto entonces es posible cerrar la puerta.
- El tamaño de la puerta no es posible cambiarlo.
- El color solamente es posible modificarlo.

Desarrolla el código basado en las pruebas `specs` correspondientes.

```python
"""Door class"""

...

```

```python
"""Ejemplo de objeto y salida"""

door_1 = Door.new("green", 5)

p door_1.size
#=> 5
p door_1.status
#=> "Cerrado"
p door_1.open
#=> "Business is closed"
p door_1.close
#=> "Door is closed"

```

```ruby
#Test Driven Development - TDD
$ test_door.py
```

