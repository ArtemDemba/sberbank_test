import pytest

from src.handlers.handler import Handler
from .values_for_test import (input_dicts_for_splitting, expected_dicts_for_splitting,
                              first_dict, second_dict, expected_result)


@pytest.mark.parametrize('input_dict, expected_output', (
        (input_dicts_for_splitting[0], expected_dicts_for_splitting[0]),
        (input_dicts_for_splitting[1], expected_dicts_for_splitting[1])
))
@pytest.mark.asyncio
async def test_correct_splitting_dicts(input_dict, expected_output):
    result = await Handler.split_tree(input_dict)
    assert result == expected_output


@pytest.mark.parametrize('first_input_dict, second_input_dict, expected_output', (
    (first_dict, second_dict, expected_result),
))
@pytest.mark.asyncio
async def test_correct_merging_dicts(first_input_dict, second_input_dict, expected_output):
    result = await Handler.merge_trees([first_input_dict, second_input_dict])
    assert result == expected_output

