import rx


def lowercase():
    def _lowercase(source):
        def subscribe(observer, scheduler=None):
            def on_next(value):
                observer.on_next(value.lower())

            return source.subscribe(
                on_next,
                observer.on_error,
                observer.on_completed,
                scheduler
            )
        return rx.create(subscribe)
    return _lowercase


rx.of('Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon').pipe(
    lowercase()
).subscribe(
    lambda value: print('Received {0}'.format(value))
)
