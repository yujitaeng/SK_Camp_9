# LIMIT

SELECT menu_code, menu_name, menu_price
FROM tbl_menu
ORDER BY menu_price DESC;

SELECT menu_code, menu_name, menu_price
FROM tbl_menu
ORDER BY menu_price DESC
LIMIT 5;