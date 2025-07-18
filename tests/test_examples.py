import logging
import sys

try:
    import pytest
    from lectrick.__main__ import map_command_impl
except ModuleNotFoundError:
    print("Please install pytest and lectrick.")
    sys.exit(1)

log = logging.getLogger(__name__)
    
def test_examples():
    example_paths = ["examples/chars", "examples/hello", "examples/quiet"]
    
    for example in example_paths:
        mapped = map_command_impl(example, "", return_out=True)
        alternate_engine_mapped = map_command_impl(example, "", return_out=True, alternate_engine=True)
        if alternate_engine_mapped:  # If this fails, it will only warn, not fail the test
            with open(f"{example}.csv", "r") as map:
                if alternate_engine_mapped != map.read():
                    log.warning(f"Alternate engine mapping for {example} does not match expected output.")
        else:
            log.warning(f"Alternate engine mapping for {example} returned None, expected a string output.")
            assert False
        if mapped:
            with open(f"{example}.csv", "r") as map:
                if mapped == map.read():
                    assert True
                else:
                    assert False
        else:
            assert False
