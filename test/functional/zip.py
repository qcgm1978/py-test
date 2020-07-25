import collections
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
            sentinel = object()
            iterators = [iter(it) for it in iterables]
            assert(isinstance(iterators , collections.Iterable))
            while iterators:
                result = []
                for it in iterators:
                    elem = next(it, sentinel)
                    if elem is sentinel:
                        return
                    result.append(elem)
                # self.assertEqual(len(result),2)
                yield tuple(result)