import pytest
import blocksci


def iterate_blocks(chain):
    for height in range(0, len(chain)):
        assert chain[height].height == height


def test_access_block(chain, benchmark):
    benchmark(iterate_blocks, chain)


def iterate_transactions(chain):
    for block in chain:
        for idx in range(0, block.tx_count):
            assert block.txes[idx]


def test_access_txes(chain, benchmark):
    benchmark(iterate_transactions, chain)
