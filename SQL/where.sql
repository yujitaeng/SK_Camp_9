# where

-- 1) 비교 연산자
SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
WHERE orderable_status = 'Y';

SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
WHERE orderable_status <> 'Y';

SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
WHERE menu_price <= 10000;

-- SELECT menu_name, menu_price, orderable_status
-- FROM tbl_menu
-- WHERE 10000 < menu_price <= 20000;

-- 2) AND
SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
WHERE 10000 < menu_price 
and menu_price <= 20000;

-- 3) OR
SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
where menu_price > 30000
or menu_name = '열무김치라떼';

-- 4) BETWEEN
SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
WHERE menu_price between 10000 and 20000;

SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
WHERE menu_price not between 10000 and 20000;

-- 5) LIKE
SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
where menu_name like '%김치%';

SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
where menu_name not like '%김치%';

-- 6) IN
SELECT menu_name, menu_price, orderable_status, category_code
FROM tbl_menu
where category_code = 4
or category_code = 5
or category_code = 6;

SELECT menu_name, menu_price, orderable_status, category_code
FROM tbl_menu
where category_code not in (4, 5, 6);

-- 7) IS NULL
select category_code, category_name, ref_category_code
from tbl_category
where ref_category_code is not null;
