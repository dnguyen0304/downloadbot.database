# -*- coding: utf-8 -*-

from nose.tools import (assert_equal,
                        assert_is_instance,
                        assert_is_none,
                        assert_is_not_none,
                        assert_true,
                        raises)

from .. import repositories


class MockModel:
    pass


class TestGenerateSid:

    def __init__(self):
        self.sid = None

    def setup(self):
        self.sid = repositories._generate_sid()

    def test_is_of_type_string(self):
        assert_is_instance(self.sid, str)

    def test_length(self):
        assert_true(len(self.sid) == repositories._SID_LENGTH)

    def test_is_alphanumeric(self):
        assert_true(self.sid.isalnum())


class TestSetSid:

    def __init__(self):
        self.model = None
        self.sid = None

    def setup(self):
        self.model = MockModel()
        self.model.models_sid = None
        self.sid = 'foo'

    def test_set_sid(self):
        repositories._set_sid(model=self.model, sid=self.sid)
        assert_is_not_none(self.model.models_sid)

    def test_set_sid_skips_protected_attributes(self):
        self.model._models_sid = None
        self.test_set_sid()
        assert_is_none(self.model._models_sid)

    @raises(AttributeError)
    def test_set_sid_no_sid_raises_exception(self):
        self.model = MockModel()
        self.test_set_sid()
