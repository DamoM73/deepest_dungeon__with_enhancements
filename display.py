from rich.console import Console
from rich.panel import Panel

class Display:
    def __init__(self):
        self.console = Console()

    def message(self, message):
        self.console.print(Panel(message, style="bright_blue"))
        
    def converse(self, message):
        self.console.print(Panel(message[1], 
                                 style="yellow", 
                                 title=f"[yellow]{message[0]}[yellow]", 
                                 title_align="left"))
        
    def action(self, message):
        self.console.print(Panel(message, style="bright_green"))
        
    def fight(self, message):
        self.console.print(Panel(message, style="bright_red"))