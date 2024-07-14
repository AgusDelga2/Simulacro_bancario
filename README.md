# Simulación bancaria

El siguiente script es una simulación bancaria con programación orientada a objetos que incluye clases para manejar clientes, cuentas de ahorro y plazos fijos.

Fecha: 2021


### Clases y Métodos

#### 1. `Banco`
- **Constructor**: 
  - `__init__(self, clientes)`: Inicializa la clase `Banco` con una lista de clientes.

#### 2. `Agenda`
- **Constructor**:
  - `__init__(self)`: Solicita al usuario que ingrese información sobre el cliente (nombre, DNI, teléfono y email) y guarda estos datos en un diccionario `datos_clientes`.

#### 3. `Clientes`
- Hereda de `Agenda`.s
- **Constructor**:
  - `__init__(self)`: Inicializa los atributos `cantidad`, `CajaAhorro` y `PlazoFijo`. Actualiza el diccionario `datos_clientes` con la información del cliente.
- **Métodos**:
  - `depositar(self)`: Solicita un monto para depositar y lo agrega al saldo del cliente.
  - `extraer(self)`: Solicita un monto para extraer, asegurando que no exceda el saldo actual. Si el monto es válido, lo deduce del saldo del cliente.
  - `imprimirTotal(self)`: Imprime el saldo actual del cliente.


#### 4. `Cuentas`
- Clase base para `CajaAhorro` y `PlazoFijo`.
- **Constructor**:
  - `__init__(self, titular, cantidad)`: Inicializa el titular de la cuenta y el saldo.
- **Método**:
  - `imprimir(self)`: Imprime los detalles de la cuenta.

#### 5. `CajaAhorro`
- Hereda de `Cuentas`.
- **Constructor**:
  - `__init__(self, titular, cantidad)`: Inicializa usando el constructor de `Cuentas`.
- **Método**:
  - `imprimir(self)`: Imprime los detalles de la cuenta de ahorro.

#### 6. `PlazoFijo`
- Hereda de `Cuentas`.
- **Constructor**:
  - `__init__(self, titular, cantidad, plazo, interes)`: Inicializa usando el constructor de `Cuentas` y agrega atributos `plazo` e `interes`.
- **Métodos**:
  - `importeInteres(self)`: Calcula y devuelve el interés total del plazo fijo.
  - `imprimir(self)`: Imprime los detalles del plazo fijo.
