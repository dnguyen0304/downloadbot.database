# -*- coding: utf-8 -*-

from nose.tools import (assert_equal,
                        assert_is_instance,
                        assert_is_none,
                        assert_is_not_none,
                        assert_true,
                        raises)

from .. import models
from .. import repositories


class MockModel(models.Base):

    def __init__(self):
        super().__init__()


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


class TestSetMetadata:

    def __init__(self):
        self.entity = None
        self.by = None

    def set_up(self, is_new):
        self.entity = MockModel()
        self.by = -1
        if not is_new:
            self.entity.created_at = self.entity.created_by = 'foo'
        repositories._set_metadata(entity=self.entity, by=self.by)

    def test_set_metadata_create_new_entity(self):
        self.set_up(is_new=True)
        assert_is_not_none(self.entity.created_at)
        assert_equal(self.by, self.entity.created_by)

    def test_set_metadata_update_existing_entity(self):
        self.set_up(is_new=False)
        assert_is_not_none(self.entity.updated_at)
        assert_equal(self.by, self.entity.updated_by)
