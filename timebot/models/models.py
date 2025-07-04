from pydantic import BaseModel, RootModel, model_validator
from typing import Any


class BasicTask(BaseModel):
    name: str
    every: str | None = None
    subtasks: list["BasicTask"] | None = None
    times: int = 1

    @model_validator(mode="before")
    @classmethod
    def parse_any(cls, data):
        if isinstance(data, str):
            return {"name": data}
        if isinstance(data, dict):
            return data
        raise TypeError(f"Invalid task: {data}")


class TaskList(BaseModel):
    name: str | None = None
    tasks: list[BasicTask]

    @model_validator(mode="before")
    @classmethod
    def normalize_section(cls, data: Any):
        """
        Accepts either:
        - {"tasks": [...]}
        - [...]  (short form)
        """
        if isinstance(data, dict) and "tasks" in data:
            return data
        elif isinstance(data, list):
            return {"tasks": data}
        elif isinstance(data, str):
            return {"tasks": [data]}
        else:
            raise TypeError(f"Invalid section format: {data}")


class TaskListGroups(BaseModel):
    groups: list[TaskList]

    @model_validator(mode="before")
    @classmethod
    def normalize_section(cls, data: Any):
        """
        Accepts either:
        ```
        - name: A
          tasks:
            - ...
        ```
        OR
        ```
        A:
          tasks:
            - ...
        ```
        """
        if isinstance(data, str):
            return {"groups": [data]}

        if isinstance(data, list):
            return {"groups": [data]}

        elif isinstance(data, dict):
            if "tasks" in data:
                return {"groups": [data]}

            items = []
            for k, v in data.items():
                if not getattr(v, "name", ""):
                    v["name"] = k
                items.append(v)
            return {"groups": items}

        else:
            raise TypeError(f"Invalid section format: {data}")


class TopLevelFile(RootModel):
    root: dict[str, TaskList] | TaskList

    # @model_validator(mode="before")
    # @classmethod
    # def parse_top_level(cls, data: Any):
    # if isinstance(data, list):
    # raise TypeError("not yet")
    # if not isinstance(data, dict):
    # raise TypeError("not dict")

    # sections = []
    # for section_name, section_value in data.items():
    ## Build section including its name
    # print(section_value)
    ##breakpoint()
    # sections.append(
    # TaskSection(name=section_name, **section_value)
    # )
    # return {"sections": sections}

    # @model_validator(mode="before")
    # @classmethod
    # def parse_any(cls, data):
    # if 'tasks' not in data.keys():
    ## alternate syntax
    # return for k,v in data.items():

    # return data
