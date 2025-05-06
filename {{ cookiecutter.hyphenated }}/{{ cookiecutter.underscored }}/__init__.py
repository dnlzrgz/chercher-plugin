from typing import Generator
from chercher import Document, hookimpl


@hookimpl
def ingest(uri: str, settings: dict) -> Generator[Document, None, None]:
    yield Document(uri="", title="", body="", hash="", metadata={})


@hookimpl
def prune(uri: str, settings: dict) -> bool | None:
    return None
