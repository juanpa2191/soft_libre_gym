# Sistema de Gestión de Gimnasio - MVC en Python

Este proyecto implementa un sistema básico de gestión para un gimnasio utilizando el patrón de diseño MVC (Modelo-Vista-Controlador) en Python. Utiliza MySQL como base de datos con procedimientos almacenados para las operaciones CRUD.

## Estructura del Proyecto

```
gym/
├── config/
│   ├── __init__.py
│   └── db.py              # Configuración de conexión a la base de datos
├── models/
│   ├── __init__.py
│   ├── member.py          # Modelo para miembros
│   ├── trainer.py         # Modelo para entrenadores
│   ├── role.py            # Modelo para roles
│   ├── user.py            # Modelo para usuarios
│   ├── membership.py      # Modelo para membresías
│   ├── member_subscription.py  # Modelo para suscripciones
│   ├── gym_class.py       # Modelo para clases
│   ├── class_schedule.py  # Modelo para horarios de clases
│   ├── attendance.py      # Modelo para asistencia
│   ├── payment.py         # Modelo para pagos
│   ├── supplier.py        # Modelo para proveedores
│   ├── product.py         # Modelo para productos
│   ├── inventory.py       # Modelo para inventario
│   ├── sale.py            # Modelo para ventas
│   ├── sale_item.py       # Modelo para items de venta
│   ├── maintenance.py     # Modelo para mantenimiento
│   └── audit_log.py       # Modelo para log de auditoría
├── controllers/
│   ├── __init__.py
│   ├── member_controller.py    # Controlador para operaciones de miembros
│   └── payment_controller.py   # Controlador para operaciones de pagos
├── views/                 # (Reservado para futuras vistas)
├── main.py                # Script principal con menú interactivo
├── test_connection.py     # Script para probar conexión
└── README.md              # Este archivo
```

## Requisitos

- Python 3.7+
- MySQL Server
- MySQL ODBC Driver 9.4 Unicode
- Librerías Python:
  - pyodbc

## Instalación

1. **Instalar dependencias:**
   ```bash
   pip install pyodbc
   ```

2. **Configurar la base de datos:**
   - Ejecutar el script `schema.sql` en MySQL para crear la base de datos `gym_db` y los procedimientos almacenados.
   - Asegurarse de que el usuario `root` tenga acceso con la contraseña especificada.

3. **Configurar conexión:**
   - Verificar la configuración en `config/db.py`. La cadena de conexión ODBC debe apuntar a tu servidor MySQL.

## Uso

Ejecutar el script principal:

```bash
python main.py
```

Esto mostrará un menú interactivo con las siguientes opciones:

1. Crear miembro
2. Obtener miembro por ID
3. Actualizar miembro
4. Eliminar miembro
5. Crear pago
0. Salir

## Funcionalidades Implementadas

### Miembros
- Crear nuevo miembro
- Obtener miembro por ID
- Actualizar información de miembro
- Eliminar miembro

### Pagos
- Registrar nuevo pago

## Base de Datos

El sistema utiliza procedimientos almacenados en MySQL para todas las operaciones:

- `sp_create_member`
- `sp_get_member_by_id`
- `sp_update_member`
- `sp_delete_member`
- `sp_create_payment`

## Notas Técnicas

- Utiliza pyodbc para la conexión ODBC a MySQL.
- Los modelos son clases simples que representan las entidades de la base de datos.
- Los controladores manejan la lógica de negocio y las llamadas a procedimientos almacenados.
- El script principal proporciona una interfaz de línea de comandos básica.

## Próximas Mejoras

- Implementar controladores para todas las entidades restantes.
- Agregar validación de datos.
- Crear vistas web con Flask o similar.
- Implementar autenticación y autorización.
- Agregar logging y manejo de errores más robusto.

## Contribución

Este proyecto es educativo. Para mejoras, modificar los archivos correspondientes siguiendo la estructura MVC.