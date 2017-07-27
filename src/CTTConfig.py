from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from configparser import ConfigParser


class BaseError(Exception):
    pass


class OptionError(BaseError):
    pass


class SectionError(BaseError):
    pass


DEFAULT_SECTION = 'ctt'

mandatory_keys = [
    'api_token', # Remove me
    'notify',
    'rootfs_path', # Remove me
    'server',
    'ssh_server',
    'ssh_username',
    'token',
    'username',
    'web_ui_address',
]


class CTTConfig:

    def __init__(self, file, boards, validate=True):
        self.__boards = boards
        self.__config = ConfigParser()

        self.__config.read_file(file)

        if (validate):
            self.__validate_config_file()

        self.__parse_cmdline()

        if (validate):
            self.__validate_cmdline()

    def __parse_cmdline(self):
        parser = ArgumentParser(description='Send custom job to a LAVA server')

        parser.add_argument('-d', '--debug', action='store_true',
                            help='Debug mode')
        parser.add_argument('--no-send', action='store_true',
                            help='Don\'t send the job')
        parser.add_argument('--default-notify', action='store_true', # Remove me
                            help='Use the board configuration mail recipients')
        parser.add_argument('--notify', nargs='+', # Remove me ?
                            help='Mail recipients of the notifications')
        parser.add_argument('-b', '--boards', nargs='+',
                            help='Board to run the test on')
        parser.add_argument('-l', '--list', action='store_true',
                            help='List all the available boards')

        job = parser.add_argument_group('Job handling')
        job.add_argument('--output-dir', default='jobs',
                         help='Path where the jobs will be stored')
        job.add_argument('--rootfs-path', # Remove me
                         help='Path to the prebuilt rootfs images directory')
        job.add_argument('--job-name', help='Name of the job') # Remove me

        job.add_argument('--rootfs', help='Path to your rootfs image')
        job.add_argument('--kernel', help='Path to your kernel image')
        job.add_argument('--dtb', help='Path to your dtb')
        job.add_argument('--dtb-folder', help='Path to your dtb folder')
        job.add_argument('--modules', help='Path to your modules tar.gz')
        job.add_argument('-t', '--tests', nargs='+',
                         help='Tests to run on the board')

        lava = parser.add_argument_group('LAVA server options')
        lava.add_argument('--server', help='LAVA server to send results to')
        lava.add_argument('--username', help='LAVA username')
        lava.add_argument('--token', help='LAVA token')

        artifacts = parser.add_argument_group('Artifacts options') # Remove me
        artifacts.add_argument('--api-token', help='KernelCI API token')
        artifacts.add_argument('--tree', default='mainline',
                               help='KernelCI tree to use')
        artifacts.add_argument('--branch', default='master',
                               help='KernelCI branch to use')
        artifacts.add_argument('--defconfigs', nargs='+',
                               help='KernelCI defconfig to use')
        artifacts.add_argument('--no-kci', action='store_true',
                               help='Ignore KernelCI artifacts')

        ssh = parser.add_argument_group('SSH server options')
        ssh.add_argument('--ssh-server', help='SSH server')
        ssh.add_argument('--ssh-username', help='SSH username')

        self.__cmdline = vars(parser.parse_args())

    def __validate_config_file(self):
        if not self.__config.has_section(DEFAULT_SECTION):
            raise SectionError('Missing %s section' % DEFAULT_SECTION)

    def __validate_cmdline(self):
        # We can always just list the boards
        if self.__cmdline['list']:
            return

        # Validate that we have all the basic options...
        for option in mandatory_keys:
            if not self.__contains__(option):
                raise OptionError('Missing %s option' % option)

        # ... and the options that can only be passed through the command line
        if self.__cmdline['boards'] is None:
            raise OptionError('Missing board')

        for board in self.__cmdline['boards']:
            # Expand all boards to what we know
            if board == 'all':
                self.__cmdline['boards'] = list(self.__boards.keys())
                break

            if board not in self.__boards.keys():
                raise OptionError('Invalid board %s' % board)

    def __getitem__(self, key):
        if key in self.__cmdline:
            val = self.__cmdline[key]
            if val is not None:
                return self.__cmdline[key]

        if (self.__config.has_section(DEFAULT_SECTION) and
            key in self.__config[DEFAULT_SECTION]):
                #
                # The notify key can be multiple values, we
                # should return it as a list
                #
                if key == 'notify':
                    return self.__config[DEFAULT_SECTION][key].split()

                return self.__config[DEFAULT_SECTION][key]

        raise KeyError

    def __contains__(self, key):
        if key in self.__cmdline:
            val = self.__cmdline[key]
            if val is not None:
                return True

        if (self.__config.has_section(DEFAULT_SECTION) and
                key in self.__config[DEFAULT_SECTION]):
            return True

        return False
