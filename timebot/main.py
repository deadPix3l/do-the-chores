#!/usr/bin/env python3
import yaml

def load_file_as_model(yaml_file):
    with open(yaml_file, 'r') as f:
        yml = f.read()

    data = yaml.safe_load(yml)
    model = TopLevelModel(**data)
    #print(model)
    #print(model.model_dump_json(exclude_none=True, indent=2))
    return model

def checkfile_cli():
    import fire
    fire.Fire(load_file_as_model)

if __name__=="__main__":
    checkfile_cli()

