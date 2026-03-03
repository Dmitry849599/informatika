# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
volume = 1.44*1024*1024
v_symbole = 4
v_book = pages*lines*symbols*v_symbole
quantity_book = volume//v_book
print("Количество книг, помещающихся на дискету:", int(quantity_book))
