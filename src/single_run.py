import argparse
import os

import wandb
import yaml
from lightning.pytorch.loggers import WandbLogger

from settings import ENTITY, PROJECT, JobType
from trainer.train import train


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run experiment from a yaml file")

    parser.add_argument("yaml_file", type=str)

    args = parser.parse_args()

    with open(os.path.join("yaml_configs", f"{args.yaml_file}.yaml"), "r") as file:
        config = yaml.safe_load(file)
    with wandb.init(
        project=PROJECT,
        entity=ENTITY,
        job_type=JobType.TRAINING.value,
        config=config,
    ) as run:
        config = wandb.config
        logger = WandbLogger(project=PROJECT, entity=ENTITY)
        data_artifact = run.use_artifact(f"{config.dataset}:latest")
        bedrooms_dir = data_artifact.download()

        config_dict = config.as_dict()

        if hasattr(config, "config_dir"):
            config_artifact = run.use_artifact(f"{config.config_dir}:latest")
            config_dict["config_dir"] = config_artifact.download()

        train(config_dict, bedrooms_dir, logger)
