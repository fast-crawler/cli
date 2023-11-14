import code

import fastcrawler

try:
    import IPython

    ipython_enabled = True
except ImportError:
    ipython_enabled = False


class FastCrawlerCliShell(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<fastcrawler-cli shell>"):
        code.InteractiveConsole.__init__(self, locals, filename)

    def run(self):
        banner = "Welcome to the FastCrawlerCli Shell!"
        exit_msg = "Exiting Library Shell. Goodbye!"
        self.interact(banner, exit_msg)

    def do_something(self, arg):
        """
        Sample command that does something.
        Usage: something [arg]
        """
        if arg:
            print("Doing something with arg:", arg)
        else:
            print("Doing something without arg")

    def do_quit(self, arg):
        """
        Exit the library shell.
        Usage: quit
        """
        print("Exiting FastCrawlerCli Shell. Goodbye!")
        return True

    def default(self, line):
        print("Unknown command:", line)


class MyLibrary:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def show_data(self):
        print("Library Data:")
        for item in self.data:
            print(item)


def main():
    shell_locals = {"fastcrawler": fastcrawler}
    shell = FastCrawlerCliShell(shell_locals)

    if ipython_enabled:
        # Start IPython shell with auto-completion
        IPython.embed(
            user_ns=shell_locals,
            banner2="Welcome to the FastCrawlerCli Shell!",
        )
    else:
        shell.run()


if __name__ == "__main__":
    main()
