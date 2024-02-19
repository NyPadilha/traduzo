import json
from src.models.history_model import HistoryModel


def test_request_history():
    history = HistoryModel.list_as_json()

    assert json.loads(history)[0]["translate_to"] == "pt"
    assert json.loads(history)[0]["translate_from"] == "en"
    assert (
        json.loads(history)[0]["text_to_translate"]
        == "Hello, I like videogame"
    )
