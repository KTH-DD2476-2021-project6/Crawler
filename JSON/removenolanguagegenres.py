import jsonlines
data = []
#read the original files with all the books
with jsonlines.open('book_best_books_01_100.jl') as f:
    for item in f:
        #if the item does not have a 'genres' or 'language' key, we ignore it.
        if 'genres' not in item:
            pass
        elif 'language' not in item:
            pass
        #else we append it to data.
        else:
            data.append(item)
f.close()

#then we write the updated books to a new file.
with jsonlines.open('book_goodversion.jl', 'w') as f:
    for i in data:
        f.write(i)
f.close()
