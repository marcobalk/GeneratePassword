import sublime, sublime_plugin, string
from random import sample, choice, randrange

class PasswordCommand(sublime_plugin.TextCommand):
    secure = False
    chars = string.ascii_letters + string.digits
    secure_chars = chars + "!@#$%^&*_-+=|/?:;<>~"
    length = randrange(6, 31)
    
    def run(self, edit):
        population = self.secure_chars if self.secure else self.chars
        p = ''.join(sample(population, self.length))
        for region in self.view.sel():
            self.view.replace(edit, region, p)

class GenerateShortPasswordCommand(PasswordCommand):
    length = 10

class GenerateMediumPasswordCommand(PasswordCommand):
    length = 15

class GenerateLongPasswordCommand(PasswordCommand):
    length = 20

class GenerateShortSecurePasswordCommand(GenerateShortPasswordCommand):
    secure = True

class GenerateMediumSecurePasswordCommand(GenerateMediumPasswordCommand):
    secure = True
    
class GenerateLongSecurePasswordCommand(GenerateLongPasswordCommand):
    secure = True