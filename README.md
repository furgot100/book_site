## 1.How would we filter for all books with titles containing the word ‘Django’?
We would use Book.objects.filter(book__title='Django')

## 2. How would we filter for all books with tag ‘Fiction’?
Tag.objects.filter(name='Fiction')

## 3.How would we filter for all authors who have written books containing the word ‘Django’?
Author.objects.filter(book__title='Django')
