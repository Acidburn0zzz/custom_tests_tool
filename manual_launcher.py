#!/usr/bin/env python3
# -*- coding:utf-8 -*
#

import json
import logging
import os
import sys

from pprint import pprint

from src.CTTConfig import CTTConfig, OptionError, SectionError
from src.CTTFormatter import CTTFormatter
from src.rootfs_chooser import RootfsChooser, RootfsAccessError
from src.crafter import JobCrafter

class CTTLauncher:
    def __init__(self):
        self.__set_config()
        self.__set_logging()

    def __set_logging(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        paramiko_logger = logging.getLogger("paramiko")
        paramiko_logger.setLevel(logging.WARN)

        requests_logger = logging.getLogger("requests")
        requests_logger.setLevel(logging.WARN)

        handler = logging.StreamHandler()
        if self._cfg['debug']:
            handler.setLevel(logging.DEBUG)
        else:
            handler.setLevel(logging.INFO)

        formatter = CTTFormatter()
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    def __set_config(self):
        ctt_root_location = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.expanduser('~/.cttrc')) as f:
            self._cfg = CTTConfig(f)

        with open(os.path.join(ctt_root_location, "ci_tests.json")) as f:
            self._tests_config = json.load(f)

        with open(os.path.join(ctt_root_location, "boards.json")) as f:
            self._boards_config = json.load(f)
            # Add the name field
            for k,v in self._boards_config.items():
                v['name'] = k
                v['device_type'] = k

        self.crafter = JobCrafter(self._boards_config, self._cfg)

    def launch(self):
        for board in self._cfg['boards']:
            logging.info(board)

            # Handle rootfs, since it's not mandatory
            if 'rootfs' not in self._cfg:
                try:
                    rootfs = RootfsChooser().get_url(self._boards_config[board])
                except RootfsAccessError as e:
                    logging.warning(e)
                    continue
            else:
                rootfs = self._cfg['rootfs']

            if 'tests' in self._cfg:
                # This is needed to generate the test list as a list of
                # dictionaries, as in the `ci_tests.json` file.
                # When a test has been affected to a board, but overrides a
                # default value (the template to use, for example; useful for
                # multinode tests), this makes sure to take that value into
                # account by transforming the test name given in the command line, by
                # the dictionary of the configuration.
                tests = [
                    # Try to look for the test dict in the ci_tests configuration
                    next(
                        iter([e for e in self._tests_config[board]['tests'] if e['name'] == t]),
                        # Default: a simple dict with the name of the test
                        {'name': t}
                    )
                    for t in self._cfg['tests']
                ]
            else:
                logging.critical("  No test asked, aborting")
                sys.exit(1)

            for test in tests:
                logging.debug("  Building job(s) for %s" % test['name'])

                artifacts = {}

                if 'kernel' in self._cfg:
                    artifacts['kernel'] = self._cfg['kernel']

                if 'dtb' in self._cfg:
                    artifacts['dtb'] = self._cfg['dtb']
                elif 'dtb_folder' in self._cfg:
                    artifacts['dtb'] = "%s/%s.dtb" % (self._cfg['dtb_folder'],
                            self._boards_config[board]['dt'])

                if 'modules' in self._cfg:
                    artifacts['modules'] = self._cfg['modules']

                artifacts['rootfs'] = rootfs

                logging.info("  Making %s job" % test['name'])
                job_name = "%s--custom_kernel--%s" % (board, test['name'])
                self.crafter.make_jobs(board, artifacts, test, job_name)

if __name__ == "__main__":
    CTTLauncher().launch()

