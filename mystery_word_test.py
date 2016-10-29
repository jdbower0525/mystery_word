from mystery_word import main

def test_even_numbers():
    assert is_palindrome('toot') == True

def test_odd_numbers():
    assert is_palindrome('tot') == True

def test_simple_values():
    assert is_palindrome('stunt nuts') == True

def test_complete_sentences():
    assert is_palindrome('Lisa Bonet ate no basil.') == True

def test_complex_sentences():
    assert is_palindrome('A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!') == True

def test_multiple_sentences():
    assert is_palindrome('Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.') == True

def test_non_palindromes():
    assert is_palindrome('i am not a palindrome') == False
