-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 04, 2022 at 06:29 AM
-- Server version: 8.0.27
-- PHP Version: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectdrone`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int NOT NULL,
  `email` varchar(255) NOT NULL,
  `uname` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `email`, `uname`, `pass`) VALUES
(3, 'admin@gmail.com', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `topic` varchar(255) NOT NULL,
  `comment` varchar(10000) NOT NULL,
  `cont_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `topic`, `comment`, `cont_time`) VALUES
(17, 'siti nurul aiman', 'aiman@gmail.com', 'General-Enquiries', 'hello', '2022-06-29 07:44:20');

-- --------------------------------------------------------

--
-- Table structure for table `dat`
--

CREATE TABLE `dat` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `image` varchar(255) NOT NULL,
  `result` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `dat`
--

INSERT INTO `dat` (`id`, `user_id`, `image`, `result`, `timestamp`) VALUES
(9, 15, 'static/uploaded_img/Corn_Gray_Spot (80).JPG', 'blight', '2022-07-01 02:37:12'),
(10, 15, 'static/uploaded_img/Corn_Gray_Spot (100).JPG', 'gray leaf spot', '2022-07-01 02:37:16'),
(11, 15, 'static/uploaded_img/Corn_Gray_Spot (81).JPG', 'gray leaf spot', '2022-07-04 05:52:38'),
(12, 15, 'static/uploaded_img/Corn_Gray_Spot (81).JPG', 'gray leaf spot', '2022-07-04 05:53:14');

-- --------------------------------------------------------

--
-- Table structure for table `info`
--

CREATE TABLE `info` (
  `info_id` int NOT NULL,
  `num` int NOT NULL,
  `title` text NOT NULL,
  `image` text NOT NULL,
  `description` text NOT NULL,
  `info_topic` text NOT NULL,
  `timestamp_post` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `info`
--

INSERT INTO `info` (`info_id`, `num`, `title`, `image`, `description`, `info_topic`, `timestamp_post`) VALUES
(18, 1, 'Blight', 'static/image/Corn_Blight (217).JPG', 'Any of various plant diseases whose symptoms include sudden and severe yellowing, browning, spotting, withering, or dying of leaves, flowers, fruit, stems, or the entire plant. Most blights are caused by bacterial or fungal infestations, which usually attack the shoots and other young, rapidly growing tissues of a plant. Fungal and bacterial blights mostly occur under cool moist conditions, and most economically important plants are susceptible to one or more blights. Measures for controlling and preventing blights typically involve the destruction of the infected plant parts; use of disease-free seed or stock and resistant varieties; crop rotation; pruning and spacing of plants for better air circulation; controlling pests that carry the fungus from plant to plant; avoidance of overhead watering and working among wet plants; and, where needed, the application of fungicide or antibiotics. Proper sanitation is key to stop the spread of the infestation. For bacterial blights, fixed copper or streptomycin is an effective antibiotic if applied weekly during damp weather when leaves and shoots are expanding. ', 'Fields and Soils Analysis', '2022-06-30 07:17:14'),
(19, 2, 'Common Rust', 'static/image/Corn_Common_Rust (142).JPG', 'Common rust produces rust-coloured to dark brown, elongated pustules on both leaf surfaces. The pustules contain rust spores (urediniospores) that are cinnamon brown in colour. Pustules darken as they age. Leaves, as well as sheaths, can be infected. Under severe conditions leaf chlorosis and death may occur. Common Rust is most problematic during prolonged periods of cool, wet weather. Rust diseases are generally easy to identify by the appearance of brown pustules. 	The best management practice is to use resistant corn hybrids. Fungicides can also be beneficial, especially if applied early when few pustules have appeared on the leaves.', 'Fields and Soils Analysis', '2022-06-30 07:17:14'),
(20, 3, 'Gray Leaf Spot', 'static/image/Corn_Gray_Spot (80).JPG', '	Early symptoms of gray leaf spot can be seen on leaves as small, spherical lesions with a yellow halo around them. These first lesions may be tan or brown before fungal sporulation begins. The initial disease can be hard to identify as gray leaf spot at this stage because it looks like eyespot and common rust. However, as the lesions mature, they elongate into rectangular, narrow, brown to gray spots that usually develop on the lower leaves and spread upward on the plant during the season. The lesions elongate and expand parallel to the leaf veins and can be 1.5 to 2 inches long. With favourable weather the lesions can rapidly merge and kill the entire leaf. Mature gray leaf spot symptoms can also be confused with symptoms of anthracnose leaf blight.', 'Farming', '2022-07-01 09:47:11');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `email` varchar(30) NOT NULL,
  `uname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pwd` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `uname`, `pwd`, `user_time`) VALUES
(15, 'aiman@gmail.com', 'aiman', '123', '0000-00-00 00:00:00'),
(20, 'nurul@gmail.com', 'nurul', '123', '2022-06-29 07:42:51');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dat`
--
ALTER TABLE `dat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`info_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `dat`
--
ALTER TABLE `dat`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `info`
--
ALTER TABLE `info`
  MODIFY `info_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
