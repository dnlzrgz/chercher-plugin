from typing import Generator
from chercher import Document, hook_impl


class IngestPlugin:
    """
    Chercher plugin.
    """

    @hook_impl
    def ingest(self, uri: str) -> Generator[Document, None, None]:
        yield Document(uri=uri, content="")
