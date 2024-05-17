import glob
import os

from settings import DATA_DIR, ENTITY, PROJECT, ArtifactType, JobType
import wandb



def upload_raw_data():
    data_dir = os.path.join(DATA_DIR, "bedroom")
    print(data_dir)
    if os.path.exists(data_dir):
        print("Data directory exists")
        
    else:
        print("Data directory does not exist")
        # Code to execute if the path does not exist
        pass
    with wandb.init(
        project=PROJECT, entity=ENTITY, job_type=JobType.UPLOAD_DATA.value
    ) as run:
        artifact = wandb.Artifact(
            "bedrooms-raw",
            type=ArtifactType.DATASET.value,
            description="Raw bedroom files dataset",
        )

        files = glob.glob(os.path.join(data_dir, '**', "*.jpg"), recursive=True)
        for file in files:
            artifact.add_file(file,)
        run.log_artifact(artifact)


if __name__ == "__main__":
    upload_raw_data()
