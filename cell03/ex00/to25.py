
value = int(input())

# หากตัวเลขที่ใส่เข้ามามีค่ามากกว่าหรือเท่ากับ 25: ให้แสดงผลคำว่า "Error"
if value >= 25:
	print("Error")
else:
	for num in range(value, 25):
		print(f"Inside the loop, my variable is {num}")
