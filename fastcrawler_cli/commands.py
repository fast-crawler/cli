import typer

import shell

app = typer.Typer()


@app.command("shell")
def shell_command():
    """Enter the FastCrawlerCli Shell."""
    shell.shell()


@app.command("version")
def version_command():
    """Show the FastCrawlerCli version."""
    print("v1.0.0")


if __name__ == "__main__":
    app()
