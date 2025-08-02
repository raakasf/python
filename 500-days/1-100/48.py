import threading
def add_numbers(x, y):
	print(x + y)
t = threading.Thread(target=add_numbers, args=(5, 7))
t.start()
t.join()
