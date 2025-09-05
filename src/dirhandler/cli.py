import typer
import os

app = typer.Typer()

@app.command()
def showdir():
    print(os.getcwd())


