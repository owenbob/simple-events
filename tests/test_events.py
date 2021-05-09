
from tests.basetest import BaseTestCase
from tests.fixtures import (
    all_events,
    save_event_query,
    expected_save_event_result,
    query_by_paramaters_with_all_matching,
    query_by_paramaters_with_no_match,
    expected_query_by_paramaters_with_match,
    expected_query_by_paramaters_with_no_match
)


class TestEvents(BaseTestCase):
    def test_all_events(self):
        query_result = self.test_client.execute(all_events)
        assert len(query_result.get("data").get("events")) == 3

    def test_save_event(self):
        query_result = self.test_client.execute(save_event_query)
        assert query_result == expected_save_event_result

    def test_query_event_by_parameters(self):
        query_result_one = self.test_client.execute(
            query_by_paramaters_with_all_matching
        )
        assert query_result_one == expected_query_by_paramaters_with_match

        query_result_two = self.test_client.execute(
            query_by_paramaters_with_no_match
        )
        assert query_result_two == expected_query_by_paramaters_with_no_match
