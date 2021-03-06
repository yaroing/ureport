from enum import Enum


class OrgCache(Enum):
    boundaries = 1
    main_polls = 2
    brick_polls = 3
    other_polls = 4
    flows = 5
    recent_reporters = 6
    all_reporters = 7


def refresh_caches(org, caches):
    from ureport.polls.tasks import refresh_org_flows
    if OrgCache.flows in caches:
        refresh_org_flows.delay(org.pk)
