SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";



CREATE TABLE `user_progress` (
  `ID` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `progress_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;



INSERT INTO `user_progress` (`ID`, `user_id`, `progress_id`) VALUES
(1, 24, 342),
(2, 12, 234),
(3, 15, 323),
(4, 2, 323),
(5, 123, 1232);


ALTER TABLE `user_progress`
  ADD PRIMARY KEY (`ID`);



ALTER TABLE `user_progress`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;
