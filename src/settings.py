from enum import Enum


ENTITY = "mini-projects"
PROJECT = "DL3"
DATA_DIR = "../data"


class JobType(Enum):
    UPLOAD_DATA = "upload-data"
    UPLOAD_CONFIG = "upload-config"
    DOWNLOAD_DATA = "download-data"
    TRAINING = "training"


class ArtifactType(Enum):
    DATASET = "dataset"
