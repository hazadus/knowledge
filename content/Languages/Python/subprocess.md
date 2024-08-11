📂 [[Python]]
## Using `subprocess` to run external programs
### References
- [The subprocess Module: Wrapping Programs With Python](https://realpython.com/python-subprocess/#processes-and-subprocesses)

### Examples
```python
import subprocess

def get_current_username() -> str:  
    whoami_result = subprocess.run("whoami", capture_output=True)  
    return whoami_result.stdout.decode()
```

```python
def process_count(username: str) -> int:  
	ps_command_str = "ps -u {username}".format(username=username)  
	ps_command = shlex.split(ps_command_str)  
    ps_process = subprocess.run(ps_command, stdout=subprocess.PIPE)  
    wc_process = subprocess.run("wc", input=ps_process.stdout, stdout=subprocess.PIPE)  
  
    wc_output = wc_process.stdout.decode().split(" ")  
    wc_clean_output = [item for item in wc_output if item != ""]  
    process_qty = int(wc_clean_output[0]) - 1  
    return process_qty
```


----
📂 [[Python]]