from dataclasses import dataclass
from typing import TypeVar, Callable, Any, Generic

Key = TypeVar("Key")
Value = TypeVar("Value")

DEFAULT_HASH_SIZE = 8
LOAD_FACTOR_THRESHOLD = 1


@dataclass
class Entry(Generic[Key, Value]):
    key: Key
    value: Value


@dataclass
class Bucket:
    entries: list[Entry]
    bucket_len: int = 0


@dataclass
class HashTable:
    buckets: list[Bucket | None]
    hash_fn: Callable[[Any], int]
    non_empty_buckets: list[Bucket]
    size: int = 0
    total_buckets: int = DEFAULT_HASH_SIZE


def _get_hash(hash_table: HashTable, key: Key) -> int:
    return hash_table.hash_fn(key) % hash_table.total_buckets


def create_hash_table(hash_fn: Callable[[Any], int] = hash) -> HashTable:
    buckets = [None] * DEFAULT_HASH_SIZE
    return HashTable(buckets, hash_fn, list(), total_buckets=DEFAULT_HASH_SIZE)


def delete_hash_table(hash_table: HashTable) -> None:
    del hash_table.buckets[:]
    del hash_table


def _get_node_from_bucket(bucket: list[Entry], key: Key) -> Entry | None:
    for element in bucket:
        if element.key == key:
            return element


def put(hash_table: HashTable, key: Key, value: Value) -> None:
    load_factor = hash_table.size / hash_table.total_buckets
    if load_factor >= LOAD_FACTOR_THRESHOLD:
        enlarge_table(hash_table)
    new_element = Entry(key, value)
    cell = _get_hash(hash_table, key)
    if hash_table.buckets[cell] is None:
        hash_table.buckets[cell] = Bucket([new_element], 1)
        hash_table.non_empty_buckets.append(hash_table.buckets[cell])
        hash_table.size += 1
    else:
        maybe_node = _get_node_from_bucket(hash_table.buckets[cell].entries, key)
        if maybe_node is None:
            hash_table.buckets[cell].entries.append(new_element)
            hash_table.buckets[cell].bucket_len += 1
            hash_table.size += 1
        else:
            maybe_node.value = value


def enlarge_table(hash_table: HashTable) -> None:
    new_buckets = [None] * hash_table.total_buckets * 2
    for bucket in hash_table.non_empty_buckets:
        previous_cell = _get_hash(hash_table, bucket.entries[0].key)
        hash_table.total_buckets *= 2
        new_cell = _get_hash(hash_table, bucket.entries[0].key)
        hash_table.total_buckets //= 2
        new_buckets[new_cell] = hash_table.buckets[previous_cell]
    hash_table.buckets = new_buckets
    hash_table.total_buckets *= 2


def remove(hash_table: HashTable, key: Key) -> Value:
    if not has_key(hash_table, key):
        raise ValueError
    cell = _get_hash(hash_table, key)
    maybe_node = _get_node_from_bucket(hash_table.buckets[cell].entries, key)
    hash_table.size -= 1
    result = maybe_node.value
    print(maybe_node)
    hash_table.buckets[cell].entries.remove(maybe_node)
    hash_table.buckets[cell].bucket_len -= 1
    return result


def get(hash_table: HashTable, key: Key) -> Value:
    if not has_key(hash_table, key):
        raise ValueError
    cell = _get_hash(hash_table, key)
    maybe_node = _get_node_from_bucket(hash_table.buckets[cell].entries, key)
    return maybe_node.value


def has_key(hash_table: HashTable, key: Key) -> bool:
    index = _get_hash(hash_table, key)
    if hash_table.buckets[index] is None:
        return False
    maybe_node = _get_node_from_bucket(hash_table.buckets[index].entries, key)
    if maybe_node is None:
        return False
    return True


def items(hash_table: HashTable) -> list[tuple[Key, Value]]:
    result = []
    for bucket in hash_table.non_empty_buckets:
        for entry in bucket.entries:
            result.append((entry.key, entry.value))
    return result
