#!/usr/bin/env python3
import pytest
from gendiff import generate_diff

def get_answer(path):
    with open(path) as file:
        string = file.read()
    return string


def test_generated_diff():
    string = get_answer('tests/fixtures/result')
    assert string == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
