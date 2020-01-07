#! /usr/bin/env python
from policy_sentry.shared.database import connect_db
from policy_sentry.querying.actions import get_actions_with_access_level


if __name__ == '__main__':
    db_session = connect_db('bundled')
    actions = get_actions_with_access_level(db_session, 's3', 'Permissions management')
    for action in actions:
        print(action)

"""
Output:

    s3:bypassgovernanceretention
    s3:deleteaccesspointpolicy
    s3:deletebucketpolicy
    s3:objectowneroverridetobucketowner
    s3:putaccesspointpolicy
    s3:putaccountpublicaccessblock
    s3:putbucketacl
    s3:putbucketpolicy
    s3:putbucketpublicaccessblock
    s3:putobjectacl
    s3:putobjectversionacl
"""
