from datetime import datetime
from typing import Any, Dict, List
import pandas as pd

from config.categories import documents


class dd_file:

    name: str
    extension: str
    streamlit_object: Any
    content: bytes
    extracted_content: str
    category: str
    ai_output: str

    def __init__(self, file_object: Any) -> None:
        self.name = file_object.name
        self.streamlit_object = file_object
        self.extension = file_object.name.split('.')[1]
        self.content = file_object.getvalue()

    def set_category(self, _category) -> None:
        self.category = _category

    def set_readable_content(self, _content: str) -> None:
        self.extracted_content = _content

    def set_ai_output(self, _output: str) -> None:
        self.ai_output = _output


class dd_contract:

    id: str
    files: Dict[str, dd_file]
    output_file: bytes
    created_at: datetime
    
    def __init__(self, _id: str) -> None:
        self.id: str = _id

    def set_files(self, file_list: List[Any]) -> None:
        self.files = {}
        for f in file_list:
            self.files[f.name] = dd_file(f)

    def files_to_pandas(self) -> pd.DataFrame:
        df = pd.DataFrame()
        df['Documento'] = [f"{documents[self.files[file].category]['name']} ({self.files[file].name})" for file in self.files.keys()]
        df['Perguntas'] = [documents[self.files[file].category]['questions'] for file in self.files.keys()]
        df['Respostas'] = [self.files[file].ai_output for file in self.files.keys()]
        return df