from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Button, Footer, Header, Label, Static
from textual import on
import pyfiglet

from quiz.drivingsidequiz import apiCall

def get_country_data():
    country = apiCall()
    return country["name"], country["side"]

class QuizApp(App): 
    CSS_PATH = "userinterface.tcss"

    BINDINGS = [
        ("a", "left", "Left"),
        ("d", "right", "Right"),
    ]

    def __init__(self):
        super().__init__()
        self.score = 0
        self.topscore = 0
        self.country_name = ""
        self.driving_side = ""



    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="score_container"):
            yield Label("Score: 0", id="score_label")
            yield Label("Top Score: 0", id="topscore_label")

        yield Static(pyfiglet.figlet_format("Driving Side?", font="big"), id="question_banner")
        yield Label("", id="country_display")

        with Container(id="button_container"):
            yield Button("Left", id="left")
            yield Button("Right", id="right")
            
        yield Footer()

    def on_mount(self) -> None:
        self.fetch_new_country()

    def fetch_new_country(self) -> None:
        self.country_name, self.driving_side = get_country_data()
        figlet_text = pyfiglet.figlet_format(self.country_name, font="big")
        self.query_one("#country_display", Label).update(figlet_text)

    def update_scores(self) -> None:
        if self.score > self.topscore:
            self.topscore = self.score
        self.query_one("#score_label").update(f"Score: {self.score}")
        self.query_one("#topscore_label").update(f"Top Score: {self.topscore}")

    def action_left(self) -> None:
        if self.driving_side == "left":
            self.score += 1
        else:
            self.score = 0
        self.update_scores()
        self.fetch_new_country()

    def action_right(self) -> None:
        if self.driving_side == "right":
            self.score += 1
        else:
            self.score = 0
        self.update_scores()
        self.fetch_new_country()

    @on(Button.Pressed)
    def handle_answer(self, event: Button.Pressed) -> None:
        if event.button.id == self.driving_side:
            self.score += 1
        else:
            self.score = 0
            
        self.update_scores()
        self.fetch_new_country()

if __name__ == "__main__":
    QuizApp().run()