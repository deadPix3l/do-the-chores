#!/usr/bin/env python3
import yaml
from timebot.models import *


def load_file_as_model(yaml_file) -> TaskListGroups:
    with open(yaml_file, "r") as f:
        yml = f.read()

    data = yaml.safe_load(yml)
    return load_obj_as_model(data)


def load_obj_as_model(data: dict | list | str) -> TaskListGroups:
    model = TaskListGroups.model_validate(data)
    # print(model)
    # print(model.model_dump_json(exclude_none=True, indent=2))
    return model


def checkfile_with_json(yaml_file):
    model = load_file_as_model(yaml_file)
    print(model.model_dump_json(exclude_none=True, indent=2))
    return model


def checkfile_cli():
    import fire

    fire.Fire(checkfile_with_json)


if __name__ == "__main__":
    checkfile_cli()
