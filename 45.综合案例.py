import my_utils.str_util
print(my_utils.str_util.str_reverse("hei"))
print(my_utils.str_util.substr("itheima",1, 6))
from my_utils import file_util
file_util.print_file_info("D:/bill.txt.txt")
file_util.append_to_file("D:/test_append.txt.txt", "hello")