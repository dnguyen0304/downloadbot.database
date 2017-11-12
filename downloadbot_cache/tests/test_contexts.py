# -*- coding: utf-8 -*-


class MockEntityState:

    def __init__(self, is_transient, is_persistent):
        self.transient = is_transient
        self.persistent = is_persistent


class TestSetMetadata:

    def __init__(self):
        self.entity = None
        self.by = None

    def set_up(self, is_transient, is_persistent):
        self.entity = models.Model(created_at=None,
                                   created_by=0,
                                   updated_at=None,
                                   updated_by=0)
        entity_state = MockEntityState(is_transient=is_transient,
                                       is_persistent=is_persistent)
        self.by = -1
        contexts._set_metadata(entity=self.entity,
                               entity_state=entity_state,
                               by=self.by)

    def test_set_metadata_create_new_entity(self):
        self.set_up(is_transient=True, is_persistent=False)
        assert_is_not_none(self.entity.created_at)
        assert_equal(self.by, self.entity.created_by)

    def test_set_metadata_update_existing_entity(self):
        self.set_up(is_transient=False, is_persistent=True)
        assert_is_not_none(self.entity.updated_at)
        assert_equal(self.by, self.entity.updated_by)
