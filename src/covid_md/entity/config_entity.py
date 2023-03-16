from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen= True)
class DataPreprocessingConfig:
    root_dir: Path
    data_path: Path
    preprocess_records: Path

@dataclass(frozen=True)
class DataTrainingConfig:
    root_dir: Path
    data_path: Path
    test_size: float
    monitor: str
    verbose: int
    save_best_only: bool
    mode: str
    epochs: int
    validation_split: float
    model: str
@dataclass(frozen= True)
class MaskDetectionConfig:
    root_dir: Path
    face_classifier: Path