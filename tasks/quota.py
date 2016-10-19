from __future__ import absolute_import

import sys
import leancloud


LEANCLOUD_MASTER_KEY = "ywhqmYxpFKTyemJrFl8YYT2j"
LEANCLOUD_APP_ID = "hwB46P8KvcGH258ka0JfnMww-gzGzoHsz"


def main():
    leancloud.init(LEANCLOUD_APP_ID, LEANCLOUD_MASTER_KEY)
    ClientQuota = leancloud.Object.extend('ClientQuota')
    results = ClientQuota.query.find()
    for result in results:
        result.set('access_count', 0)

    ClientQuota.save_all(results)


if __name__ == '__main__':
    sys.exit(main())
