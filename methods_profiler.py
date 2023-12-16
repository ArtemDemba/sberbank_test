import cProfile
import pstats


def profile_method(filename: str):
    def wrapper(method):
        def inner(*args, **kwargs):
            profiler = cProfile.Profile()
            profiler.enable()
            result = method(*args, **kwargs)
            profiler.disable()
            profiler.dump_stats(f'{filename}.prof')
            stats = pstats.Stats(f'{filename}.prof')
            stats.sort_stats('cumulative')
            stats.print_stats()
            return result
        return inner
    return wrapper
