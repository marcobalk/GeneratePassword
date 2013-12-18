import sublime, sublime_plugin, string
from random import sample, choice, randrange

class PasswordCommand(sublime_plugin.TextCommand):
    chars = string.ascii_letters + string.digits
    length = randrange(6, 31)
    
    def run(self, edit):
        p = ''.join(sample(self.chars, self.length))
        for region in self.view.sel():
            self.view.replace(edit, region, p)

class GenerateShortPasswordCommand(PasswordCommand):
    length = 10

class GenerateMediumPasswordCommand(PasswordCommand):
    length = 15

class GenerateLongPasswordCommand(PasswordCommand):
    length = 20

class GenerateShortSecurePasswordCommand(PasswordCommand):
    chars = string.ascii_letters + string.digits + "!@#$%^&*_-+=|/?:;<>~"
    length = 10

class GenerateMediumSecurePasswordCommand(PasswordCommand):
    chars = string.ascii_letters + string.digits + "!@#$%^&*_-+=|/?:;<>~"
    length = 15
    
class GenerateLongSecurePasswordCommand(PasswordCommand):
    chars = string.ascii_letters + string.digits + "!@#$%^&*_-+=|/?:;<>~"
    length = 20