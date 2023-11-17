# shell.py
import code
import fastcrawler

try:
    import IPython

    ipython_enabled = True
except ImportError:
    ipython_enabled = False


class ShellInterface:
    def __init__(self, banner: str, exit_msg: str):
        self.banner = banner
        self.exit_msg = exit_msg

    def run(self):
        pass


class FastCrawlerCliShell(ShellInterface, code.InteractiveConsole):
    def __init__(
        self,
        locals=None,
        banner="",
        exit_msg="",
        filename="<fastcrawler-cli shell>",
    ):
        ShellInterface.__init__(self, banner, exit_msg)
        code.InteractiveConsole.__init__(self, locals, filename)

    def run(self):
        self.interact(banner=self.banner, exitmsg=self.exit_msg)


class IPythonShell(ShellInterface):
    def __init__(self, locals, banner="", exit_msg=""):
        ShellInterface.__init__(self, banner, exit_msg)
        self.locals = locals

    def run(self):
        IPython.embed(
            user_ns=self.locals,
            banner2=self.banner,
            exit_msg=self.exit_msg,
            colors="Neutral",
            display_banner=True,
        )


class FastCrawlerCli:
    def __init__(self, shell: ShellInterface, shell_locals=None):
        self.shell = shell
        self.shell_locals = shell_locals or {"fastcrawler": fastcrawler}

    def start_shell(self):
        self.shell.run()


def shell():
    banner = "Welcome to the FastCrawlerCli Shell!"
    exit_msg = "Exiting FastCrawlerCli Shell. Goodbye!"

    if ipython_enabled:
        shell = IPythonShell({"fastcrawler": fastcrawler}, banner, exit_msg)
    else:
        shell = FastCrawlerCliShell({"fastcrawler": fastcrawler}, banner, exit_msg)

    cli = FastCrawlerCli(shell)
    cli.start_shell()


if __name__ == "__main__":
    shell()
