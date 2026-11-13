from prometheus_client import Gauge

ACCOUNT_TIER_SIZE = Gauge("qa_account_tier_size", "accounts per tier", ["tier"])

def tier_of(account):
    return account.get("tier", "basic")
