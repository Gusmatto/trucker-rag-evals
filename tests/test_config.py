import json

import pytest

from src import config


@pytest.mark.parametrize(
    "path", [config.KNOWLEDGE_BASE_PATH, config.GOLDEN_DATASET_PATH]
)
def test_data_file_is_a_json_array(path):
    assert path.exists(), f"missing {path}"
    assert isinstance(json.loads(path.read_text(encoding="utf-8")), list)


def test_top_k_is_three():
    assert config.TOP_K == 3
