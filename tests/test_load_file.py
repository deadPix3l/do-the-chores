from hypothesis import given, strategies as st

from timebot.file import *
from timebot.models import *


@given(st.text(min_size=1))
def test_load_single_str_task(s):
    x = load_obj_as_model(s)
    assert isinstance(x, TaskListGroups)
    assert len(x.groups) == 1
    y = x.groups[0]
    assert len(y.tasks) == 1
    assert y.tasks[0].name == s


@given(st.lists(st.text(min_size=1), min_size=1))
def test_load_multiple_str_tasks_as_list(s):
    x = load_obj_as_model(s)
    assert isinstance(x, TaskListGroups)
    assert len(x.groups) == 1
    assert [i.name for i in x.groups[0].tasks] == s


@given(st.lists(st.text(min_size=1), min_size=1))
def test_load_tasks_list_dict(s):
    x = load_obj_as_model({"tasks": s})
    assert isinstance(x, TaskListGroups)
    assert len(x.groups) == 1
    assert len(x.groups[0].tasks) == len(s)
    assert [i.name for i in x.groups[0].tasks] == s


# def test_load_basic_task_dict(s):
#    assert isinstance(_load_obj_as_model(s), TopLevelFile)

# def test_load_basic_task(s):
#    assert isinstance(_load_obj_as_model(s), TopLevelFile)

# def test_load_basic_task(s):
#    assert isinstance(_load_obj_as_model(s), TopLevelFile)
