-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 28-05-2024 a las 05:34:46
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bibilioteca_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

DROP TABLE IF EXISTS `categorias`;
CREATE TABLE IF NOT EXISTS `categorias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id`, `categoria`) VALUES
(1, 'Generalidades'),
(2, 'Filosofía'),
(3, 'Religión'),
(4, 'Ciencias sociales'),
(5, 'Filología'),
(6, 'Ciencias naturales'),
(7, 'Ciencias prácticas'),
(8, 'Arte'),
(9, 'Literatura'),
(10, 'Historia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

DROP TABLE IF EXISTS `libros`;
CREATE TABLE IF NOT EXISTS `libros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` text COLLATE utf8mb4_spanish2_ci NOT NULL,
  `isbn` text COLLATE utf8mb4_spanish2_ci NOT NULL,
  `autor` varchar(100) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `editorial` varchar(60) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `fecha_publicacion` date NOT NULL,
  `id_categoria` int NOT NULL,
  `edicion` int NOT NULL,
  `numero_paginas` int NOT NULL,
  `numero_copias` int NOT NULL,
  `copias_disponibles` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`id`, `titulo`, `isbn`, `autor`, `editorial`, `fecha_publicacion`, `id_categoria`, `edicion`, `numero_paginas`, `numero_copias`, `copias_disponibles`) VALUES
(1, 'El Señor de los Anillos: La Comunidad del Anillo', '978-84-206-5060-2', 'J.R.R. Tolkien', 'Minotauro', '1954-07-29', 1, 1, 1200, 15, 15),
(2, 'El Hobbit', '978-84-206-6732-8', 'J.R.R. Tolkien', 'Minotauro', '1937-09-21', 1, 1, 310, 10, 10),
(3, 'Cien años de soledad', '978-84-376-2785-2', 'Gabriel García Márquez', 'Alfaguara', '1967-05-30', 2, 1, 472, 20, 20),
(4, 'El Principito', '978-84-206-4697-5', 'Antoine de Saint-Exupéry', 'Salamandra', '1943-04-06', 3, 1, 240, 12, 12),
(5, '1984', '978-84-493-2272-3', 'George Orwell', 'Destino', '1949-06-08', 3, 1, 328, 15, 15),
(6, 'El Alquimista', '978-84-663-3797-9', 'Paulo Coelho', 'Planeta', '1988-03-14', 3, 1, 288, 18, 18),
(7, 'El Silencio de los Corderos', '978-84-303-0563-9', 'Thomas Harris', 'Plaza & Janés', '1988-02-01', 4, 1, 624, 14, 14),
(8, 'Orgullo y Prejuicio', '978-84-206-6148-2', 'Jane Austen', 'Alba Editorial', '1813-01-28', 2, 1, 560, 16, 16),
(9, 'Don Quijote de la Mancha', '978-84-670-0408-2', 'Miguel de Cervantes', 'Penguin Random House', '1605-01-16', 2, 1, 1080, 25, 25),
(10, 'El Cuadro de las Meninas', '978-84-235-3827-6', 'José Luis Corral', 'Taurus', '2005-10-01', 5, 1, 320, 11, 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

DROP TABLE IF EXISTS `prestamos`;
CREATE TABLE IF NOT EXISTS `prestamos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_libro` int NOT NULL,
  `fecha_prestamo` date NOT NULL,
  `fecha_devolucion` date NOT NULL,
  `id_sancion` int NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `prestamos`
--

INSERT INTO `prestamos` (`id`, `id_usuario`, `id_libro`, `fecha_prestamo`, `fecha_devolucion`, `id_sancion`, `activo`) VALUES
(1, 1, 1, '2024-05-27', '2024-06-10', 0, 0),
(2, 2, 2, '2024-05-28', '2024-06-12', 1, 0),
(3, 3, 3, '2024-05-29', '0000-00-00', 0, 1),
(4, 4, 2, '2024-05-30', '2024-06-08', 2, 0),
(5, 5, 5, '2024-05-31', '0000-00-00', 0, 1),
(6, 6, 6, '2024-06-01', '2024-06-15', 3, 0),
(7, 2, 6, '2024-06-02', '0000-00-00', 0, 1),
(8, 3, 8, '2024-06-03', '2024-06-06', 4, 0),
(9, 1, 9, '2024-06-04', '0000-00-00', 0, 1),
(10, 5, 4, '2024-06-05', '2024-06-07', 5, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

DROP TABLE IF EXISTS `reservas`;
CREATE TABLE IF NOT EXISTS `reservas` (
  `id_reserva` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_libro` int NOT NULL,
  `posicion_cola` int NOT NULL,
  PRIMARY KEY (`id_reserva`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `reservas`
--

INSERT INTO `reservas` (`id_reserva`, `id_usuario`, `id_libro`, `posicion_cola`) VALUES
(1, 2, 4, 2),
(2, 1, 6, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

DROP TABLE IF EXISTS `roles`;
CREATE TABLE IF NOT EXISTS `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rol` varchar(40) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `rol`) VALUES
(1, 'Administrador'),
(2, 'Bibliotecario'),
(3, 'Lector');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sanciones`
--

DROP TABLE IF EXISTS `sanciones`;
CREATE TABLE IF NOT EXISTS `sanciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `descripcion` text COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `sanciones`
--

INSERT INTO `sanciones` (`id`, `fecha_inicio`, `fecha_fin`, `descripcion`) VALUES
(1, '2024-05-20', '2024-05-25', 'Entrega tardía de libro'),
(2, '2024-05-22', '2024-05-27', 'Entrega tardía de libro'),
(3, '2024-05-24', '2024-05-31', 'Libro entregado con daños'),
(4, '2024-05-26', '2024-06-01', 'Entrega tardía de libro'),
(5, '2024-05-28', '2024-05-30', 'Libro entregado con manchas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `apellidos` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `id_rol` int NOT NULL,
  `correo` varchar(255) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `contrasena` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombres`, `apellidos`, `id_rol`, `correo`, `contrasena`) VALUES
(1, 'Juan José', 'Pérez González', 1, 'juan@ejemplo.com', 'contrasena123'),
(2, 'María', 'García López', 2, 'maria@ejemplo.com', 'contrasena456'),
(3, 'Pedro', 'López Martínez', 3, 'pedro@ejemplo.com', 'contrasena789'),
(4, 'Ana', 'Román Gutiérrez', 3, 'ana.roman@ejemplo.com', 'contrasena012'),
(5, 'Roberto Ismael', 'Gutiérrez Flores', 2, 'roberto.gutierrez@ejemplo.com', 'contrasena345'),
(6, 'Isabel', 'Flores Sánchez', 3, 'isabel.flores@ejemplo.com', 'contrasena678'),
(7, 'Carlos', 'Martínez Ramírez', 3, 'carlos.martinez@ejemplo.com', 'contrasena901'),
(8, 'Laura', 'Sánchez Pérez', 3, 'laura.sanchez@ejemplo.com', 'contrasena234'),
(9, 'David', 'Ramírez González', 3, 'david.ramirez@ejemplo.com', 'contrasena567');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
