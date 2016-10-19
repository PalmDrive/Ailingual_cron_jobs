from __future__ import absolute_import

from ailingual_cron.cron_manager import CronManager
import sys
import os


def main():
    cm = CronManager()
    cm.remove_all()

    dir = os.getcwd()
    cm.add_minutely(
        'reset quota',
        True,
        dir + "/task.sh " + dir + "/env/bin/activate " + os.path.join(
            dir, "tasks/quota.py"
        )
    )


if __name__ == '__main__':
    sys.exit(main())
