-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th2 28, 2023 lúc 01:51 PM
-- Phiên bản máy phục vụ: 10.4.21-MariaDB
-- Phiên bản PHP: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `ecobike`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hoa_don`
--

CREATE TABLE `hoa_don` (
  `maHoaDon` int(11) NOT NULL,
  `nguoiGiaoDich` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `maThe` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `maXe` int(11) NOT NULL,
  `noiDung` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `maNhaXe` int(11) NOT NULL,
  `thoiDiemGiaoDich` datetime NOT NULL,
  `soTienThanhToan` int(11) NOT NULL,
  `phuongThucThanhToan` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `hoa_don`
--

INSERT INTO `hoa_don` (`maHoaDon`, `nguoiGiaoDich`, `maThe`, `maXe`, `noiDung`, `maNhaXe`, `thoiDiemGiaoDich`, `soTienThanhToan`, `phuongThucThanhToan`) VALUES
(1, 'Trần Tiến Bằng', 'BANG20193988', 20230001, 'Thanh toán Thuê xe', 1, '2023-02-14 19:58:00', 400000, 'EcobikeBank'),
(2, 'Nguyễn Thành Phong', 'PHONG20192016', 20230004, 'Thanh toán Thuê xe', 2, '2023-02-14 19:59:00', 600000, 'EcobikeBank'),
(3, 'Lê Quốc Hưng', 'HUNG20191881', 20230002, 'Thanh toán Thuê xe', 1, '2023-02-14 20:39:00', 400000, 'EcobikeBank'),
(4, 'Bằng', 'Bang456789', 20230002, 'Thanh toán Trả xe', 2, '2023-02-14 20:40:00', 1520000, 'EcobikeBank'),
(5, 'Trần Tiến Bằng', 'BANG20193988', 20230001, 'Hoàn tiền Trả xe', 1, '2023-02-15 10:11:00', -225000, 'EcobikeBank'),
(6, 'Trần Tiến Bằng', '225153284562', 20230001, 'Thanh toán Thuê xe', 1, '2023-02-16 08:45:00', 400000, 'EcobikeBank'),
(7, 'Trần Tiến Bằng', '225153284562', 20230001, 'Thanh toán Trả xe', 1, '2023-02-22 09:41:00', 768000, 'EcobikeBank');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nha_xe`
--

