import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional

DATA_DIR = Path(__file__).parent


@dataclass(frozen=True)
class SearchTestData:
    id: str
    query: str
    expected_count: int
    description: str


def load_search_data(ids: Optional[Iterable[str]] = None) -> List[SearchTestData]:
    with open(DATA_DIR / "search_data.json", encoding="utf-8") as f:
        raw_data = json.load(f)["search_input"]

    if ids is not None:
        raw_data = [item for item in raw_data if item["id"] in ids]

    return [
        SearchTestData(
            id=item["id"],
            query=item["query"],
            expected_count=item["expected_result_count"],
            description=item["description"]
        )
        for item in raw_data
    ]
