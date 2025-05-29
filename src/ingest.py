from pathlib import Path
from langchain.schema import Document

def load_paragraphs_from_pages(dir_path="data/talmud-pages"):
    all_docs = []
    base_path = Path(dir_path)
    for file_path in base_path.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        for idx, para in enumerate(paragraphs):
            all_docs.append(Document(
                page_content=para,
                metadata={
                    "source": str(file_path.name),
                    "paragraph_index": idx
                }
            ))
    return all_docs
