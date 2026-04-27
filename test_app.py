import pytest
from app import process_data


def test_process_data_success():
    assert process_data([10, 20]) == 15


from app import process_data

from app import process_data

def test_process_data_empty():
    # This will fail and trigger the SRE Agent
    assert process_data([]) == 0
