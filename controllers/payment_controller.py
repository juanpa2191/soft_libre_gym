import pyodbc
from config.db import get_connection
from models.payment import Payment

class PaymentController:
    @staticmethod
    def create_payment(member_id, amount, method, reference):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("CALL sp_create_payment(?, ?, ?, ?, ?)", (member_id, amount, method, reference, 0))
            while cursor.nextset():
                pass
            conn.commit()
            cursor.execute("SELECT @p_payment_id")
            row = cursor.fetchone()
            payment_id = row[0] if row else None
            return Payment(id=payment_id, member_id=member_id, amount=amount, method=method, reference=reference)
        except Exception as e:
            print(f"Error creating payment: {e}")
            return None
        finally:
            conn.close()