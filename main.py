from stats import create_dictionary
from stats import count_words
from stats import create_ordered_dicts
import sys
def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    print(file_contents)

def main(bookName):
    fPath = bookName
    words = count_words(fPath)
    dic = create_dictionary(fPath)
    #print(str(words) + " words found in the document")
    #print(dic)
    lstDicts = create_ordered_dicts(dic)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + fPath + "...")
    print("----------- Word Count ----------")
    print("Found " + str(words) + " total words")
    print("--------- Character Count -------")
    for i in lstDicts:
        print(i["char"] + ": " + str(i["num"]))
    print("============= END ===============")
if __name__=="__main__":
    if (len(sys.argv) == 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookName = sys.argv[1]
    main(bookName)
