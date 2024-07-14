import subprocess

class CommandRunner:
    def __init__(self, working_directory="/var/www/html"):
        self.working_directory = working_directory

    def run_command(self, command, use_sudo=False):
        """Runs a single command in the specified working directory."""
        if use_sudo:
            command = f"sudo {command}"
        process = subprocess.Popen(command, shell=True, cwd=self.working_directory)
        process.communicate()  # Wait for the command to complete

    def run_commands(self, commands):
        """Runs a list of commands in the specified working directory."""
        for command in commands:
            self.run_command(command)

    def configure_git_safe_directory(self):
        """Adds the working directory to Git's safe.directory list."""
        command = f"git config --global --add safe.directory {self.working_directory}"
        self.run_command(command, use_sudo=True)

    def pull_and_reload(self):
        """Pulls from GitHub and reloads Nginx."""
        # Ensure the directory is marked as safe for Git
        self.configure_git_safe_directory()
        
        commands = [
            "sudo git pull",             # Pull the latest changes from the repository
            "sudo systemctl reload nginx"  # Reload Nginx to apply changes
        ]
        self.run_commands(commands)