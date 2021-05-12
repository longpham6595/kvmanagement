# importing module multiprocessing
import multiprocessing
 
def print_cube(num):
    """
    Hàm in thể tích của khối lập phương
    """
    print("Giá trị lập phương: {}".format(num * num * num))
 
def print_square(num):
    """
    Hàm in diện tích hình vuông
    """
    print("Diện tích hình vuông: {}".format(num * num))
 
# Chương trình chính
if __name__ == "__main__":
    # Tạo hai tiến trình process
    p1 = multiprocessing.Process(target=print_square, args=(10, ))
    p2 = multiprocessing.Process(target=print_cube, args=(10, ))
 
    # Bắt đầu process 1
    p1.start()
    # Bắt đầu process 2
    p2.start()
 
    # Chờ tới khi process 1 hoàn thành
    p1.join()
    # Chờ tới khi process 2 hoàn thành
    p2.join()
 
    # Cả hai processes hoàn thành
    print("Done!")