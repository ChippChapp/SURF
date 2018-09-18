# -*- coding: utf-8 -*-

import pytest

from g import functions as fn

def test_output_units():
    model_a_out, model_b_out = fn.create_model_output()
    assert isinstance(model_a_out, float)
    assert isinstance(model_b_out, float)

def test_input_is_output():
    model_a_out, model_b_out = fn.create_model_output()
    print str(model_a_out)
    print str(model_b_out)
    assert model_a_out == model_b_out, "output from model a and b"
    print 'hello World'
    