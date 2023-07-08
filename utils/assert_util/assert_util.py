from conftest import LOGGER
from typing import Any
from utils.data_sets import AssertMethods


class AssertUtil:
    def _complete_match(self, want: Any, validation: Any):
        assert want == validation

    def _include(self, want: Any, validation: Any):
        assert want in validation

    def _non_match(self, want: Any, validation: Any):
        assert want != validation

    def _non_include(self, want: Any, validation: Any):
        assert want not in validation

    @classmethod
    def assert_with_log(cls, want: Any, validation: Any, methods: AssertMethods = AssertMethods.complete_match):
        assertutil = AssertUtil()
        try:
            getattr(assertutil, f"_{methods}")(want, validation)
        except Exception as e:
            LOGGER.warning(f"{e}\n\tAssert with log:\n\t\twant: {want}\n\t\tvalidation: {validation}")
