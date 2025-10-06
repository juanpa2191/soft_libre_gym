import pyodbc
from config.db import get_connection
from models.member import Member

class MemberController:
    @staticmethod
    def create_member(first_name, last_name, email, phone):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("CALL sp_create_member(?, ?, ?, ?, ?)", (first_name, last_name, email, phone, 0))
            while cursor.nextset():
                pass
            conn.commit()
            cursor.execute("SELECT @p_member_id")
            row = cursor.fetchone()
            member_id = row[0] if row else None
            return Member(id=member_id, first_name=first_name, last_name=last_name, email=email, phone=phone)
        except Exception as e:
            print(f"Error creating member: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_member_by_id(member_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("CALL sp_get_member_by_id(?)", (member_id,))
            result = cursor.fetchone()
            if result:
                return Member(id=result[0], first_name=result[1], last_name=result[2], email=result[3], phone=result[4], birth_date=result[5], created_at=result[6])
            return None
        except Exception as e:
            print(f"Error getting member: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def update_member(member_id, first_name, last_name, email, phone):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("CALL sp_update_member(?, ?, ?, ?, ?)", (member_id, first_name, last_name, email, phone))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error updating member: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def delete_member(member_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("CALL sp_delete_member(?)", (member_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting member: {e}")
            return False
        finally:
            conn.close()