#!/usr/bin/env python3
import pytest
from gendiff import generate_diff

PATH_FILE1_JSON = 'tests/fixtures/file1.json'
PATH_FILE2_JSON = 'tests/fixtures/file2.json'
PATH_FILE1_YAML = 'tests/fixtures/file1.yaml'
PATH_FILE2_YAML = 'tests/fixtures/file2.yaml'
PATH_FILE1_YML = 'tests/fixtures/file1.yml'
PATH_FILE2_YML = 'tests/fixtures/file2.yml'
PATH_RESULT = 'tests/fixtures/result'


def get_answer(path):
    with open(path) as file:
        string = file.read()
    return string

@pytest.mark.parametrize('file1, file2, result', [
    (PATH_FILE1_JSON, PATH_FILE2_JSON, PATH_RESULT),
    (PATH_FILE1_YML, PATH_FILE2_YML, PATH_RESULT),
    (PATH_FILE1_YAML, PATH_FILE2_YAML, PATH_RESULT),
])
def test_generated_diff(file1, file2, result):
    string = get_answer('tests/fixtures/result')
    assert string == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')

