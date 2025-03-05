from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll
from textual.widgets import Header, Footer, Input, Static
from textual.reactive import reactive
from textual.events import InputSubmitted

class MessageLog(VerticalScroll):
    """A scrolling container for messages."""
    def append_message(self, message: str):
        self.mount(Static(message))
        self.scroll_end()

class AdventureApp(App):
    CSS = """
    Screen {
        layout: horizontal;
    }
    
    .left-panel {
        width: 2fr;
        layout: vertical;
    }
    
    .message-log {
        height: 1fr;
        overflow-y: auto;
        border: solid white;
    }
    
    .input-box {
        height: 3;
        border: solid white;
    }
    
    .right-panel {
        width: 1fr;
        background: yellow;
    }
    """
    
    message_log = reactive(lambda: None)
    
    def compose(self) -> ComposeResult:
        """Create child widgets."""
        self.message_log = MessageLog(classes="message-log")
        return Container(
            Container(
                self.message_log,
                Input(placeholder="Enter command...", classes="input-box"),
                classes="left-panel"
            ),
            Static("Game Info Panel", classes="right-panel")
        )
    
    def on_input_submitted(self, event: InputSubmitted) -> None:
        """Handle user input."""
        command = event.value.strip()
        if command:
            self.message_log.append_message(f"> {command}")
        event.input.value = ""  # Clear input box

if __name__ == "__main__":
    AdventureApp().run()
