-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 21, 2024 at 06:09 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shopping`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `password` text NOT NULL,
  `email` text NOT NULL,
  `security_question` text NOT NULL,
  `security_answer` text NOT NULL,
  `device_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`id`, `name`, `password`, `email`, `security_question`, `security_answer`, `device_name`) VALUES
(1, 'USER', '123', 'user@gmail.com', 'Name', 'USER', 'LAPTOP-JH106GME');

-- --------------------------------------------------------

--
-- Table structure for table `cars_data`
--

CREATE TABLE `cars_data` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `car_price` text NOT NULL,
  `model_date` text NOT NULL,
  `car_type` text NOT NULL,
  `car_capicity` text NOT NULL,
  `car_brand` text NOT NULL,
  `car_features` text NOT NULL,
  `car_image1` text NOT NULL,
  `car_image2` text NOT NULL,
  `car_image3` text NOT NULL,
  `car_image4` text NOT NULL,
  `car_image5` text NOT NULL,
  `car_image6` text NOT NULL,
  `device_name` text NOT NULL,
  `time` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cars_data`
--

INSERT INTO `cars_data` (`id`, `name`, `car_price`, `model_date`, `car_type`, `car_capicity`, `car_brand`, `car_features`, `car_image1`, `car_image2`, `car_image3`, `car_image4`, `car_image5`, `car_image6`, `device_name`, `time`) VALUES
(45, 'Dummy Car', '₹100,000', '01/March/2019', 'Petrol', '4', 'Marauti & Suzuki', 'Air conditional + Top Roof Open', 'car_images/background1.png', 'car_images/background2.png', 'car_images/background3.png', 'car_images/background4.png', 'car_images/car.png', 'car_images/background.png', 'LAPTOP-JH106GME', '15-02-24 18:48:38'),
(49, 'Hyundai Creata', '₹800,000', '10/October/2022', 'Petrol', '4', 'Hyundai', 'Air conditional + Top Roof Open', 'car_images/background1.png', 'car_images/background2.png', 'car_images/background3.png', 'car_images/background4.png', 'car_images/car.png', 'car_images/background.png', 'LAPTOP-JH106GME', '16-02-24 19:45:22');

-- --------------------------------------------------------

--
-- Table structure for table `car_brand_values`
--

CREATE TABLE `car_brand_values` (
  `id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_brand_values`
--

INSERT INTO `car_brand_values` (`id`, `value`) VALUES
(2, 'Kia'),
(3, 'Ford'),
(4, 'Hyundai'),
(5, 'BMW'),
(8, 'On Demand'),
(10, 'Mahindra'),
(11, 'Marauti & Suzuki'),
(12, 'Renault'),
(13, 'Toayta');

-- --------------------------------------------------------

--
-- Table structure for table `car_feature_values`
--

CREATE TABLE `car_feature_values` (
  `id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_feature_values`
--

INSERT INTO `car_feature_values` (`id`, `value`) VALUES
(3, 'No Additional Features'),
(5, 'Air conditional + Top Roof Open');

-- --------------------------------------------------------

--
-- Table structure for table `car_type_values`
--

CREATE TABLE `car_type_values` (
  `id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_type_values`
--

INSERT INTO `car_type_values` (`id`, `value`) VALUES
(1, 'Petrol'),
(2, 'Diseal'),
(3, 'CNG'),
(10, 'Electric');

-- --------------------------------------------------------

--
-- Table structure for table `customer_account`
--

CREATE TABLE `customer_account` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `password` text NOT NULL,
  `email` text NOT NULL,
  `mobile` text NOT NULL,
  `state` text NOT NULL,
  `city` text NOT NULL,
  `customer_id` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_account`
--

INSERT INTO `customer_account` (`id`, `name`, `password`, `email`, `mobile`, `state`, `city`, `customer_id`) VALUES
(1, 'Customer1', '123', 'customer1@gmail.com', '7689340251', 'Punjab', 'Ludhiyana', '715021428'),
(2, 'Customer2', '456', 'customer2@gmail.com', '7689340496', 'Andra Pradesh', 'Amaravati', '829102641');

