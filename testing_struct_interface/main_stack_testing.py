import pytest
from stack_class import Stack
from exceptions import Empty_Exception, Null_Exception


@pytest.fixture
def new_stack():
    return Stack()


@pytest.fixture
def filled_stack(*data):
    def __stack_making(*data):
        return Stack(*data)

    return __stack_making


def test_stack_size(filled_stack):
    data = ["Y42 Book For Java", "Y42 Book For Python"]
    stack = filled_stack(*data)

    expected = len(data)
    real = stack.size()

    assert expected == real


def test_nvalue_push(new_stack):
    new_book = "Y42 book for C"
    new_stack.push(new_book)
    assert new_stack.size() == 1
    assert new_stack.peek() == new_book
#


def test_nonevalue_push(new_stack):
    new_book = None  # Null Element
    with pytest.raises(Null_Exception):
        new_stack.push(new_book)


def test_pop(filled_stack):
    books = ["Y42 Book For Java", "Y42 Book For Python"]
    stack = filled_stack(*books)
    expected = books[-1]
    real = stack.pop()

    assert expected == real
    assert stack.size() == len(books) - 1


def test_empty_pop(new_stack):
    with pytest.raises(Empty_Exception):
        new_stack.pop()


def test_peek(filled_stack):
    peek_ = "last_book"
    stack = filled_stack("Y42 Book For Java", "Y42 Book For Python", peek_)

    size_before_peek = stack.size()
    expected = peek_
    real = stack.peek()
    size_after_peek = stack.size()

    assert expected == real
    assert size_before_peek == size_after_peek


def test_empty_peek(new_stack):
    with pytest.raises(Empty_Exception):
        new_stack.peek()


def test_non_empty(filled_stack):
    stack = filled_stack("book")
    assert not stack.empty()


def test_empty(new_stack):
    assert new_stack.empty()
