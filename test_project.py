import project
import pytest

def test_add_task():
    tasks = []
    new_tasks = project.add_task(tasks, "Buy groceries")
    assert len(new_tasks) == 1
    assert new_tasks[0] == "Buy groceries"

def test_complete_task():
    tasks = ["Buy groceries", "Finish homework"]
    new_tasks = project.complete_task(tasks, 0)
    assert len(new_tasks) == 1
    assert new_tasks[0] == "Finish homework"

def test_complete_task_invalid_index():
    tasks = ["Buy groceries"]
    new_tasks = project.complete_task(tasks, 1)
    assert len(new_tasks) == 1
    assert new_tasks[0] == "Buy groceries"

def test_view_tasks(capsys):
    tasks = ["Buy groceries", "Finish homework"]
    project.view_tasks(tasks)
    captured = capsys.readouterr()
    assert "1. Buy groceries" in captured.out
    assert "2. Finish homework" in captured.out

# Add more test functions as needed

if __name__ == "__main__":
    pytest.main(["-v", "test_project.py"])
