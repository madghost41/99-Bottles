def bottle_song():
	for x in range (99, -1, -1):
		if x > 1:
			print(f"{x} bottles of beer on the wall, {x} bottles of beer. Take one down and pass it around, {x} bottles of beer on the wall.")

		elif x == 0:
			print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
		elif x == 1:
			print("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")
	

bottle_song()
