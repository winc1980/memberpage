CREATE TABLE `profile` (
	`first_name` VARCHAR(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
	`last_name` VARCHAR(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
	`team` VARCHAR(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
	`fac,univ` VARCHAR(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
	`self_intro` TEXT,
	`img` TEXT
);

insert into profile values('Fuma', 'Suzuki', 'HPチーム', '早稲田大学社会科学部', '')