""" 1 Tạo 1 func có 1 list items mà một người muốn trong cái 
bánh sandwich. Hàm đấy nên có 1 đối chứa nhiều nhất có thể 
items được truyền vào, Rồi in các items ra """

def sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print("- " + item)

""" Viết 1 hàm chứa thông tin về 1 ôtô trong 1 dictionary. 
HÀm luôn phải có đối số là tên nhà sản xuất (manufacturer) và tên mẫu (model).
hàm có thể gọi với bất kfi số lượng cặp key-value"""

def car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# Test the functions
sandwich('turkey', 'cheddar cheese', 'lettuce', 'mayo')
my_outback = car('subaru', 'outback', color='blue', tow_package=True)

print(my_outback)