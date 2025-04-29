import pytest
from string_utils import StringUtils

utils = StringUtils()
 
@pytest.mark.parametrize("input_str, expected", [  
    ("skypro", "Skypro"),  
    ("hello Moskow", "Hello Moskow"),
    ("123") == "123"
    ("", ""),  
    (" ", " ")
    ("123test") == "123test"
])  
def test_capitalize(input_str, expected):  
    assert utils.capitalize(input_str) == expected 

@pytest.mark.parametrize("input_str, expected", [
    ("  test  ", "test"), 
    ("  hello ", "hello")
    ("") == ""
 ]) 
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected 

@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "S"), 
    ("SkyPro", "U"), 
    ("SkyPro", "t")
 ])
def test_contains(string, symbol):
    assert utils.contains(string: "SkyPro", symbol:"S") == True
    assert utils.contains(string: "SkyPro", symbol:"U") == False
    return symbol in string

@pytest.mark.parametrize("input_string, char_to_remove, expected_output",[
    ('repository', 'r', 'epository'),
    ('long-term', '-', 'longterm')
 ])
def test_delete_symbol(input_string, char_to_remove, expected_output):
    input_string = StringUtils()
    assert input_string.delete_symbol(input_string, char_to_remove) == expected_output
