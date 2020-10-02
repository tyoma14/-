

class Page:
    def __init__(self, content: str):
        self.content = content


class Book:
    def __init__(self, name: str, authors: set, pages: list, table_of_contents: dict):
        self.name = name
        self.authors = authors
        self.pages = pages
        self.table_of_contents = table_of_contents

    def find_pages_by_chapter_name(self, chapter_name: str):
        if chapter_name in self.table_of_contents:
            start_page_num = self.table_of_contents.get(chapter_name)
            end_page_num = min([page_num for page_num in self.table_of_contents.values() if page_num > start_page_num], default=len(self.pages))-1
            return self.pages[start_page_num:end_page_num+1]
        raise Exception("Chapter not found")

    def get_authors_in_alphabet_order(self):
        return sorted(self.authors)


def create_test_book():
    pages = [Page(str.format("Sample Text On Page {}", x)) for x in range(41)]
    table_of_contents = {"Intro": 0, "Chapter 1": 3, "Chapter 2": 9, "Chapter 3": 20, "Outro": 36}
    authors = {"Eric Freeman", "Elisabeth Robson", "Bert Bates", "Kathy Sierra"}
    return Book("Design Patterns", authors, pages, table_of_contents)


if __name__ == "__main__":
    test_book = create_test_book()
    print(test_book.get_authors_in_alphabet_order())
    chapter_pages = test_book.find_pages_by_chapter_name("Chapter 2")
    for page in chapter_pages:
        print(page.content)
