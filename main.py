import os
import importlib
from datetime import datetime


class Terminal:
    def __init__(self):
        """Initializes the terminal, command history, and dynamically loads commands."""
        self.history = []
        self.commands = {}
        self._load_commands()

    def _load_commands(self):
        """Dynamically loads command modules from the 'commands' directory."""
        command_dir = 'commands'
        for filename in os.listdir(command_dir):
            # Load only .py files, excluding __init__.py
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]  # Remove .py extension
                try:
                    # Construct the full module path (e.g., commands.ls)
                    module = importlib.import_module(f"{command_dir}.{module_name}")
                    # Map the command name to its execute function
                    self.commands[module_name] = module.execute
                except Exception as e:
                    print(f"Error loading command '{module_name}': {e}")

        # Add special commands that need access to the Terminal's state (self)
        self.commands['history'] = self.handle_history

    def handle_history(self, args):
        """Displays the command history."""
        for i, (cmd_name, cmd_args, timestamp) in enumerate(self.history, 1):
            # Format arguments for display (join with spaces, quote if needed)
            if cmd_args:
                args_str = ' '.join(cmd_args)
                cmd_text = f"{cmd_name} {args_str}"
            else:
                cmd_text = cmd_name
            print(f"{i:>4}  [{timestamp}] {cmd_text}")

    def run(self):
        """Runs the main loop of the terminal."""
        while True:
            current_directory = os.getcwd()
            command_input = input(f"MyTerminal:{current_directory}$ ")

            if not command_input.strip():
                continue

            parts = command_input.strip().split()
            cmd_name = parts[0]
            args = parts[1:]

            # Store command with arguments and timestamp in history
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append((cmd_name, args, timestamp))

            if command_input.strip().lower() == 'exit':
                print("Exiting MyTerminal. Goodbye!")
                break

            # Find the command function in our dictionary and call it
            command_func = self.commands.get(cmd_name)
            if command_func:
                command_func(args)
            else:
                print(f"Command not recognized: {cmd_name}")


if __name__ == "__main__":
    # Create an instance of the Terminal and run it
    terminal = Terminal()
    terminal.run()
