
select category_code, category_name, ref_category_code
from tbl_category
order by category_name DESC;

SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
WHERE menu_price
between 20000 and 30000
or menu_name like '%밥%';

SELECT menu_name, menu_price
FROM tbl_menu;


select category_code, category_name, ref_category_code, menu_price
from tbl_category
where category_name not like '%기타%, %쥬스%, %커피%'
and menu_price = 13000;