-- --------------------------------------------------------

--
-- Table structure for table `customer_login`
--

CREATE TABLE `customer_login` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `mobile` text NOT NULL,
  `password` text NOT NULL,
  `email` text NOT NULL,
  `customer_id` text NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_login`
--

INSERT INTO `customer_login` (`id`, `name`, `mobile`, `password`, `email`, `customer_id`, `time`) VALUES
(1, 'Customer1', '7689340251', '123', 'customer1@gmail.com', '715021428', '2024-02-13 17:16:19'),
(2, 'Customer2', '7689340496', '456', 'customer2@gmail.com', '829102641', '2024-02-14 21:34:45');

-- --------------------------------------------------------

--
-- Table structure for table `email_data`
--

CREATE TABLE `email_data` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `datetime` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `email_data`
--

INSERT INTO `email_data` (`id`, `name`, `email`, `title`, `content`, `datetime`) VALUES
(10, 'Customer1', 'kotharijitendra960@gmail.com', 'Hello Mail', 'Hello how are you\n', '21/02/24 00/06/35');

-- --------------------------------------------------------

--
-- Table structure for table `email_sender`
--

CREATE TABLE `email_sender` (
  `id` int(11) NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL,
  `device_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `email_sender`
--

INSERT INTO `email_sender` (`id`, `email`, `password`, `device_name`) VALUES
(1, 'sushmakotnalatanmaykothari@gmail.com', 'lgyqsmaukiphyaqe', 'LAPTOP-JH106GME');

-- --------------------------------------------------------

--
-- Table structure for table `logindata`
--

