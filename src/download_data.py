from settings import ENTITY, PROJECT, JobType
import wandb


def download_data(artifact_name: str):
    with wandb.init(
        project=PROJECT, entity=ENTITY, job_type=JobType.DOWNLOAD_DATA.value
    ) as run:
        data_artifact = run.use_artifact(f"{artifact_name}:latest")
        bedrooms_directory = data_artifact.download()
