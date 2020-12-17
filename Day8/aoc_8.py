import time
from typing import Union

def run_script(filepath: str) -> Union[int, str, float, bool]:
    with open(filepath, "r") as f:
        raw_data = f.read()
    return main_function(raw_data)

def main_function(raw_data: str) -> Union[int, str, float, bool]:
    start_time = time.time()
    
    result = your_script(raw_data)

    elapsed_time = time.time() - start_time
    print(f"Time elapsed : {elapsed_time}s")
    return result

def your_script(raw_data: str) -> Union[int, str, float, bool]:
    """
    Time to code! Write your code here to solve today's problem
    """
    program = Program(raw_data.split("\n"))
    program.debug_run()
    return program.accumulator

class Program:

    def __init__(self, commands: list):
        self.commands = []
        for command in commands:
            self.commands.append(command)
        self.index = 0
        self.explored = []
        self.accumulator = 0

    def copy(self):
        new_program = Program(self.commands)
        new_program.index = self.index
        for idx in self.explored:
            new_program.explored.append(idx)
        new_program.accumulator = self.accumulator
        return new_program

    def debug_run(self) -> int:
        while True:
            self.explored.append(self.index)
            if self.run_debug(self.index):
                print(f"Exit found! Change line {self.index + 1}")
                self.transform_current()
                self.run_until_loop_or_end()
                return self.accumulator
            next_index = self.run_command(self.index)
            if next_index in self.explored:
                break
            self.index = next_index

    def run_until_loop_or_end(self) -> bool:
        while True:
            self.explored.append(self.index)
            next_index = self.run_command(self.index)
            if next_index in self.explored:
                print(self.explored)
                return False
            if next_index >= len(self.commands):
                return True
            self.index = next_index

    def run_debug(self, command_index) -> bool:
        next_line = self.commands[command_index]
        command, delta = next_line.split(" ")
        next_index = command_index
        if command == "acc":
            return False
        else:
            new_program = self.copy()
            new_program.transform_current()
            return new_program.run_until_loop_or_end()

    def transform_current(self):
        current_line = self.commands[self.index]
        if "nop" in current_line:
            self.commands[self.index] = current_line.replace("nop", "jmp")
        else:
            self.commands[self.index] = current_line.replace("jmp", "nop")

    def run_command(self, command_index) -> int:
        next_line = self.commands[command_index]
        command, delta = next_line.split(" ")
        next_index = command_index
        if command == "nop":
            next_index += 1
        elif command == "acc":
            self.accumulator += int(delta)
            next_index += 1
        elif command == "jmp":
            next_index += int(delta)
        return next_index

if __name__ == "__main__":
    print(run_script("input.txt"))