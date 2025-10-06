from controllers.member_controller import MemberController
from controllers.payment_controller import PaymentController

def main():
    while True:
        print("\n--- Menú del Sistema de Gimnasio ---")
        print("1. Crear miembro")
        print("2. Obtener miembro por ID")
        print("3. Actualizar miembro")
        print("4. Eliminar miembro")
        print("5. Crear pago")
        print("0. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            first_name = input("Nombre: ")
            last_name = input("Apellido: ")
            email = input("Email: ")
            phone = input("Teléfono: ")
            member = MemberController.create_member(first_name, last_name, email, phone)
            if member:
                print(f"Miembro creado: {member}")
            else:
                print("Error al crear miembro")

        elif choice == '2':
            try:
                member_id = int(input("ID del miembro: "))
                member = MemberController.get_member_by_id(member_id)
                if member:
                    print(f"Miembro: {member}")
                else:
                    print("Miembro no encontrado")
            except ValueError:
                print("ID inválido")

        elif choice == '3':
            try:
                member_id = int(input("ID del miembro: "))
                first_name = input("Nuevo nombre: ")
                last_name = input("Nuevo apellido: ")
                email = input("Nuevo email: ")
                phone = input("Nuevo teléfono: ")
                success = MemberController.update_member(member_id, first_name, last_name, email, phone)
                if success:
                    print("Miembro actualizado")
                else:
                    print("Error al actualizar miembro")
            except ValueError:
                print("ID inválido")

        elif choice == '4':
            try:
                member_id = int(input("ID del miembro: "))
                success = MemberController.delete_member(member_id)
                if success:
                    print("Miembro eliminado")
                else:
                    print("Error al eliminar miembro")
            except ValueError:
                print("ID inválido")

        elif choice == '5':
            try:
                member_id = int(input("ID del miembro: "))
                amount = float(input("Monto: "))
                method = input("Método (cash/card/transfer): ")
                reference = input("Referencia: ")
                payment = PaymentController.create_payment(member_id, amount, method, reference)
                if payment:
                    print(f"Pago creado: {payment}")
                else:
                    print("Error al crear pago")
            except ValueError:
                print("Datos inválidos")

        elif choice == '0':
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()