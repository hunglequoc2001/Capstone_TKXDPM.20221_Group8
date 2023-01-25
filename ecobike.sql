-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th1 25, 2023 lúc 03:40 PM
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
(1, 'Lê Quốc Hưng', '136047_group08_20221', 20230002, 'Thuê xe', 1, '2023-01-14 12:00:00', 400000, 'Ecobikebank'),
(2, 'Trần Tiến Bằng', '136047_group09_20221', 20230004, 'thuê xe', 1, '2023-01-22 13:05:27', 600000, 'EcobikeBank'),
(7, 'Lê Quốc Hưng', '136047_group08_20221', 20230002, 'trả xe', 1, '2023-01-25 21:39:00', -200000, 'EcobikeBank');

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
(1, 'B6', 100, 'Bách Khoa, Hai Bà Trưng, Hà Nội', '09873126166', 'B6ktxBKHN@gmail.com');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `xe`
--

CREATE TABLE `xe` (
  `maXe` int(11) NOT NULL,
  `bienSoXe` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `loaiXe` varchar(100) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'Xe đạp đơn',
  `luongPin` int(11) NOT NULL DEFAULT 0,
  `giaTriXe` int(11) NOT NULL,
  `hangXe` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `xe`
--

INSERT INTO `xe` (`maXe`, `bienSoXe`, `loaiXe`, `luongPin`, `giaTriXe`, `hangXe`) VALUES
(20230001, '29A-12345', 'Xe đạp đơn', 0, 1000000, 'Merida'),
(20230002, '29A-18355', 'Xe đạp đơn', 0, 1000000, 'Merida'),
(20230003, '38A-52185', 'Xe đạp đôi', 0, 1200000, 'Specialized'),
(20230004, '46N-52185', 'Xe đạp điện đơn', 0, 1500000, 'Scott');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `xe_dang_duoc_thue`
--

CREATE TABLE `xe_dang_duoc_thue` (
  `maXe` int(11) NOT NULL,
  `maThe` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nguoiThueXe` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `phuongThucThueXe` int(11) NOT NULL DEFAULT 0,
  `thoiDiemThue` datetime NOT NULL,
  `noiThueXe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `xe_dang_duoc_thue`
--

INSERT INTO `xe_dang_duoc_thue` (`maXe`, `maThe`, `nguoiThueXe`, `phuongThucThueXe`, `thoiDiemThue`, `noiThueXe`) VALUES
(20230004, '136047_group09_20221', 'Trần Tiến Bằng', 0, '2023-01-22 13:05:27', 1);

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
(20230001, 1, 'a1', '2023-01-25 21:40:01'),
(20230002, 1, 'h2', '2023-01-15 11:40:48'),
(20230003, 1, 'c1', '2023-01-14 08:47:33');

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
  ADD PRIMARY KEY (`maXe`);

--
-- Chỉ mục cho bảng `xe_dang_duoc_thue`
--
ALTER TABLE `xe_dang_duoc_thue`
  ADD PRIMARY KEY (`maXe`),
  ADD UNIQUE KEY `maThe` (`maThe`),
  ADD KEY `noiThueXe` (`noiThueXe`);

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
  MODIFY `maNhaXe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `xe`
--
ALTER TABLE `xe`
  MODIFY `maXe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20230005;

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
-- Các ràng buộc cho bảng `xe_trong_nha_xe`
--
ALTER TABLE `xe_trong_nha_xe`
  ADD CONSTRAINT `xe_trong_nha_xe_ibfk_1` FOREIGN KEY (`maXe`) REFERENCES `xe` (`maXe`),
  ADD CONSTRAINT `xe_trong_nha_xe_ibfk_2` FOREIGN KEY (`maNhaXe`) REFERENCES `nha_xe` (`maNhaXe`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
