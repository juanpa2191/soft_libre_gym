-- schema.sql
CREATE DATABASE IF NOT EXISTS gym_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE gym_db;

-- Roles y usuarios del sistema
CREATE TABLE IF NOT EXISTS roles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL UNIQUE,
  description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(80) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role_id INT,
  full_name VARCHAR(150),
  email VARCHAR(150),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE SET NULL
);

-- Miembros y entrenadores
CREATE TABLE IF NOT EXISTS members (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(150) UNIQUE,
  phone VARCHAR(30),
  birth_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS trainers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(150) UNIQUE,
  phone VARCHAR(30),
  hire_date DATE,
  specialty VARCHAR(100)
);

-- Membresías y suscripciones
CREATE TABLE IF NOT EXISTS memberships (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  duration_months INT,
  price DECIMAL(10,2),
  description TEXT
);

CREATE TABLE IF NOT EXISTS member_subscriptions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  member_id INT NOT NULL,
  membership_id INT NOT NULL,
  start_date DATE,
  end_date DATE,
  status ENUM('active','expired','cancelled') DEFAULT 'active',
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE,
  FOREIGN KEY (membership_id) REFERENCES memberships(id) ON DELETE RESTRICT
);

-- Clases y horarios
CREATE TABLE IF NOT EXISTS classes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120),
  description TEXT,
  trainer_id INT,
  capacity INT DEFAULT 20,
  FOREIGN KEY (trainer_id) REFERENCES trainers(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS class_schedule (
  id INT AUTO_INCREMENT PRIMARY KEY,
  class_id INT NOT NULL,
  scheduled_at DATETIME NOT NULL,
  duration_minutes INT,
  location VARCHAR(100),
  FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS attendance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  schedule_id INT NOT NULL,
  member_id INT NOT NULL,
  attended_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  status ENUM('present','absent') DEFAULT 'present',
  FOREIGN KEY (schedule_id) REFERENCES class_schedule(id) ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);

-- Pagos
CREATE TABLE IF NOT EXISTS payments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  member_id INT NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  paid_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  method ENUM('cash','card','transfer') DEFAULT 'card',
  reference VARCHAR(120),
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);

-- Productos, proveedores e inventario
CREATE TABLE IF NOT EXISTS suppliers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200),
  contact VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200),
  sku VARCHAR(80) UNIQUE,
  price DECIMAL(10,2),
  supplier_id INT,
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS inventory (
  product_id INT PRIMARY KEY,
  quantity INT DEFAULT 0,
  min_quantity INT DEFAULT 0,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Ventas
CREATE TABLE IF NOT EXISTS sales (
  id INT AUTO_INCREMENT PRIMARY KEY,
  member_id INT NULL,
  total DECIMAL(10,2),
  sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
  created_by INT NULL,
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE SET NULL,
  FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS sale_items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  sale_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10,2),
  FOREIGN KEY (sale_id) REFERENCES sales(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);

-- Mantenimiento y auditoría
CREATE TABLE IF NOT EXISTS maintenance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  equipment VARCHAR(150),
  description TEXT,
  maintenance_date DATE,
  cost DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS audit_log (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  action VARCHAR(255),
  object_type VARCHAR(100),
  object_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

USE gym_db;
DELIMITER //

-- Crear miembro
CREATE PROCEDURE sp_create_member(
  IN p_first_name VARCHAR(100),
  IN p_last_name VARCHAR(100),
  IN p_email VARCHAR(150),
  IN p_phone VARCHAR(30),
  OUT p_member_id INT
)
BEGIN
  INSERT INTO members(first_name,last_name,email,phone) 
  VALUES(p_first_name,p_last_name,p_email,p_phone);
  SET p_member_id = LAST_INSERT_ID();
END;
//

-- Obtener miembro por id
CREATE PROCEDURE sp_get_member_by_id(
  IN p_id INT
)
BEGIN
  SELECT * FROM members WHERE id = p_id;
END;
//

-- Actualizar miembro
CREATE PROCEDURE sp_update_member(
  IN p_id INT,
  IN p_first_name VARCHAR(100),
  IN p_last_name VARCHAR(100),
  IN p_email VARCHAR(150),
  IN p_phone VARCHAR(30)
)
BEGIN
  UPDATE members
  SET first_name = p_first_name,
      last_name  = p_last_name,
      email      = p_email,
      phone      = p_phone
  WHERE id = p_id;
END;
//

-- Eliminar miembro
CREATE PROCEDURE sp_delete_member(IN p_id INT)
BEGIN
  DELETE FROM members WHERE id = p_id;
END;
//

-- Registrar pago
CREATE PROCEDURE sp_create_payment(
  IN p_member_id INT,
  IN p_amount DECIMAL(10,2),
  IN p_method ENUM('cash','card','transfer'),
  IN p_reference VARCHAR(120),
  OUT p_payment_id INT
)
BEGIN
  INSERT INTO payments(member_id, amount, method, reference) 
  VALUES(p_member_id, p_amount, p_method, p_reference);
  SET p_payment_id = LAST_INSERT_ID();
END;
//

DELIMITER ;