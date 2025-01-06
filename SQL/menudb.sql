use menudb;
# DML
SELECT menu_code, menu_name, menu_price, category_code, orderable_status
FROM tbl_menu;

# INSERT
-- INSERT INTO 테이블명 VALUES (컬럼순으로, 삽일할, 데이터, 나열, ...)
INSERT INTO tbl_menu VALUES (null, '고기짬뽕', 9500, 6, 'Y' );

-- INSERT INTO 테이블명 (컬럼명1, 컬럼명2, 컬럼명3, ...)
-- VALUES (데이터1, 데이터2, 데이터3)
INSERT INTO tbl_menu(menu_code, menu_name, menu_price, category_code, orderable_status)
VALUES (null, '탕수육', 20000, 6, 'Y');

INSERT INTO tbl_menu(menu_code, menu_name, menu_price, category_code, orderable_status)
VALUES ('카페라떼', 4500, 7, 'Y');

-- MULTI INSERT
INSERT INTO tbl_menu
VALUES
(null, '콰트로치즈햄버거', 10500, 12, 'Y'),
(null, '프렌치프라이', 8900, 12, 'Y'),
(null, '코울슬로', 3000, 12, 'Y');

-- INSERT INTO tbl_menu VALUES (null, '100번 음식', 100, 10, 'Y');

# UPDATE
-- UPDATE 테이블명
--    SET 컬럼명1 = 수정할 데이터,
--        컬럼명2 = 수정할 데이터,
--        ...
-- [  WHERE 수정 대상 데이터 조건 ];

UPDATE tbl_menu
   SET menu_name = '100번이었던 음식'
		, menu_price = 19000
WHERE menu_code = 100;

# DELETE
-- DELETE FROM 테이블명 [ WHERE 삭제 조건 ];
DELETE
FROM tbl_menu
WHERE menu_code = 101;

DELETE
  FROM tbl_menu
ORDER BY menu_code DESC
LIMIT 3;


# REPLACE
-- REPLACE는 중복값에 대해서는 데이터를 덮어쓰고, 중복값이 없다면 INSERT한다. 
-- INTO 키워드 생략 가능
REPLACE INTO tbl_menu VALUES (100, '100번 음식 리플레이스!', 100000, 10, 'Y');
REPLACE tbl_menu VALUES (120, '없는 메뉴 리플레이스', 10101, 8, 'Y');
