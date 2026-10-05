from prompt_toolkit import prompt
import getpass

t = prompt("What is your name: ", default=f"{getpass.getuser()}")