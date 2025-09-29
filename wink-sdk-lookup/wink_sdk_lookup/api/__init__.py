# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_lookup.api.lookup_api import LookupApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_lookup.api.lookup_api import LookupApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