CREATE TABLE `logindata` (
  `id` int(11) NOT NULL,
  `email` text NOT NULL,
  `device_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `logindata`
--

INSERT INTO `logindata` (`id`, `email`, `device_name`) VALUES
(3, 'user@gmail.com', 'LAPTOP-JH106GME');

-- --------------------------------------------------------

--
-- Table structure for table `registred_customers`
--

CREATE TABLE `registred_customers` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `mobile` text NOT NULL,
  `gender` text NOT NULL,
  `address` text NOT NULL,
  `dob` text NOT NULL,
  `dor` text NOT NULL,
  `nationality` text NOT NULL,
  `prooftype` text NOT NULL,
  `proofid` text NOT NULL,
  `customer_id` text NOT NULL,
  `customer_photo` text NOT NULL,
  `car_image` text NOT NULL,
  `car_id` int(11) NOT NULL,
  `car_name` text NOT NULL,
  `car_price` text NOT NULL,
  `car_brand` text NOT NULL,
  `model_date` text NOT NULL,
  `car_number` text NOT NULL,
  `time` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registred_customers`
--

INSERT INTO `registred_customers` (`id`, `name`, `email`, `mobile`, `gender`, `address`, `dob`, `dor`, `nationality`, `prooftype`, `proofid`, `customer_id`, `customer_photo`, `car_image`, `car_id`, `car_name`, `car_price`, `car_brand`, `model_date`, `car_number`, `time`) VALUES
(29, 'Customer1', 'customer1@gmail.com', '7689340251', 'Male', 'Ludhiyana,Punjab,India\n\n\n\n', '01/01/01', '15/02/24', 'Indian', 'Adhar card', '729812041752', '715021428', 'customer_images/admin2.png', 'car_images/maruti-suzuki-vittara-brezza-1.png', 44, 'Maruti Suzuki Vittara Brezza', '₹650,000', 'Marauti & Suzuki', '02/Febuary/2019', 'PN 5427 7911', '21/02/24'),
(30, 'Customer2', 'customer2@gmail.com', '7689340496', 'Female', 'Andra Pradesh, Amaravati, India\n\n', '02/02/02', '15/02/24', 'Indian', 'Adhar card', '932518201639', '829102641', 'customer_images/customer.png', 'car_images/huyandai-creata-1.png', 29, 'Hyundai Creata', '₹700,000', 'Hyundai', '3/March/2019', 'AP 4124 6762', '21/02/24'),
(32, 'Customer3', 'customer3@gmail.com', '8710264952', 'Female', 'Jabalpur,Madhya Pradesh, India\n\n', '20/02/05', '16/02/24', 'Indian', 'Adhar card', '703125579034', '953265489', 'customer_images/admin2.png', 'car_images/huyandai-creata-1.png', 46, 'On Demand1', '₹500,000', 'On Demand', '01/March/2019', 'MP 5290 7317', '21/02/24'),
(33, 'Customer4', 'customer4@gmail.com', '8971203544', 'Male', 'Alwar, Rajasthan, India\n\n', '30/04/01', '16/02/24', 'Indian', 'Adhar card', '93210352872', '840234017', 'customer_images/customer.png', 'car_images/huyandai-creata-1.png', 47, 'On Demand2', '₹650,000', 'On Demand', '3/March/2021', 'RJ 6432 8032', '21/02/24'),
(35, 'Customer5', 'customer5@gmail.com', '9216302658', 'Male', 'Pune, Maharastra, India\n\n\n\n', '16/10/04', '21/02/24', 'Indian', 'Adhar card', '891023456789', '983541206', 'customer_images/admin2.png', 'car_images/background1.png', 50, 'On Demand3', '₹700,000', 'On Demand', '5/October/2021', 'MH 2886 8734', '21/02/24');

-- --------------------------------------------------------

--
-- Table structure for table `reserve_cars_data`
--

CREATE TABLE `reserve_cars_data` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `car_price` text NOT NULL,
  `model_date` text NOT NULL,
  `car_type` text NOT NULL,
  `car_capicity` text NOT NULL,
  `car_brand` text NOT NULL,
  `car_features` text NOT NULL,
  `car_image1` text NOT NULL,
  `car_image2` text NOT NULL,
  `car_image3` text NOT NULL,
  `car_image4` text NOT NULL,
  `car_image5` text NOT NULL,
  `car_image6` text NOT NULL,
  `device_name` text NOT NULL,
  `time` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reserve_cars_data`
--

INSERT INTO `reserve_cars_data` (`id`, `name`, `car_price`, `model_date`, `car_type`, `car_capicity`, `car_brand`, `car_features`, `car_image1`, `car_image2`, `car_image3`, `car_image4`, `car_image5`, `car_image6`, `device_name`, `time`) VALUES
(26, 'Maruti Suzuki Vittara Brezza', '₹650,000', '02/Febuary/2019', 'Petrol', '4', 'Marauti & Suzuki', 'Air conditional + Top Roof Open', 'car_images/maruti-suzuki-vittara-brezza-1.png', 'car_images/maruti-suzuki-vittara-brezza-2.png', 'car_images/maruti-suzuki-vittara-brezza-3.png', 'car_images/maruti-suzuki-vittara-brezza-4.png', 'car_images/maruti-suzuki-vittara-brezza-5.png', 'car_images/maruti-suzuki-vittara-brezza-6.png', 'LAPTOP-JH106GME', '15-02-24 18:44:09'),
(27, 'Hyundai Creata', '₹700,000', '3/March/2019', 'Diseal', '6', 'Hyundai', 'Air conditional + Top Roof Open', 'car_images/huyandai-creata-1.png', 'car_images/huyandai-creata-2.png', 'car_images/huyandai-creata-3.png', 'car_images/huyandai-creata-4.png', 'car_images/huyandai-creata-5.png', 'car_images/huyandai-creata-6.png', 'LAPTOP-JH106GME', '15-02-24 18:46:35'),
(29, 'On Demand1', '₹500,000', '01/March/2019', 'Petrol', '4', 'On Demand', 'Air conditional + Top Roof Open', 'car_images/background1.png', 'car_images/background2.png', 'car_images/background3.png', 'car_images/background.png', 'car_images/car.png', 'car_images/background.png', 'LAPTOP-JH106GME', '16-02-24 20:46:19'),
(30, 'On Demand2', '₹650,000', '3/March/2021', 'Diseal', '6', 'On Demand', 'No Additional Features', 'car_images/background1.png', 'car_images/background2.png', 'car_images/background3.png', 'car_images/background4.png', 'car_images/car.png', 'car_images/background.png', 'LAPTOP-JH106GME', '16-02-24 20:49:24'),
(32, 'On Demand3', '₹700,000', '5/October/2021', 'CNG', '8', 'On Demand', 'Air conditional + Top Roof Open', 'car_images/background1.png', 'car_images/background2.png', 'car_images/background3.png', 'car_images/background4.png', 'car_images/car.png', 'car_images/background.png', 'LAPTOP-JH106GME', '21-02-24 22:08:16');

-- --------------------------------------------------------

--
-- Table structure for table `reserve_customers_data`
--

CREATE TABLE `reserve_customers_data` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `mobile` text NOT NULL,
  `gender` text NOT NULL,
  `address` text NOT NULL,
  `dob` text NOT NULL,
  `dor` text NOT NULL,
  `nationality` text NOT NULL,
  `prooftype` text NOT NULL,
  `proofid` text NOT NULL,
  `customer_id` text NOT NULL,
  `customer_photo` text NOT NULL,
  `car_image` text NOT NULL,
  `car_id` text NOT NULL,
  `car_name` text NOT NULL,
  `car_price` text NOT NULL,
  `car_brand` text NOT NULL,
  `model_date` text NOT NULL,
  `car_number` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reserve_customers_data`
--

INSERT INTO `reserve_customers_data` (`id`, `name`, `email`, `mobile`, `gender`, `address`, `dob`, `dor`, `nationality`, `prooftype`, `proofid`, `customer_id`, `customer_photo`, `car_image`, `car_id`, `car_name`, `car_price`, `car_brand`, `model_date`, `car_number`) VALUES
(22, 'Dummy Customer', 'dummy@gmail.com', '1234567890', 'Male', 'Dummy\n', '03/03/03', '15/02/24', 'Dummy', 'Adhar card', '123456789012', '123456789', 'customer_images/customer_feedback.png', 'car_images/background1.png', '43', 'Dummy Car', '₹100,000', 'Marauti & Suzuki', '01/March/2019', 'DM 5472 7923');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cars_data`
--
ALTER TABLE `cars_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_brand_values`
--
ALTER TABLE `car_brand_values`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_feature_values`
--
ALTER TABLE `car_feature_values`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_type_values`
--
ALTER TABLE `car_type_values`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer_account`
--
ALTER TABLE `customer_account`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer_login`
--
ALTER TABLE `customer_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `email_data`
--
ALTER TABLE `email_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `email_sender`
--
ALTER TABLE `email_sender`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `logindata`
--
ALTER TABLE `logindata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registred_customers`
--
ALTER TABLE `registred_customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reserve_cars_data`
--
ALTER TABLE `reserve_cars_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reserve_customers_data`
--
ALTER TABLE `reserve_customers_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cars_data`
--
ALTER TABLE `cars_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `car_brand_values`
--
ALTER TABLE `car_brand_values`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `car_feature_values`
--
ALTER TABLE `car_feature_values`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `car_type_values`
--
ALTER TABLE `car_type_values`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `customer_account`
--
ALTER TABLE `customer_account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `customer_login`
--
ALTER TABLE `customer_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `email_data`
--
ALTER TABLE `email_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `email_sender`
--
ALTER TABLE `email_sender`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `logindata`
--
ALTER TABLE `logindata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `registred_customers`
--
ALTER TABLE `registred_customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `reserve_cars_data`
--
ALTER TABLE `reserve_cars_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `reserve_customers_data`
--
ALTER TABLE `reserve_customers_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