CREATE TABLE `nha_xe` (
  `maNhaXe` int(11) NOT NULL,
  `tenNhaXe` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `sucChua` int(11) NOT NULL,
  `diaChi` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `soDienThoai` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `mail` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `nha_xe`
--

INSERT INTO `nha_xe` (`maNhaXe`, `tenNhaXe`, `sucChua`, `diaChi`, `soDienThoai`, `mail`) VALUES
(1, 'Bách Khoa', 100, 'Bách Khoa, Hai Bà Trưng, Hà Nội', '09873126166', 'bachkhoaecobike@gmail.com'),
(2, 'Cầu Giấy', 200, 'Yên Hòa, Cầu Giấy, Hà Nội', '0985512301', 'caugiayecobike@gmail.com'),
(3, 'Hoàn Kiếm', 500, 'Cửa Đông, Hoàn Kiếm, Hà Nội', '0957845264', 'hoankiemecobike@gmail.com'),
(4, 'Ngọc Hà', 400, 'Ngọc Hà, Ba Đình, Hà Nôi', '0916791325', 'ngochaecobike@gmail.com');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `xe`
--

CREATE TABLE `xe` (
  `maXe` int(11) NOT NULL,
  `bienSoXe` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `loaiXe` varchar(100) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'Xe đạp đơn',
  `giaTriXe` int(11) NOT NULL,
  `hangXe` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `xe`
--

INSERT INTO `xe` (`maXe`, `bienSoXe`, `loaiXe`, `giaTriXe`, `hangXe`) VALUES
(20230001, '29A-12345', 'Xe đạp đơn', 1000000, 'Merida'),
(20230002, '29A-18355', 'Xe đạp đơn', 1000000, 'Merida'),
(20230003, '38A-52185', 'Xe đạp đôi', 1200000, 'Specialized'),
(20230004, '46N-52185', 'Xe đạp điện đơn', 1500000, 'Scott'),
(20230005, '39A-11625', 'Xe đạp điện đôi', 2000000, 'Asama'),
(20230006, '04Y-97017', 'Xe đạp điện đơn', 1500000, 'Asama'),
(20230007, '61W-33269', 'Xe đạp điện đôi', 2000000, 'Honda'),
(20230008, '06V-49064', 'Xe đạp đôi', 1200000, 'Meride'),
(20230009, '54I-53390', 'Xe đạp đơn', 1000000, 'Romance'),
(20230010, '04J-86267', 'Xe đạp điện đơn', 1500000, 'Asama'),
(20230011, '86B-87545', 'Xe đạp điện đôi', 2000000, 'HKbike'),
(20230012, '62L-16479', 'Xe đạp đôi', 1200000, 'Kona'),
(20230013, '81N-56234', 'Xe đạp điện đơn', 1500000, 'Nijia'),
(20230014, '61G-26741', 'Xe đạp điện đôi', 2000000, 'Bridgestone'),
(20230015, '66U-13304', 'Xe đạp đơn', 1000000, 'Scott'),
(20230016, '34O-64121', 'Xe đạp điện đơn', 1500000, 'Bridgestone'),
(20230017, '06D-19921', 'Xe đạp đơn', 1000000, 'Romance'),
(20230018, '34E-77174', 'Xe đạp điện đôi', 2000000, 'Giant'),
(20230019, '70I-71974', 'Xe đạp điện đôi', 2000000, 'Bridgestone'),
(20230020, '70W-80640', 'Xe đạp điện đôi', 2000000, 'Bridgestone'),
(20230021, '38R-01793', 'Xe đạp đôi', 1200000, 'Santa Cruz'),
(20230022, '96O-67847', 'Xe đạp điện đôi', 2000000, 'Asama'),
(20230023, '63L-80236', 'Xe đạp điện đôi', 2000000, 'Honda'),
(20230024, '17U-32204', 'Xe đạp điện đôi', 2000000, 'Giant'),
(20230025, '23U-27113', 'Xe đạp đôi', 1200000, 'Trek'),
(20230026, '25I-41327', 'Xe đạp đơn', 1000000, 'Specialized'),
(20230027, '61K-65493', 'Xe đạp điện đơn', 1500000, 'BMX'),
(20230028, '79H-94520', 'Xe đạp điện đôi', 2000000, 'Asama'),
(20230029, '88B-43715', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230030, '63A-44287', 'Xe đạp điện đơn', 1500000, 'Honda'),
(20230031, '87U-49458', 'Xe đạp đôi', 1200000, 'Cannondale'),
(20230032, '43H-58994', 'Xe đạp đơn', 1000000, 'Cannondale'),
(20230033, '90Z-74755', 'Xe đạp điện đơn', 1500000, 'Honda'),
(20230034, '40A-89007', 'Xe đạp đôi', 1200000, 'Meride'),
(20230035, '66J-70408', 'Xe đạp điện đơn', 1500000, 'BMX'),
(20230036, '67M-64747', 'Xe đạp điện đôi', 2000000, 'HKbike'),
(20230037, '44O-84918', 'Xe đạp đơn', 1000000, 'GT'),
(20230038, '25Z-75501', 'Xe đạp đơn', 1000000, 'Scott'),
(20230039, '78U-21278', 'Xe đạp đơn', 1000000, 'Santa Cruz'),
(20230040, '63Y-19126', 'Xe đạp điện đôi', 2000000, 'HKbike'),
(20230041, '65F-45856', 'Xe đạp đôi', 1200000, 'Santa Cruz'),
(20230042, '29X-33911', 'Xe đạp đơn', 1000000, 'Scott'),
(20230043, '81I-22688', 'Xe đạp điện đơn', 1500000, 'Asama'),
(20230044, '99Y-32076', 'Xe đạp đơn', 1000000, 'GT'),
(20230045, '99C-43381', 'Xe đạp đôi', 1200000, 'Cannondale'),
(20230046, '36V-88634', 'Xe đạp điện đôi', 2000000, 'Hyundai'),
(20230047, '58B-95477', 'Xe đạp đôi', 1200000, 'Scott'),
(20230048, '74L-90191', 'Xe đạp điện đôi', 2000000, 'Bridgestone'),
(20230049, '60G-65926', 'Xe đạp điện đôi', 2000000, 'BMX'),
(20230050, '31K-71270', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230051, '88I-00669', 'Xe đạp điện đôi', 2000000, 'BMX'),
(20230052, '23X-41252', 'Xe đạp điện đôi', 2000000, 'Hyundai'),
(20230053, '01V-02670', 'Xe đạp điện đôi', 2000000, 'Hyundai'),
(20230054, '26C-03558', 'Xe đạp đôi', 1200000, 'Trek'),
(20230055, '81W-78935', 'Xe đạp điện đơn', 1500000, 'BMX'),
(20230056, '44G-08598', 'Xe đạp đôi', 1200000, 'Romance'),
(20230057, '42S-72850', 'Xe đạp đơn', 1000000, 'GT'),
(20230058, '05V-13866', 'Xe đạp đơn', 1000000, 'Meride'),
(20230059, '36F-18878', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230060, '31K-87685', 'Xe đạp đôi', 1200000, 'Giant'),
(20230061, '42A-36458', 'Xe đạp điện đôi', 2000000, 'Yamaha'),
(20230062, '92T-28657', 'Xe đạp đôi', 1200000, 'Meride'),
(20230063, '06Q-58673', 'Xe đạp đôi', 1200000, 'Kona'),
(20230064, '31B-42244', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230065, '75T-21040', 'Xe đạp đơn', 1000000, 'Scott'),
(20230066, '86X-45508', 'Xe đạp điện đôi', 2000000, 'Hyundai'),
(20230067, '76X-06575', 'Xe đạp đôi', 1200000, 'Cannondale'),
(20230068, '63X-02800', 'Xe đạp đôi', 1200000, 'Trek'),
(20230069, '23I-92936', 'Xe đạp đôi', 1200000, 'Romance'),
(20230070, '58T-36670', 'Xe đạp điện đơn', 1500000, 'Giant'),
(20230071, '95B-81282', 'Xe đạp đôi', 1200000, 'Trek'),
(20230072, '65N-90176', 'Xe đạp đơn', 1000000, 'GT'),
(20230073, '52N-77853', 'Xe đạp đôi', 1200000, 'Giant'),
(20230074, '24Q-86318', 'Xe đạp đơn', 1000000, 'Trek'),
(20230075, '88X-55235', 'Xe đạp đôi', 1200000, 'Giant'),
(20230076, '75C-48739', 'Xe đạp đơn', 1000000, 'Giant'),
(20230077, '35A-42935', 'Xe đạp đơn', 1000000, 'Meride'),
(20230078, '23H-91559', 'Xe đạp đơn', 1000000, 'Meride'),
(20230079, '98B-42917', 'Xe đạp điện đơn', 1500000, 'Giant'),
(20230080, '71V-74362', 'Xe đạp đôi', 1200000, 'GT'),
(20230081, '50T-06352', 'Xe đạp đôi', 1200000, 'Trek'),
(20230082, '28T-98866', 'Xe đạp đơn', 1000000, 'Romance'),
(20230083, '21V-89001', 'Xe đạp điện đơn', 1500000, 'Giant'),
(20230084, '01W-10497', 'Xe đạp đôi', 1200000, 'Giant'),
(20230085, '07P-74879', 'Xe đạp đôi', 1200000, 'Specialized'),
(20230086, '19U-08461', 'Xe đạp đôi', 1200000, 'Meride'),
(20230087, '17Q-13235', 'Xe đạp đơn', 1000000, 'GT'),
(20230088, '43H-17453', 'Xe đạp đơn', 1000000, 'Santa Cruz'),
(20230089, '24O-89056', 'Xe đạp điện đơn', 1500000, 'HKbike'),
(20230090, '07D-26417', 'Xe đạp đôi', 1200000, 'Kona'),
(20230091, '95X-46518', 'Xe đạp điện đơn', 1500000, 'Yamaha'),
(20230092, '03U-35125', 'Xe đạp đôi', 1200000, 'Trek'),
(20230093, '00P-72065', 'Xe đạp điện đơn', 1500000, 'BMX'),
(20230094, '44D-10842', 'Xe đạp đơn', 1000000, 'Giant'),
(20230095, '15E-72559', 'Xe đạp điện đơn', 1500000, 'Yamaha'),
(20230096, '04U-69559', 'Xe đạp điện đôi', 2000000, 'Asama'),
(20230097, '27Z-42322', 'Xe đạp điện đơn', 1500000, 'Nijia'),
(20230098, '97Z-22906', 'Xe đạp đôi', 1200000, 'Giant'),
(20230099, '69H-91395', 'Xe đạp đôi', 1200000, 'Meride'),
(20230100, '28H-79330', 'Xe đạp điện đơn', 1500000, 'Asama'),
(20230101, '89D-81637', 'Xe đạp đôi', 1200000, 'Cannondale'),
(20230102, '04I-30193', 'Xe đạp điện đôi', 2000000, 'Giant'),
(20230103, '49Y-88721', 'Xe đạp điện đơn', 1500000, 'Yamaha'),
(20230104, '96Z-45809', 'Xe đạp đôi', 1200000, 'Giant'),
(20230105, '23U-03151', 'Xe đạp đơn', 1000000, 'Romance'),
(20230106, '77R-78922', 'Xe đạp đơn', 1000000, 'Trek'),
(20230107, '77Y-16806', 'Xe đạp điện đôi', 2000000, 'Honda'),
(20230108, '01V-66635', 'Xe đạp điện đôi', 2000000, 'Asama'),
(20230109, '06J-86457', 'Xe đạp đơn', 1000000, 'Scott'),
(20230110, '15U-90648', 'Xe đạp đôi', 1200000, 'Marin'),
(20230111, '16Y-71622', 'Xe đạp đơn', 1000000, 'Marin'),
(20230112, '15H-11838', 'Xe đạp điện đôi', 2000000, 'BMX'),
(20230113, '60D-02559', 'Xe đạp điện đơn', 1500000, 'Bridgestone'),
(20230114, '23X-19067', 'Xe đạp điện đơn', 1500000, 'Bridgestone'),
(20230115, '93Z-12719', 'Xe đạp điện đôi', 2000000, 'Yamaha'),
(20230116, '70U-86999', 'Xe đạp điện đôi', 2000000, 'Asama'),
(20230117, '21H-98408', 'Xe đạp điện đôi', 2000000, 'Nijia'),
(20230118, '90X-71823', 'Xe đạp đơn', 1000000, 'Romance'),
(20230119, '74S-42868', 'Xe đạp đôi', 1200000, 'Specialized'),
(20230120, '93R-36787', 'Xe đạp đôi', 1200000, 'Meride'),
(20230121, '98I-29087', 'Xe đạp đôi', 1200000, 'Giant'),
(20230122, '65H-20054', 'Xe đạp đơn', 1000000, 'Specialized'),
(20230123, '38Z-16439', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230124, '09O-46497', 'Xe đạp điện đơn', 1500000, 'BMX'),
(20230125, '81N-59808', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230126, '33A-42441', 'Xe đạp điện đơn', 1500000, 'Yamaha'),
(20230127, '79A-95412', 'Xe đạp điện đôi', 2000000, 'Asama'),
(20230128, '15A-99372', 'Xe đạp đôi', 1200000, 'Giant'),
(20230129, '40Y-38890', 'Xe đạp đơn', 1000000, 'GT'),
(20230130, '83H-77242', 'Xe đạp đôi', 1200000, 'Giant'),
(20230131, '60K-28911', 'Xe đạp điện đơn', 1500000, 'Honda'),
(20230132, '43R-29273', 'Xe đạp đôi', 1200000, 'Santa Cruz'),
(20230133, '01D-34027', 'Xe đạp điện đơn', 1500000, 'Yamaha'),
(20230134, '65B-58115', 'Xe đạp đôi', 1200000, 'Kona'),
(20230135, '14V-92322', 'Xe đạp điện đơn', 1500000, 'Honda'),
(20230136, '25Q-05528', 'Xe đạp điện đôi', 2000000, 'Hyundai'),
(20230137, '56J-42420', 'Xe đạp điện đơn', 1500000, 'HKbike'),
(20230138, '73F-72467', 'Xe đạp điện đôi', 2000000, 'HKbike'),
(20230139, '13V-80078', 'Xe đạp điện đôi', 2000000, 'HKbike'),
(20230140, '58U-05239', 'Xe đạp điện đơn', 1500000, 'HKbike'),
(20230141, '52T-74965', 'Xe đạp điện đơn', 1500000, 'Giant'),
(20230142, '68B-63428', 'Xe đạp đôi', 1200000, 'Marin'),
(20230143, '22U-53644', 'Xe đạp điện đôi', 2000000, 'Hyundai'),
(20230144, '77B-47127', 'Xe đạp điện đơn', 1500000, 'Nijia'),
(20230145, '38K-33430', 'Xe đạp đơn', 1000000, 'Romance'),
(20230146, '13A-23996', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230147, '71F-33839', 'Xe đạp đơn', 1000000, 'Specialized'),
(20230148, '79X-66251', 'Xe đạp điện đôi', 2000000, 'BMX'),
(20230149, '70J-27147', 'Xe đạp điện đôi', 2000000, 'Asama'),
(20230150, '26K-03789', 'Xe đạp điện đơn', 1500000, 'BMX'),
(20230151, '48F-93782', 'Xe đạp điện đơn', 1500000, 'Giant'),
(20230152, '71J-13483', 'Xe đạp đôi', 1200000, 'Cannondale'),
(20230153, '04T-77741', 'Xe đạp đôi', 1200000, 'Meride'),
(20230154, '27X-13284', 'Xe đạp đôi', 1200000, 'Santa Cruz'),
(20230155, '12F-44179', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230156, '29P-85332', 'Xe đạp đơn', 1000000, 'GT'),
(20230157, '84T-22299', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230158, '07S-85852', 'Xe đạp đôi', 1200000, 'Santa Cruz'),
(20230159, '89Z-36771', 'Xe đạp điện đôi', 2000000, 'Yamaha'),
(20230160, '68U-44500', 'Xe đạp đơn', 1000000, 'Cannondale'),
(20230161, '21O-18178', 'Xe đạp điện đôi', 2000000, 'Honda'),
(20230162, '60T-42034', 'Xe đạp đơn', 1000000, 'Meride'),
(20230163, '67A-11392', 'Xe đạp đôi', 1200000, 'Santa Cruz'),
(20230164, '34W-79199', 'Xe đạp đôi', 1200000, 'Trek'),
(20230165, '20U-37617', 'Xe đạp đôi', 1200000, 'Trek'),
(20230166, '38U-81846', 'Xe đạp điện đơn', 1500000, 'HKbike'),
(20230167, '91I-79495', 'Xe đạp điện đôi', 2000000, 'Yamaha'),
(20230168, '43K-02463', 'Xe đạp đôi', 1200000, 'Romance'),
(20230169, '97X-07618', 'Xe đạp đôi', 1200000, 'Santa Cruz'),
(20230170, '75X-44431', 'Xe đạp điện đôi', 2000000, 'Hyundai'),
(20230171, '68B-75859', 'Xe đạp đôi', 1200000, 'Trek'),
(20230172, '48L-98692', 'Xe đạp đôi', 1200000, 'Trek'),
(20230173, '32J-73148', 'Xe đạp điện đôi', 2000000, 'BMX'),
(20230174, '21I-92008', 'Xe đạp điện đôi', 2000000, 'HKbike'),
(20230175, '23I-34949', 'Xe đạp đôi', 1200000, 'Romance'),
(20230176, '77Y-32705', 'Xe đạp điện đôi', 2000000, 'Giant'),
(20230177, '72E-33000', 'Xe đạp đôi', 1200000, 'Cannondale'),
(20230178, '49G-15047', 'Xe đạp đơn', 1000000, 'Marin'),
(20230179, '64U-26940', 'Xe đạp điện đơn', 1500000, 'BMX'),
(20230180, '83I-50117', 'Xe đạp đôi', 1200000, 'Cannondale'),
(20230181, '78L-53678', 'Xe đạp điện đơn', 1500000, 'HKbike'),
(20230182, '02D-34619', 'Xe đạp đơn', 1000000, 'Romance'),
(20230183, '67M-51409', 'Xe đạp đôi', 1200000, 'GT'),
(20230184, '32L-55794', 'Xe đạp đơn', 1000000, 'Santa Cruz'),
(20230185, '06O-20888', 'Xe đạp đơn', 1000000, 'Meride'),
(20230186, '74B-65404', 'Xe đạp đôi', 1200000, 'Marin'),
(20230187, '55Q-78275', 'Xe đạp điện đơn', 1500000, 'Hyundai'),
(20230188, '14I-73217', 'Xe đạp điện đôi', 2000000, 'Giant'),
(20230189, '30Z-01956', 'Xe đạp đơn', 1000000, 'Specialized'),
(20230190, '37R-95616', 'Xe đạp đôi', 1200000, 'Giant'),
(20230191, '42Y-87913', 'Xe đạp điện đôi', 2000000, 'Bridgestone'),
(20230192, '81S-94086', 'Xe đạp đôi', 1200000, 'Meride'),
(20230193, '93D-88797', 'Xe đạp đôi', 1200000, 'Marin'),
(20230194, '87S-18503', 'Xe đạp điện đôi', 2000000, 'Bridgestone'),
(20230195, '32B-65248', 'Xe đạp đơn', 1000000, 'Romance'),
(20230196, '99Q-31089', 'Xe đạp điện đôi', 2000000, 'Asama'),
(20230197, '61P-60495', 'Xe đạp đôi', 1200000, 'Meride'),
(20230198, '12P-39829', 'Xe đạp điện đôi', 2000000, 'Hyundai'),
(20230199, '42R-86570', 'Xe đạp điện đôi', 2000000, 'Nijia'),
(20230200, '20C-89855', 'Xe đạp đôi', 1200000, 'Meride'),
(20230201, '53C-31620', 'Xe đạp đơn', 1000000, 'Specialized'),
(20230202, '09C-54482', 'Xe đạp đơn', 1000000, 'Romance'),
(20230203, '40K-02204', 'Xe đạp đơn', 1000000, 'Marin'),
(20230204, '90L-96306', 'Xe đạp đôi', 1200000, 'Romance'),
(20230205, '38Q-97904', 'Xe đạp đôi', 1200000, 'Scott');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `xe_dang_duoc_thue`
--

CREATE TABLE `xe_dang_duoc_thue` (
  `maXe` int(11) NOT NULL,
  `maThe` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nguoiThueXe` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `phuongThucThueXe` varchar(100) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `thoiDiemThue` datetime NOT NULL,
  `noiThueXe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `xe_dang_duoc_thue`
--

INSERT INTO `xe_dang_duoc_thue` (`maXe`, `maThe`, `nguoiThueXe`, `phuongThucThueXe`, `thoiDiemThue`, `noiThueXe`) VALUES
(20230004, '225252685159', 'Nguyễn Thành Phong', 'Gói 24h', '2023-02-14 19:59:00', 2),
(20230006, '695667583966', 'Nguyễn Văn Trọng', 'Gói 24h', '2023-02-11 21:52:00', 1),
(20230008, '857344335650', 'Trần Văn Bảo', 'Gói 24h', '2023-02-09 22:58:00', 2),
(20230009, '590921461488', 'Nguyễn Thị Hoàng', 'Bình thường', '2023-02-14 17:55:00', 1),
(20230010, '949834436164', 'Nguyễn Thị Quyên', 'Gói 24h', '2023-02-20 11:55:00', 4),
(20230013, '102665576043', 'Lê Văn Phước', 'Bình thường', '2023-02-14 21:37:00', 3),
(20230014, '211605879626', 'Lê Thị Phương', 'Bình thường', '2023-02-03 05:39:00', 2),
(20230015, '586448084536', 'Huỳnh Hữu Tấn', 'Bình thường', '2023-02-03 15:14:00', 3),
(20230016, '754396685872', 'Nguyễn Thị Thu Hiền', 'Bình thường', '2023-02-19 20:12:00', 4),
(20230018, '957620951876', 'Nguyễn Thị Hạnh', 'Bình thường', '2023-02-03 08:39:00', 4),
(20230020, '852905412485', 'Nguyễn Thị Ngọc Trang', 'Bình thường', '2023-02-10 05:48:00', 4),
(20230021, '519487974694', 'Ngô Thị Thùy', 'Gói 24h', '2023-02-02 10:17:00', 3),
(20230022, '186295769911', 'Ngô Đình Phong', 'Gói 24h', '2023-02-09 10:10:00', 1),
(20230023, '771694027917', 'Trần Thị Thuỳ', 'Bình thường', '2023-02-17 05:16:00', 4),
(20230024, '645656237953', 'Lê Văn Trọng', 'Gói 24h', '2023-02-13 01:32:00', 1),
(20230025, '579045490443', 'Đoàn Phạm Anh', 'Gói 24h', '2023-02-11 06:43:00', 4),
(20230028, '785002628058', 'Hồ Thị Thu', 'Gói 24h', '2023-02-20 04:18:00', 2),
(20230029, '264922209149', 'Lê Thị Tuyết', 'Gói 24h', '2023-02-02 18:52:00', 4),
(20230032, '168264394829', 'Phạm Thị Thuý', 'Gói 24h', '2023-02-18 02:01:00', 4),
(20230033, '930266721660', 'Phạm Thị Minh', 'Bình thường', '2023-02-08 01:07:00', 1),
(20230034, '264492324799', 'Trần Thị Thanh Bình', 'Bình thường', '2023-02-20 03:20:00', 1),
(20230040, '851683364820', 'Đỗ Quang Huy', 'Gói 24h', '2023-02-03 17:10:00', 1),
(20230042, '642775003092', 'Hoàng Thị Tuyết', 'Bình thường', '2023-02-11 07:07:00', 2),
(20230044, '453052783562', 'Trần Văn Sơn', 'Bình thường', '2023-02-15 09:59:00', 4),
(20230046, '399045479505', 'Phạm Văn Tuấn', 'Bình thường', '2023-02-02 17:58:00', 2),
(20230047, '860819796103', 'Nguyễn Thị Thu', 'Bình thường', '2023-02-11 20:36:00', 1),
(20230049, '660924040421', 'Trần Thị Huyền', 'Gói 24h', '2023-02-15 16:47:00', 2),
(20230050, '453514911486', 'Trần Thị Nhàn', 'Gói 24h', '2023-02-10 17:09:00', 2),
(20230051, '153609006588', 'Trần Văn Nghĩa', 'Bình thường', '2023-02-19 12:48:00', 1),
(20230053, '583054474835', 'Nguyễn Văn Lộc', 'Gói 24h', '2023-02-11 14:04:00', 1),
(20230054, '558958057866', 'Nguyễn Thị Phương', 'Bình thường', '2023-02-05 03:49:00', 4),
(20230057, '511462006474', 'Nguyễn Thị Phượng', 'Gói 24h', '2023-02-09 17:13:00', 1),
(20230060, '928375590891', 'Hoàng Thị Nhàn', 'Bình thường', '2023-02-01 14:57:00', 3),
(20230061, '262665015243', 'Trần Tuấn Khải', 'Gói 24h', '2023-02-03 18:17:00', 2),
(20230062, '828339806264', 'Trần Văn Hoàng', 'Bình thường', '2023-02-11 18:10:00', 3),
(20230063, '628285077729', 'Nguyễn Văn Thắng', 'Gói 24h', '2023-02-06 16:18:00', 2),
(20230064, '987641655060', 'Nguyễn Thị Thanh', 'Bình thường', '2023-02-03 00:56:00', 4),
(20230065, '606121628899', 'Nguyễn Thị Tuyết', 'Bình thường', '2023-02-13 04:07:00', 1),
(20230066, '461379877579', 'Trần Văn Phúc', 'Gói 24h', '2023-02-09 03:39:00', 3),
(20230067, '733356703470', 'Lê Hoàng Thịnh', 'Gói 24h', '2023-02-20 22:49:00', 3),
(20230068, '951605987625', 'Bùi Minh Hải', 'Bình thường', '2023-02-17 08:57:00', 4),
(20230070, '260775285736', 'Nguyễn Văn Hải', 'Bình thường', '2023-02-20 10:28:00', 4),
(20230075, '230965852465', 'Nguyễn Thị Hằng', 'Gói 24h', '2023-02-14 13:38:00', 2),
(20230079, '849192317158', 'Lê Thị Thu', 'Gói 24h', '2023-02-11 19:52:00', 4),
(20230080, '955519958661', 'Nguyễn Thị Miêu', 'Bình thường', '2023-02-01 21:42:00', 2),
(20230081, '899660450162', 'Nguyễn Văn Tiến', 'Bình thường', '2023-02-03 18:29:00', 2),
(20230083, '302198599643', 'Nguyễn Quang Nhật', 'Bình thường', '2023-02-15 14:24:00', 1),
(20230084, '398571919658', 'Trần Văn Nhật', 'Gói 24h', '2023-02-16 16:56:00', 2),
(20230086, '107625601157', 'Cao Thị Nga', 'Gói 24h', '2023-02-10 01:26:00', 2),
(20230088, '769563292452', 'Phạm Văn Hiệp', 'Gói 24h', '2023-02-13 13:55:00', 3),
(20230090, '623606628948', 'Trần Văn Hải', 'Gói 24h', '2023-02-13 21:27:00', 1),
(20230092, '163505210968', 'Nguyễn Hồng Nhung', 'Gói 24h', '2023-02-18 09:33:00', 1),
(20230093, '187751602370', 'Lý Trần Tuấn', 'Gói 24h', '2023-02-17 18:12:00', 1),
(20230095, '461410577895', 'Nguyễn Văn Dũng', 'Gói 24h', '2023-02-17 14:59:00', 4),
(20230097, '465313101360', 'Nguyễn Văn Tài', 'Gói 24h', '2023-02-10 21:15:00', 4),
(20230099, '590395145166', 'Trần Hoàng Thịnh', 'Bình thường', '2023-02-11 00:20:00', 4),
(20230100, '656501639465', 'Trần Thị Thanh', 'Gói 24h', '2023-02-12 21:43:00', 4),
(20230101, '398599303707', 'Trần Văn Bằng', 'Bình thường', '2023-02-20 17:22:00', 2),
(20230102, '468080563288', 'Nguyễn Thị Ngọc', 'Bình thường', '2023-02-12 07:46:00', 4),
(20230103, '193576633933', 'Nguyễn Thị Thu Thảo', 'Gói 24h', '2023-02-09 09:21:00', 2),
(20230104, '980092956980', 'Trần Thị Kỳ', 'Gói 24h', '2023-02-02 21:46:00', 3),
(20230105, '259607780629', 'Lê Đình Minh', 'Bình thường', '2023-02-01 02:17:00', 4),
(20230106, '363386207079', 'Nguyễn Văn Nhật', 'Gói 24h', '2023-02-11 15:34:00', 1),
(20230107, '130835232366', 'Nguyễn Văn Phú', 'Gói 24h', '2023-02-18 20:06:00', 2),
(20230108, '634316581638', 'Nguyễn Thị Ngọc Anh', 'Bình thường', '2023-02-19 10:25:00', 1),
(20230111, '744630591954', 'Vũ Tấn Phát', 'Bình thường', '2023-02-01 09:51:00', 3),
(20230112, '628846787069', 'Nguyễn Văn Tường', 'Gói 24h', '2023-02-02 10:02:00', 4),
(20230115, '188813843608', 'Phan Quốc Thịnh', 'Gói 24h', '2023-02-19 16:46:00', 2),
(20230116, '509971874588', 'Trần Văn Quang', 'Gói 24h', '2023-02-05 23:56:00', 1),
(20230117, '398362098370', 'Trần Thị Tuyết', 'Gói 24h', '2023-02-03 12:37:00', 3),
(20230120, '130756258764', 'Trần Thị Ngọc', 'Gói 24h', '2023-02-12 19:30:00', 4),
(20230122, '593784983310', 'Trần Thị Thu', 'Bình thường', '2023-02-17 02:30:00', 4),
(20230123, '402092816536', 'Nguyễn Thị Diệu', 'Bình thường', '2023-02-18 04:53:00', 4),
(20230128, '358110378544', 'Lê Thị Thu Hà', 'Gói 24h', '2023-02-16 11:57:00', 3),
(20230131, '374925534796', 'Nguyễn Văn Thành', 'Gói 24h', '2023-02-03 14:23:00', 1),
(20230135, '613400353975', 'Trần Văn Thạch', 'Bình thường', '2023-02-08 01:14:00', 2),
(20230136, '618822372761', 'Đinh Hồng Quân', 'Gói 24h', '2023-02-18 00:57:00', 4),
(20230137, '518002775897', 'Trần Văn Đạt', 'Bình thường', '2023-02-18 21:30:00', 4),
(20230139, '510166138497', 'Nguyễn Văn Tú', 'Gói 24h', '2023-02-01 00:55:00', 1),
(20230141, '177083932755', 'Nguyễn Thị Huyền', 'Gói 24h', '2023-02-06 00:47:00', 2),
(20230143, '830622716264', 'Lê Thị Hoài', 'Gói 24h', '2023-02-03 10:13:00', 3),
(20230146, '154759837017', 'Nguyễn Văn Hiền', 'Gói 24h', '2023-02-06 10:55:00', 3),
(20230147, '371068393154', 'Nguyễn Văn Phúc', 'Bình thường', '2023-02-03 06:28:00', 2),
(20230152, '501099777188', 'Nguyễn Văn Thông', 'Gói 24h', '2023-02-18 21:01:00', 1),
(20230153, '484442484993', 'Lê Văn Thịnh', 'Gói 24h', '2023-02-03 14:10:00', 1),
(20230154, '645628515687', 'Nguyễn Thị Hương', 'Gói 24h', '2023-02-05 19:29:00', 2),
(20230157, '483087152095', 'Nguyễn Thị Kim Anh', 'Bình thường', '2023-02-06 02:37:00', 1),
(20230158, '501441353891', 'Lê Thị Hồng', 'Bình thường', '2023-02-18 04:24:00', 2),
(20230161, '243438556927', 'Nguyễn Văn Thịnh', 'Gói 24h', '2023-02-08 19:38:00', 2),
(20230164, '694529923247', 'Trần Văn Phong', 'Gói 24h', '2023-02-19 14:58:00', 2),
(20230166, '368119510205', 'Trần Văn Đức', 'Gói 24h', '2023-02-19 02:50:00', 4),
(20230167, '162193142493', 'Phạm Thị Thu Hà', 'Bình thường', '2023-02-18 19:01:00', 2),
(20230168, '987024786973', 'Trần Thị Hồng', 'Gói 24h', '2023-02-14 03:06:00', 3),
(20230170, '469350484470', 'Nguyễn Văn Sơn', 'Gói 24h', '2023-02-01 18:18:00', 2),
(20230174, '684767302165', 'Trần Văn Hưng', 'Gói 24h', '2023-02-14 05:10:00', 4),
(20230175, '948974694391', 'Phạm Văn Lâm', 'Bình thường', '2023-02-09 02:25:00', 4),
(20230177, '932895008270', 'Nguyễn Vũ Thịnh', 'Gói 24h', '2023-02-12 16:00:00', 4),
(20230178, '472440251368', 'Trần Thị Ngọc Hạnh', 'Bình thường', '2023-02-08 05:07:00', 4),
(20230179, '258375469702', 'Trần Thị Nhung', 'Gói 24h', '2023-02-15 06:47:00', 1),
(20230180, '737079741769', 'Trần Văn Cường', 'Bình thường', '2023-02-02 23:33:00', 1),
(20230181, '409635389108', 'Lê Văn Thuận', 'Bình thường', '2023-02-04 10:43:00', 2),
(20230182, '831875535162', 'Đỗ Thị Ngân', 'Bình thường', '2023-02-01 07:45:00', 2),
(20230183, '413742216698', 'Nguyễn Văn Hậu', 'Bình thường', '2023-02-06 14:27:00', 2),
(20230186, '782773015087', 'Nguyễn Thị Mỹ', 'Bình thường', '2023-02-03 22:06:00', 4),
(20230187, '544965525898', 'Trần Thị Phương Thảo', 'Bình thường', '2023-02-12 12:56:00', 2),
(20230188, '868123960674', 'Võ Thị Lầm', 'Gói 24h', '2023-02-13 03:16:00', 4),
(20230189, '311426689233', 'Lê Thị Minh', 'Bình thường', '2023-02-13 21:54:00', 4),
(20230190, '377754957728', 'Trần Thị Phương Anh', 'Gói 24h', '2023-02-05 20:57:00', 2),
(20230191, '175253003122', 'Trần Đình Phong', 'Gói 24h', '2023-02-20 09:48:00', 2),
(20230193, '685375251874', 'Nguyễn Văn Hùng', 'Bình thường', '2023-02-20 15:52:00', 2),
(20230194, '347811644555', 'Nguyễn Thị Hồng', 'Gói 24h', '2023-02-14 14:24:00', 2),
(20230196, '365187158738', 'Phạm Thu Hiền', 'Gói 24h', '2023-02-04 14:11:00', 2),
(20230198, '498024063486', 'Nguyễn Văn Tâm', 'Gói 24h', '2023-02-09 19:43:00', 2),
(20230200, '252035429477', 'Lữ Toàn Quân', 'Gói 24h', '2023-02-06 02:25:00', 3),
(20230202, '594917190863', 'Nguyễn Thị Thảo', 'Gói 24h', '2023-02-03 05:12:00', 2),
(20230205, '928065823817', 'Trần Văn Lực', 'Gói 24h', '2023-02-07 15:50:00', 2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `xe_dien`
--

CREATE TABLE `xe_dien` (
  `maXe` int(11) NOT NULL,
  `luongPin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `xe_dien`
--

INSERT INTO `xe_dien` (`maXe`, `luongPin`) VALUES
(20230004, 0),
(20230005, 80),
(20230006, 85),
(20230007, 89),
(20230010, 91),
(20230011, 84),
(20230013, 87),
(20230014, 86),
(20230016, 62),
(20230018, 86),
(20230019, 90),
(20230020, 73),
(20230022, 67),
(20230023, 80),
(20230024, 89),
(20230027, 75),
(20230028, 78),
(20230029, 86),
(20230030, 63),
(20230033, 87),
(20230035, 64),
(20230036, 71),
(20230040, 86),
(20230043, 65),
(20230046, 82),
(20230048, 98),
(20230049, 78),
(20230050, 96),
(20230051, 96),
(20230052, 83),
(20230053, 75),
(20230055, 61),
(20230059, 88),
(20230061, 81),
(20230064, 91),
(20230066, 100),
(20230070, 90),
(20230079, 84),
(20230083, 67),
(20230089, 60),
(20230091, 62),
(20230093, 90),
(20230095, 75),
(20230096, 60),
(20230097, 85),
(20230100, 67),
(20230102, 96),
(20230103, 82),
(20230107, 71),
(20230108, 63),
(20230112, 86),
(20230113, 87),
(20230114, 78),
(20230115, 62),
(20230116, 83),
(20230117, 68),
(20230123, 74),
(20230124, 95),
(20230125, 79),
(20230126, 64),
(20230127, 88),
(20230131, 69),
(20230133, 98),
(20230135, 74),
(20230136, 80),
(20230137, 91),
(20230138, 63),
(20230139, 64),
(20230140, 69),
(20230141, 89),
(20230143, 94),
(20230144, 66),
(20230146, 80),
(20230148, 66),
(20230149, 86),
(20230150, 60),
(20230151, 92),
(20230155, 87),
(20230157, 88),
(20230159, 80),
(20230161, 70),
(20230166, 79),
(20230167, 66),
(20230170, 91),
(20230173, 65),
(20230174, 91),
(20230176, 84),
(20230179, 64),
(20230181, 77),
(20230187, 66),
(20230188, 93),
(20230191, 64),
(20230194, 97),
(20230196, 83),
(20230198, 90),
(20230199, 67);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `xe_trong_nha_xe`
--

CREATE TABLE `xe_trong_nha_xe` (
  `maXe` int(11) NOT NULL,
  `maNhaXe` int(11) NOT NULL,
  `viTri` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `thoiDiemNhanXe` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `xe_trong_nha_xe`
--

INSERT INTO `xe_trong_nha_xe` (`maXe`, `maNhaXe`, `viTri`, `thoiDiemNhanXe`) VALUES
(20230001, 1, 'a2', '2023-02-22 09:41:00'),
(20230002, 2, 'B4', '2023-02-14 20:40:00'),
(20230003, 2, 'a2', '2023-02-05 21:12:13'),
(20230005, 2, 'c1', '2023-02-14 13:56:51'),
(20230007, 1, 'A6', '2023-01-15 01:01:00'),
(20230011, 1, 'B9', '2023-01-26 16:43:00'),
(20230012, 3, 'C6', '2023-01-03 16:21:00'),
(20230017, 1, 'E0', '2023-01-28 18:15:00'),
(20230019, 1, 'D8', '2023-01-02 05:22:00'),
(20230026, 2, 'C7', '2023-01-30 08:23:00'),
(20230027, 3, 'F6', '2023-01-25 20:02:00'),
(20230030, 2, 'D9', '2023-01-03 07:38:00'),
(20230031, 1, 'B4', '2023-01-23 22:17:00'),
(20230035, 4, 'A0', '2023-01-18 03:03:00'),
(20230036, 3, 'E0', '2023-01-21 03:03:00'),
(20230037, 2, 'B3', '2023-01-27 23:17:00'),
(20230038, 2, 'G2', '2023-01-18 01:58:00'),
(20230039, 4, 'E4', '2023-01-19 17:02:00'),
(20230041, 2, 'A5', '2023-01-15 17:57:00'),
(20230043, 3, 'E1', '2023-01-01 12:40:00'),
(20230045, 3, 'G4', '2023-01-13 10:18:00'),
(20230048, 2, 'F6', '2023-01-02 18:44:00'),
(20230052, 4, 'E5', '2023-01-23 01:37:00'),
(20230055, 4, 'E2', '2023-01-14 23:11:00'),
(20230056, 3, 'G0', '2023-01-29 15:16:00'),
(20230058, 2, 'C2', '2023-01-10 21:48:00'),
(20230059, 1, 'D9', '2023-01-23 12:44:00'),
(20230069, 4, 'F3', '2023-01-03 21:23:00'),
(20230071, 4, 'C9', '2023-01-18 13:34:00'),
(20230072, 4, 'F0', '2023-01-02 04:47:00'),
(20230073, 4, 'C2', '2023-01-19 16:14:00'),
(20230074, 2, 'E5', '2023-01-30 10:12:00'),
(20230076, 4, 'G3', '2023-01-27 10:27:00'),
(20230077, 1, 'F5', '2023-01-04 19:57:00'),
(20230078, 2, 'C2', '2023-01-05 10:39:00'),
(20230082, 2, 'B9', '2023-01-02 17:17:00'),
(20230085, 3, 'F8', '2023-01-25 07:29:00'),
(20230087, 2, 'C7', '2023-01-19 20:47:00'),
(20230089, 3, 'A6', '2023-01-18 21:07:00'),
(20230091, 4, 'B4', '2023-01-09 16:51:00'),
(20230094, 1, 'G6', '2023-01-31 20:33:00'),
(20230096, 4, 'A6', '2023-01-15 23:33:00'),
(20230098, 2, 'B9', '2023-01-06 14:39:00'),
(20230109, 1, 'D3', '2023-01-19 03:45:00'),
(20230110, 2, 'D9', '2023-01-13 20:16:00'),
(20230113, 1, 'G9', '2023-01-09 21:25:00'),
(20230114, 4, 'A7', '2023-01-05 07:16:00'),
(20230118, 4, 'D4', '2023-01-14 03:07:00'),
(20230119, 4, 'F5', '2023-01-21 00:54:00'),
(20230121, 2, 'C0', '2023-01-13 18:56:00'),
(20230124, 2, 'B1', '2023-01-03 14:06:00'),
(20230125, 4, 'F7', '2023-01-23 20:52:00'),
(20230126, 4, 'F0', '2023-01-13 05:32:00'),
(20230127, 1, 'B3', '2023-01-11 01:08:00'),
(20230129, 4, 'E1', '2023-01-25 17:13:00'),
(20230130, 1, 'A1', '2023-01-04 22:36:00'),
(20230132, 1, 'B4', '2023-01-17 18:09:00'),
(20230133, 3, 'A3', '2023-01-07 14:45:00'),
(20230134, 4, 'B1', '2023-01-09 04:07:00'),
(20230138, 4, 'E1', '2023-01-16 00:09:00'),
(20230140, 1, 'E6', '2023-01-28 14:45:00'),
(20230142, 1, 'A7', '2023-01-31 02:25:00'),
(20230144, 3, 'A2', '2023-01-31 23:40:00'),
(20230145, 4, 'A1', '2023-01-20 13:55:00'),
(20230148, 2, 'G8', '2023-01-22 13:10:00'),
(20230149, 1, 'E3', '2023-01-05 05:23:00'),
(20230150, 1, 'C9', '2023-01-11 11:01:00'),
(20230151, 4, 'A6', '2023-01-26 20:59:00'),
(20230155, 2, 'G4', '2023-01-20 08:04:00'),
(20230156, 3, 'C7', '2023-01-02 07:12:00'),
(20230159, 2, 'G7', '2023-01-24 10:24:00'),
(20230160, 1, 'D3', '2023-01-27 16:38:00'),
(20230162, 3, 'A3', '2023-01-31 04:54:00'),
(20230163, 1, 'E9', '2023-01-01 09:47:00'),
(20230165, 4, 'E7', '2023-01-08 17:43:00'),
(20230169, 3, 'G3', '2023-01-08 19:13:00'),
(20230171, 2, 'E5', '2023-01-18 17:10:00'),
(20230172, 1, 'A1', '2023-01-09 07:35:00'),
(20230173, 2, 'A9', '2023-01-06 07:54:00'),
(20230176, 4, 'B8', '2023-01-01 13:22:00'),
(20230184, 4, 'E5', '2023-01-05 13:24:00'),
(20230185, 4, 'G3', '2023-01-26 21:19:00'),
(20230192, 1, 'E3', '2023-01-06 03:10:00'),
(20230195, 4, 'B1', '2023-01-22 20:02:00'),
(20230197, 3, 'G1', '2023-01-16 13:40:00'),
(20230199, 2, 'E7', '2023-01-22 22:20:00'),
(20230201, 3, 'F3', '2023-01-17 05:04:00'),
(20230203, 3, 'A9', '2023-01-13 01:24:00'),
(20230204, 3, 'C8', '2023-01-25 19:40:00');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `hoa_don`
--
ALTER TABLE `hoa_don`
  ADD PRIMARY KEY (`maHoaDon`),
  ADD KEY `maNhaXe` (`maNhaXe`),
  ADD KEY `maXe` (`maXe`);

--
-- Chỉ mục cho bảng `nha_xe`
--
ALTER TABLE `nha_xe`
  ADD PRIMARY KEY (`maNhaXe`);

--
-- Chỉ mục cho bảng `xe`
--
ALTER TABLE `xe`
  ADD PRIMARY KEY (`maXe`),
  ADD UNIQUE KEY `bienSoXe` (`bienSoXe`);

--
-- Chỉ mục cho bảng `xe_dang_duoc_thue`
--
ALTER TABLE `xe_dang_duoc_thue`
  ADD PRIMARY KEY (`maXe`),
  ADD UNIQUE KEY `maThe` (`maThe`),
  ADD KEY `noiThueXe` (`noiThueXe`);

--
-- Chỉ mục cho bảng `xe_dien`
--
ALTER TABLE `xe_dien`
  ADD PRIMARY KEY (`maXe`);

--
-- Chỉ mục cho bảng `xe_trong_nha_xe`
--
ALTER TABLE `xe_trong_nha_xe`
  ADD PRIMARY KEY (`maXe`),
  ADD KEY `maNhaXe` (`maNhaXe`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `hoa_don`
--
ALTER TABLE `hoa_don`
  MODIFY `maHoaDon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `nha_xe`
--
ALTER TABLE `nha_xe`
  MODIFY `maNhaXe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT cho bảng `xe`
--
ALTER TABLE `xe`
  MODIFY `maXe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20230206;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `hoa_don`
--
ALTER TABLE `hoa_don`
  ADD CONSTRAINT `hoa_don_ibfk_1` FOREIGN KEY (`maNhaXe`) REFERENCES `nha_xe` (`maNhaXe`),
  ADD CONSTRAINT `hoa_don_ibfk_2` FOREIGN KEY (`maXe`) REFERENCES `xe` (`maXe`);

--
-- Các ràng buộc cho bảng `xe_dang_duoc_thue`
--
ALTER TABLE `xe_dang_duoc_thue`
  ADD CONSTRAINT `xe_dang_duoc_thue_ibfk_1` FOREIGN KEY (`maXe`) REFERENCES `xe` (`maXe`),
  ADD CONSTRAINT `xe_dang_duoc_thue_ibfk_2` FOREIGN KEY (`noiThueXe`) REFERENCES `nha_xe` (`maNhaXe`);

--
-- Các ràng buộc cho bảng `xe_dien`
--
ALTER TABLE `xe_dien`
  ADD CONSTRAINT `xe_dien_ibfk_1` FOREIGN KEY (`maXe`) REFERENCES `xe` (`maXe`);

--
-- Các ràng buộc cho bảng `xe_trong_nha_xe`
--
ALTER TABLE `xe_trong_nha_xe`
  ADD CONSTRAINT `xe_trong_nha_xe_ibfk_1` FOREIGN KEY (`maXe`) REFERENCES `xe` (`maXe`),
  ADD CONSTRAINT `xe_trong_nha_xe_ibfk_2` FOREIGN KEY (`maNhaXe`) REFERENCES `nha_xe` (`maNhaXe`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
