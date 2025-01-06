# order by

select menu_code, menu_name, menu_price
  from tbl_menu
order by menu_name ASC;  # 오름차순(기본정렬)

select menu_code, menu_name, menu_price
  from tbl_menu
order by menu_name DESC; # 내림차순

select menu_code, menu_name, menu_price
  from tbl_menu
order by menu_price, menu_name;

select menu_code, menu_name, menu_price, menu_code * menu_price
from tbl_menu
order by menu_code * menu_price;

select menu_code, menu_name, menu_price, menu_code * menu_price as '연산결과'
from tbl_menu
order by '연산결과';

select category_code, category_name, ref_category_code
from tbl_category
order by ref_category_code is null desc, ref_category_code DESC;