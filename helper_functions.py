def kmers(seq, k, stride=1):
    """Generate a list of k-mers from a given string.

    Parameters
    ----------
    seq: str
        A string which will be decomposed into k-mers.
    k: int
    stride: int

    Returns
    -------
    List[str]

    Examples
    --------
    >>> kmers("mesenchyme", k=3, stride=1)
    ["mesench", "esenchy", "senchym", "esenchyme"]

    >>> kmers("mesenchyme", k=3, stride=2)
    ["mesench", "senchym"]

    """
    raise NotImplementedError()


def assemble_genome(seqs, k=None, stride=None):
    """Perform genome assembly using the Eulerian path algorithm.

    The overall algorithm should follow the following general structure:
    1. For an input list of sequences, e.g. kmers, construct a DeBruijn graph as
       seen in the lectures.
    2. Find all possible Euerlian paths through the graph, i.e. all possible paths
       which visit each edge exactly once. Your paths should all start from a
       source node with in-degree zero. In case no such node exists, you may use
       the first sequence in the list of input sequences as your starting point.
    3. Decode your obtained paths into sequences, and return a list (or set) of
       unique genome assemblies as strings.

    Parameters
    ----------
    seqs: List[str]
        The list of strings. In this homework, this will always be a list of k-mers.

    k: int, optional
        This parameter is optional, and you may ignore it if you do not need it.
        But, this function will be called with the same `k` as `kmers`, which will
        be used to produce `seqs`. Therefore, make sure you do not remove this
        parameter.
    stride: int, optional
        This parameter is optional, and you may ignore it if you do not need it.
        But, this function will be called with the same `stride` as `kmers`, which will
        be used to produce `seqs`. Therefore, make sure you do not remove this
        parameter.

    Returns
    -------
    Set[str]
        A set (or list if you really want) of unique assemblies for the given `seqs`.

    """
    raise NotImplementedError()
