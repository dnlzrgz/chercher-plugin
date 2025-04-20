from typing import Generator
from chercher import Document, hookimpl


@hookimpl
def ingest(uri: str, settings: dict) -> Generator[Document, None, None]:
    yield Document(uri=uri, content="")
