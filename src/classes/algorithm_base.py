import os

class AlgorithmBase:

    def __init__(self, console):
        self._name = self.__class__.__name__
        self._console = console

    def _announce(self):
        self._console.log(os.linesep + "***{}***".format(self._name))

    def _log(self, text):
        self._console.log(text)

    def run(self):
        assert False, """run() is a pure virtual method which must be
                         implemented by derived classes."""

