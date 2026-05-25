#THE LIST OF BOOKS YOU OWN
books=[]
your_books=input('Enter the name of a book you own: ')
books.append(your_books)
another_book=input("Enter the name of another book you own (or press 'Enter' to skip):")
if another_book:
   books.append(another_book)
   print("Your Library:")
   print(books)
else:
   print("Your Library:")
   print(books)
  #THE LIST OF BOOKS YOU WISH TO HAVE 
books2=[]
wish_books=input('Enter the name of a book you wish to have in the future: ')
books2.append(wish_books)
another_wish=input("Enter the name of another book you wish to have (or press 'Enter' to skip):")
if another_wish:
   books2.append(another_wish)
   print("Your Wishlist:")
   print(books2)
else:
  print("Your wishlist:")
  print(books2)
   #THE LIST OF BOOKS YOU ALREADY HAVED FROM THE WISHLIST
wish_achieved=input("Enter the name of a book from your wishist that you have acquired (or press 'Enter' to skip):")
if wish_achieved:
   books.append(wish_achieved)
   books2.remove(wish_achieved)
   print("Update Library:")
   print(books)
   print("Update Wishlist:")
   print(books2)
donate_book=input("Enter the name of a book from your library you want to donate (or press 'Enter' to skip):")
if donate_book:
   books.remove(donate_book)
   print("Final Library after Donations:")
   print(books)
else:
   print("Final Library after Donations:")
   print(books)
  

