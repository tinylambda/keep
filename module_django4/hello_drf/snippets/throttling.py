from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonRateLimit(AnonRateThrottle):
    rate = "10/day"


class UserRateLimit(UserRateThrottle):
    rate = "100/day"
