#!/usr/bin/env python3
import pytest
from gendiff import generate_diff

PATH_FILE1_JSON = 'tests/fixtures/file1.json'
PATH_FILE2_JSON = 'tests/fixtures/file2.json'
PATH_FILE1_YAML = 'tests/fixtures/file1.yaml'
PATH_FILE2_YAML = 'tests/fixtures/file2.yaml'
PATH_FILE1_YML = 'tests/fixtures/file1.yml'
PATH_FILE2_YML = 'tests/fixtures/file2.yml'
PATH_FILE1_NEST_JSON = 'tests/fixtures/file1_nest.json'
PATH_FILE2_NEST_JSON = 'tests/fixtures/file2_nest.json'
PATH_FILE1_NEST_YAML = 'tests/fixtures/file1_nest.yaml'
PATH_FILE2_NEST_YAML = 'tests/fixtures/file2_nest.yaml'
PATH_FILE1_NEST_YML = 'tests/fixtures/file1_nest.yml'
PATH_FILE2_NEST_YML = 'tests/fixtures/file2_nest.yml'
PATH_RESULT = 'tests/fixtures/result'
PATH_RESULT_NEST = 'tests/fixtures/result_nest'


def get_answer(path):
    with open(path) as file:
        string = file.read()
    return string

@pytest.mark.parametrize('file1, file2, result', [
    (PATH_FILE1_JSON, PATH_FILE2_JSON, PATH_RESULT),
    (PATH_FILE1_YML, PATH_FILE2_YML, PATH_RESULT),
    (PATH_FILE1_YAML, PATH_FILE2_YAML, PATH_RESULT),
    (PATH_FILE1_NEST_JSON, PATH_FILE2_NEST_JSON, PATH_RESULT_NEST),
    (PATH_FILE1_NEST_YML, PATH_FILE2_NEST_YML, PATH_RESULT_NEST),
    (PATH_FILE1_NEST_YAML, PATH_FILE2_NEST_YAML, PATH_RESULT_NEST),
])
def test_generated_diff(file1, file2, result):
    string = get_answer(result)
    assert string == generate_diff(file1, file2)

