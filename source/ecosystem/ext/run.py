from . import EcosystemPlugin
import subprocess
import os
import argparse


class RunExtension(EcosystemPlugin):
    name = 'run'

    def initialize(self, ecosystem):
        self.ecosystem = ecosystem
        self.parser = argparse.ArgumentParser('eco-%s' % self.name)

        self.parser.add_argument('-t', '--tools', nargs='+')
        self.parser.add_argument('-r', '--run', nargs=1)

    def execute(self, args):
        args = self.parser.parse_args(args)
        env = self.get_environment(args)

        env.getEnv(os.environ)
        self.call_process([args.run])

    @staticmethod
    def call_process(arguments):
        if not arguments or arguments[0] is None:
            msg = 'No valid executable command given. Please specify --run.'
            raise RuntimeError(msg)
        subprocess.call(arguments, shell=True)


def register(ecosystem):
    run_extension = RunExtension()
    ecosystem.register_extension(run_extension)