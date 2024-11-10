# task-tracker

A simple command-line interface for managing tasks in a JSON file. This Python script allows you to add, list, update, and delete tasks efficiently

## Features

- Add tasks
- List tasks with optional status filtering
- Update task status or description
- Delete tasks

## Prerequisites

- Python 3.x
- Basic understanding of command line usage

## Installation

1. Clone this repository:
   
   ```bash
   git clone https://github.com/C0Mon/task-tracker.git
   cd task-tracker
   ```
2. Ensure you have Python installed. You can check your Python version by running:
   ```bash
   python --version
   ```
   

## Commands
### add
```bash
python task_manager.py add "Your task description"
```
This command adds a new task with the provided description. The status is set to "todo" by default.

### list

```bash
python task_manager.py list
```
This command lists all tasks. You can filter tasks by status (e.g., "todo", "in-progress", "done") by providing the status as an argument:

```bash
python task_manager.py list todo
```
### delete
```bash
python task_manager.py delete <task_id>
```
Replace <task_id> with the ID of the task you want to delete.
### update

```bash
python task_manager.py update <task_id> "New description"
```
Replace <task_id> with the ID of the task you want to update.

### mark-in-progress

```bash
python task_manager.py mark-in-progress <task_id>
```
Replace <task_id> with the ID of the task you want to mark as in progress.

### mark-done
```bash
python task_manager.py mark-done <task_id>
```
Replace <task_id> with the ID of the task you want to mark as done.

## File Structure

    data.json: Stores tasks in JSON format.
    task_manager.py: The main script for the task manager.
