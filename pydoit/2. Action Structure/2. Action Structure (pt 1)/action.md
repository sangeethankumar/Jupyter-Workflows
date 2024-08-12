The `dodo.py` file defines several tasks, each of which contains a single action—a function that returns a specific value.

1. **`task_return_true`**:
   - **Action**: A function `return_true` that returns `True`.
   - **Result**: This task will successfully complete because it returns `True`, which is considered a successful outcome.

2. **`task_return_none`**:
   - **Action**: A function `return_none` that returns `None`.
   - **Result**: This task will also successfully complete because returning `None` is treated as a successful outcome.

3. **`task_return_dictionary`**:
   - **Action**: A function `return_dict` that returns a dictionary with a single key-value pair (`{'return': 'Yes'}`).
   - **Result**: This task will successfully complete because returning a dictionary is recognized as a successful outcome.

4. **`task_return_string`**:
   - **Action**: A function `return_str` that returns the string `"Yes"`.
   - **Result**: This task will successfully complete because returning a string is considered a successful outcome.

5. **`task_return_false`**:
   - **Action**: A function `return_false` that returns `False`.
   - **Result**: This task will be considered to have generally failed because returning `False` is indicative of a task failure.

6. **`task_raise_exception`**:
   - **Action**: A function `raise_exception` that raises an `Exception` with the message `'Nope'`.
   - **Result**: This task will result in an error because it raises an exception, which is treated as a task error.

