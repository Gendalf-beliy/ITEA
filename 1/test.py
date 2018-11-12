from home_work import Stack
import pytest

class TestClass(object):
    """
    Class for testing home_task 1
    """
    def test_default_instance(self):
        news = Stack()
        assert news.limit is None
        assert news.type is object

    def test_type_limit(self):
        news = Stack(data_type=int, limit=5)
        assert news.limit == 5
        assert news.type is int

    def test_push_over_limit(self):
        news = Stack(data_type=int, limit=1)
        news.push(7)
        with pytest.raises(Stack.LimitExceedError):
            news.push(2)

    def test_push_another_type(self):
        news = Stack(data_type=int, limit=5)
        with pytest.raises(Stack.TypeError):
            news.push('abcd')

    def test_pull(self):
        news = Stack(data_type=int, limit=5)
        news.push(7)
        news.pull()
        with pytest.raises(Stack.EmptyStackError):
            news.pull()

    def test_count(self):
        news = Stack(data_type=str, limit=5)
        news.push('a')
        news.push('b')
        news.push('c')
        assert news.count() == 3

    def test_clear(self):
        news = Stack(data_type=str, limit=5)
        news.push('a')
        news.push('b')
        news.push('c')
        news.clear()
        assert news.count() == 0

    def test_type(self):
        news = Stack(data_type=bool)
        assert news.type is bool

    def test_str(self):
        news = Stack()
        assert news.__str__() == 'Stack<object>'
