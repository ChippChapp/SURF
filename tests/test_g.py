#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the g module.
"""
import pytest

from g import g


def test_without_test_object():
    assert False


class TestG(object):
    @pytest.fixture
    def return_a_test_object(self):
        pass

    def test_g(self, g):
        assert False

    def test_with_error(self, g):
        with pytest.raises(ValueError):
            pass
