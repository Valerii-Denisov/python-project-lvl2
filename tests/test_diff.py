#!/usr/bin/env python3
import pytest
from gendiff import generate_diff

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'
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
PATH_RESULT_STYLISH_FLAT = 'tests/fixtures/result_stylish_flat'
PATH_RESULT_STYLISH_NEST = 'tests/fixtures/result_stylish_nest'
PATH_RESULT_PLAIN_FLAT = 'tests/fixtures/result_plain_flat'
PATH_RESULT_PLAIN_NEST = 'tests/fixtures/result_plain_nest'
PATH_RESULT_JSON_FLAT = 'tests/fixtures/result_json_flat'
PATH_RESULT_JSON_NEST = 'tests/fixtures/result_json_nest'


def get_answer(path):
    with open(path) as file:
        string = file.read()
    return string


@pytest.mark.parametrize('file1, file2, result, format', [
    (PATH_FILE1_JSON, PATH_FILE2_JSON, PATH_RESULT_STYLISH_FLAT, STYLISH),
    (PATH_FILE1_YML, PATH_FILE2_YML, PATH_RESULT_STYLISH_FLAT, STYLISH),
    (PATH_FILE1_YAML, PATH_FILE2_YAML, PATH_RESULT_STYLISH_FLAT, STYLISH),
    (PATH_FILE1_NEST_JSON, PATH_FILE2_NEST_JSON, PATH_RESULT_STYLISH_NEST, STYLISH),
    (PATH_FILE1_NEST_YML, PATH_FILE2_NEST_YML, PATH_RESULT_STYLISH_NEST, STYLISH),
    (PATH_FILE1_NEST_YAML, PATH_FILE2_NEST_YAML, PATH_RESULT_STYLISH_NEST, STYLISH),
    (PATH_FILE1_JSON, PATH_FILE2_JSON, PATH_RESULT_PLAIN_FLAT, PLAIN),
    (PATH_FILE1_YML, PATH_FILE2_YML, PATH_RESULT_PLAIN_FLAT, PLAIN),
    (PATH_FILE1_YAML, PATH_FILE2_YAML, PATH_RESULT_PLAIN_FLAT, PLAIN),
    (PATH_FILE1_NEST_JSON, PATH_FILE2_NEST_JSON, PATH_RESULT_PLAIN_NEST, PLAIN),
    (PATH_FILE1_NEST_YML, PATH_FILE2_NEST_YML, PATH_RESULT_PLAIN_NEST, PLAIN),
    (PATH_FILE1_NEST_YAML, PATH_FILE2_NEST_YAML, PATH_RESULT_PLAIN_NEST, PLAIN),
    (PATH_FILE1_JSON, PATH_FILE2_JSON, PATH_RESULT_JSON_FLAT, JSON),
    (PATH_FILE1_YML, PATH_FILE2_YML, PATH_RESULT_JSON_FLAT, JSON),
    (PATH_FILE1_YAML, PATH_FILE2_YAML, PATH_RESULT_JSON_FLAT, JSON),
    (PATH_FILE1_NEST_JSON, PATH_FILE2_NEST_JSON, PATH_RESULT_JSON_NEST, JSON),
    (PATH_FILE1_NEST_YML, PATH_FILE2_NEST_YML, PATH_RESULT_JSON_NEST, JSON),
    (PATH_FILE1_NEST_YAML, PATH_FILE2_NEST_YAML, PATH_RESULT_JSON_NEST, JSON),
])
def test_generated_diff(file1, file2, result, format):
    string = get_answer(result)
    assert string == generate_diff(file1, file2, format)
