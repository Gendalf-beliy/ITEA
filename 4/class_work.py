import keyword

class Language:
    words = []

    @classmethod
    def lexicon(cls):
        return cls.words


class ProgLanguage:
    keywords = []

    @classmethod
    def lexicon(cls):
        return cls.keywords


class Python(ProgLanguage):
    keywords = keyword.kwlist


a = Python()
print(a.lexicon())