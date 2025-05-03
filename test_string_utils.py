import pytest
from string_utils import StringUtils

utils = StringUtils()
 
@pytest.mark.parametrize("input_str, expected", [  
    ("skypro", "Skypro"),  
    ("hello Moskow", "Hello Moskow"),
    ("123", "123"),
    ("", ""),  
    (" ", " "),
    ("123test", "123test") 
])  
def test_capitalize(input_str, expected):  
    assert utils.capitalize(input_str) == expected 

@pytest.mark.parametrize("input_str, expected", [
    ("  test  ", "test"), 
    ("  hello ", "hello"),
    ("") == ""
 ]) 
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected 

@pytest.mark.parametrize("string, symbol, expected", [  
    ("SkyPro", "S", True),  
    ("SkyPro", "U", False)  
])  

def test_contains(string, symbol):
    assert utils.contains(string, symbol) == expected
    

@pytest.mark.parametrize("input_string, char_to_remove, expected_output",[
    ('repository', 'r', 'epository'),
    ('long-term', '-', 'longterm')
 ])
def test_delete_symbol(input_string, char_to_remove, expected_output):
    assert utils.delete_symbol(input_string, char_to_remove) == expected_output 
