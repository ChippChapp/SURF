# -*- coding: utf-8 -*-

import pytest

from g import functions as fn

def test_output_units():
    model_a_out, model_b_out = fn.create_model_output()
    assert isinstance(model_a_out, float), "output model a not a float"
    assert isinstance(model_b_out, float), "output model b not a float"

def test_input_is_output():
    model_a_out, model_b_out = fn.create_model_output()
    print str(model_a_out)
    print str(model_b_out)
    assert model_a_out == 0.5 * model_b_out, "output from model a is not half of output from model b"
    print 'hello World'
    