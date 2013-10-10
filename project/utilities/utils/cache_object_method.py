from hashlib import sha1
from django.core.cache import cache

def cache_object_method(seconds=900):
    '''
    Cache the result of a function call for the specified number of seconds,
    using Django's caching mechanism.
    Assumes that the function never returns None (as the cache returns None to indicate a miss), and that the function's result only depends on its parameters.

    Cache key contains the module name, class name and the objects id
    Meaning subsuquent calls to this objects data, even on a different
    request will hit the cache

    Usage:

    @cache_object_method(600)
    def myExpensiveMethod(parm1, parm2, parm3):
        ....
        return expensiveResult
    '''
    def do_cache(func):
        def do(self, *args, **kwargs):
            # build cache key
            key = sha1(str(func.__module__) + str(func.__name__) + str(self.id)).hexdigest()

            # check cache
            result = cache.get(key)
            if result is None:
                result = func(self, *args, **kwargs)
                cache.set(key, result, seconds)
            return result
        return do
    return do_cache