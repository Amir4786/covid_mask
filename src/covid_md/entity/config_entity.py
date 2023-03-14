from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen= True)
class DataPreprocessingConfig:
    root_dir: Path
    data_path: Path
    preprocess_records: Path