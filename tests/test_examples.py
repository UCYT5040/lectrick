import logging
import sys

try:
    import pytest
    from lectrick.__main__ import map_command_impl
except ModuleNotFoundError:
    print("Please install lectrick[test].")
    sys.exit(1)

log = logging.getLogger(__name__)

example_paths = ["examples/chars", "examples/hello", "examples/quiet", "examples/press"]

@pytest.mark.parametrize("program_path", example_paths)
def test_example(program_path):    
    mapped = map_command_impl(program_path, "", return_out=True)
    alternate_engine_mapped = map_command_impl(program_path, "", return_out=True, alternate_engine=True)
    if alternate_engine_mapped:  # If this fails, it will only warn, not fail the test
        with open(f"{program_path}.csv", "r") as map:
            if alternate_engine_mapped != map.read():
                log.warning(f"Alternate engine mapping for {program_path} does not match expected output.")
    else:
        log.warning(f"Alternate engine mapping for {program_path} returned None, expected a string output.")
        assert False
    if mapped:
        with open(f"{program_path}.csv", "r") as map:
            if mapped == map.read():
                assert True
            else:
                log.warning("Maps didn't match up")
                log.warning(mapped)
                assert False
    else:
        assert False
