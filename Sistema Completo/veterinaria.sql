-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-11-2022 a las 10:14:24
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `veterinaria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cita`
--

CREATE TABLE `cita` (
  `idCita` int(11) NOT NULL COMMENT 'Permite almacenar el número identificador de la cita',
  `idPersonal` int(11) DEFAULT NULL COMMENT 'Almacena el identificador del perfil',
  `idMascota` int(11) DEFAULT NULL COMMENT 'Permite almacenar el número identificador del cliente.',
  `fecha` date DEFAULT NULL COMMENT 'Permite almacenar la fecha en la que se agendará la cita.',
  `hora` time DEFAULT NULL COMMENT 'Permite almacenar la hora en la que se agendará la cita.',
  `asuntoCita` varchar(20) DEFAULT NULL COMMENT 'Especifica si es médica, estética, etc.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Permite almacenar la información de las citas.';

--
-- Volcado de datos para la tabla `cita`
--

INSERT INTO `cita` (`idCita`, `idPersonal`, `idMascota`, `fecha`, `hora`, `asuntoCita`) VALUES
(1, 1, 1, '2000-01-01', '15:30:00', 'Vacunas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_ventas`
--

CREATE TABLE `detalle_ventas` (
  `idVenta` varchar(5) DEFAULT NULL COMMENT 'Permite almacenar el número identificador de la venta.',
  `productos` varchar(50) DEFAULT NULL COMMENT 'Permite guardar el identificador del producto.',
  `cantidad` int(11) DEFAULT NULL COMMENT 'Permite almacenar la cantidad total.',
  `precio` float DEFAULT NULL COMMENT 'Permite almacenar el precio de cada producto.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Permite registrar las ventas.';

--
-- Volcado de datos para la tabla `detalle_ventas`
--

INSERT INTO `detalle_ventas` (`idVenta`, `productos`, `cantidad`, `precio`) VALUES
('40', '[1, 2]', 4, 270),
('41', '[1, 2]', 8, 505),
('42', '[1, 2]', 6, 370),
('43', '[1, 2]', 6, 370),
('44', '[1, 2, 3]', 10, 720);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascota`
--

CREATE TABLE `mascota` (
  `idMascota` int(11) NOT NULL COMMENT 'Permite almacenar el número identificador de la Mascota.',
  `nombreMascota` varchar(50) DEFAULT NULL COMMENT 'Permite almacenar el nombre completo de la mascota',
  `nombre_Dueno` varchar(50) DEFAULT NULL COMMENT 'Almacena el nombre del dueño',
  `telefono_Dueno` int(11) DEFAULT NULL COMMENT 'Permite almacenar el número de teléfono del dueño.',
  `correo` varchar(50) DEFAULT NULL COMMENT 'Permite almacenar el número de teléfono del cliente.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Permite almacenar la información de las mascotas.';

--
-- Volcado de datos para la tabla `mascota`
--

INSERT INTO `mascota` (`idMascota`, `nombreMascota`, `nombre_Dueno`, `telefono_Dueno`, `correo`) VALUES
(1, 'Poffy', 'Enrique Ramirez', 2147483647, 'ram@gmail.com'),
(2, 'Kira', 'Hector Juarez', 2147483647, 'hecrj@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal`
--

CREATE TABLE `personal` (
  `idPersonal` int(11) NOT NULL COMMENT 'Almacena el identificador del personal.',
  `cargo` varchar(25) DEFAULT NULL COMMENT 'Especifica el cargo del usuario.',
  `nombre` varchar(25) DEFAULT NULL COMMENT 'Almacena el nombre del personal.',
  `correo` varchar(30) DEFAULT NULL COMMENT 'Almacena el correo del personal.',
  `telefono` int(11) DEFAULT NULL COMMENT 'Almacena el numero de contacto del personal.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Almacena el personal de la empresa.';

--
-- Volcado de datos para la tabla `personal`
--

INSERT INTO `personal` (`idPersonal`, `cargo`, `nombre`, `correo`, `telefono`) VALUES
(1, 'Veterinario', 'Samuel Martinez', 'sam@gmail.com', 2147483647),
(2, 'Recepcionista', 'Martha Soto', 'mar@gmail.com', 2147483647),
(3, 'Estilista', 'Jacinto', 'jac@gmail.com', 2147483647);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `idProducto` int(11) NOT NULL COMMENT 'Permite guardar el identificador del producto.',
  `nombreProducto` varchar(50) DEFAULT NULL COMMENT 'Permite almacenar el nombre del producto.',
  `precio` float DEFAULT NULL COMMENT 'Permite almacenar el precio de cada producto.',
  `cantidadProducto` int(11) DEFAULT NULL COMMENT 'Permite especificar la cantidad de stock en el sistema.',
  `descripcion` varchar(200) DEFAULT NULL COMMENT 'Descripción del producto, detalles extra'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Permite almacenar los productos del inventario.';

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`idProducto`, `nombreProducto`, `precio`, `cantidadProducto`, `descripcion`) VALUES
(1, 'Croquetas', 85, 40, 'Sobres de comida'),
(2, 'Correa', 50, 36, 'Correa de perro'),
(3, 'Shampoo', 100, 47, 'Shampoo antipulgas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `idVenta` int(11) NOT NULL COMMENT 'Permite almacenar el número identificador de la venta.',
  `fecha` date NOT NULL,
  `hora` varchar(20) DEFAULT NULL COMMENT 'Permite especificar la hora ne la que se realizó la venta.',
  `importeTotal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Permite almacenar la información de las ventas.';

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`idVenta`, `fecha`, `hora`, `importeTotal`) VALUES
(1, '2022-11-19', '1:37', 255),
(2, '2022-11-19', '1:45', 555),
(3, '2022-11-19', '1:46', 270),
(4, '2022-11-19', '1:47', 455),
(5, '2022-11-19', '1:48', 270),
(6, '2022-11-19', '1:51', 170),
(7, '2022-11-19', '1:53', 455),
(8, '2022-11-19', '1:59', 370),
(9, '2022-11-19', '2:6', 270),
(10, '2022-11-19', '2:8', 305),
(11, '2022-11-19', '2:10', 470),
(12, '2022-11-19', '2:10', 320),
(13, '2022-11-19', '2:14', 505),
(14, '2022-11-19', '2:57', 735),
(15, '2022-11-19', '2:59', 620),
(16, '2022-11-19', '2:59', 955),
(17, '2022-11-19', '3:7', 470),
(18, '2022-11-19', '3:11', 770),
(19, '2022-11-19', '3:14', 470),
(20, '2022-11-19', '3:18', 170),
(21, '2022-11-19', '3:19', 505),
(22, '2022-11-19', '3:20', 270),
(23, '2022-11-19', '3:23', 270),
(24, '2022-11-19', '3:24', 320),
(25, '2022-11-19', '23:46', 320),
(26, '2022-11-19', '23:48', 455),
(27, '2022-11-19', '23:50', 510),
(28, '2022-11-19', '23:52', 170),
(29, '2022-11-20', '0:6', 370),
(30, '2022-11-20', '0:8', 370),
(31, '2022-11-20', '0:10', 370),
(32, '2022-11-20', '0:10', 505),
(33, '2022-11-20', '0:15:28', 270),
(34, '2022-11-20', '0:17:37', 270),
(35, '2022-11-20', '0:29:51', 370),
(36, '2022-11-20', '0:32:22', 220),
(37, '2022-11-20', '0:34:9', 370),
(38, '2022-11-20', '0:38:1', 270),
(39, '2022-11-20', '0:39:31', 270),
(40, '2022-11-20', '0:40:38', 270),
(41, '2022-11-20', '0:53:52', 505),
(42, '2022-11-20', '1:28:1', 370),
(43, '2022-11-20', '1:44:51', 370),
(44, '2022-11-20', '1:45:22', 720);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cita`
--
ALTER TABLE `cita`
  ADD PRIMARY KEY (`idCita`);

--
-- Indices de la tabla `mascota`
--
ALTER TABLE `mascota`
  ADD PRIMARY KEY (`idMascota`);

--
-- Indices de la tabla `personal`
--
ALTER TABLE `personal`
  ADD PRIMARY KEY (`idPersonal`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`idProducto`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`idVenta`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cita`
--
ALTER TABLE `cita`
  MODIFY `idCita` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Permite almacenar el número identificador de la cita', AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `mascota`
--
ALTER TABLE `mascota`
  MODIFY `idMascota` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Permite almacenar el número identificador de la Mascota.', AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `personal`
--
ALTER TABLE `personal`
  MODIFY `idPersonal` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Almacena el identificador del personal.', AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Permite guardar el identificador del producto.', AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `idVenta` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Permite almacenar el número identificador de la venta.', AUTO_INCREMENT=45;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
