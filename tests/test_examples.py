import sys

try:
    import pytest
    from lectrick.__main__ import map_command_impl
except ModuleNotFoundError:
    print("Please install pytest and lectrick.")
    sys.exit(1)
    
def test_examples():
    example_paths = ["examples/chars", "examples/hello"]
    
    for example in example_paths:
        mapped = map_command_impl(example, "", return_out=True)
        
        if mapped:
            with open(f"{example}.csv", "r") as map:
                if mapped == map.read():
                    assert True
                else:
                    assert False
        else:
            assert False