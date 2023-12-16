from dataclasses import dataclass
from typing import Optional


@dataclass
class ParseTree:
    name: Optional[str] = None
    children: Optional[list["ParseTree"]] = None


def parse(tokens: list[str]) -> ParseTree:
    new_parse_tree, index = _start(0, tokens)
    if index == len(tokens):
        return new_parse_tree
    raise ValueError(f"At the {index + 1} position was expected '+' or '*'")


def _start(index: int, tokens: list[str]) -> tuple[ParseTree, int]:
    parse_node_t, index = _t(index, tokens)
    parse_node_sum, index = _sum(index, tokens)
    return ParseTree("START", [parse_node_t, parse_node_sum]), index


def _sum(index: int, tokens: list[str]) -> tuple[ParseTree, int]:
    if index < len(tokens) and tokens[index] == "+":
        index += 1
        parse_node_t, index = _t(index, tokens)
        parse_node_sum, index = _sum(index, tokens)
        return (
            ParseTree("SUM", [ParseTree("+", None), parse_node_t, parse_node_sum]),
            index,
        )
    return ParseTree("SUM", [ParseTree("eps", None)]), index


def _t(index: int, tokens: list[str]) -> tuple[ParseTree, int]:
    parse_node_token, index = _token(index, tokens)
    parse_node_prod, index = _prod(index, tokens)
    return ParseTree("T", [parse_node_token, parse_node_prod]), index


def _prod(index: int, tokens: list[str]) -> tuple[ParseTree, int]:
    if index < len(tokens) and tokens[index] == "*":
        index += 1
        parse_node_token, index = _token(index, tokens)
        parse_node_prod, index = _prod(index, tokens)
        return (
            ParseTree(
                "PROD", [ParseTree("*", None), parse_node_token, parse_node_prod]
            ),
            index,
        )
    return ParseTree("PROD", [ParseTree("eps", None)]), index


def _token(index: int, tokens: list[str]) -> tuple[ParseTree, int]:
    if index < len(tokens) and tokens[index] == "(":
        index += 1
        parse_node_start, index = _start(index, tokens)
        if index < len(tokens) and tokens[index] == ")":
            return (
                ParseTree(
                    "TOKEN",
                    [ParseTree("(", None), parse_node_start, ParseTree(")", None)],
                ),
                index + 1,
            )
        else:
            raise ValueError(f"At the {index + 1} position was expected ')'")
    elif index < len(tokens) and tokens[index].isdigit():
        index += 1
        return ParseTree("TOKEN", [ParseTree(f"id({tokens[index - 1]})", None)]), index
    raise ValueError(f"At the {index + 1} position was expected digit")


def pretty_print(parse_tree: ParseTree) -> None:
    def pretty_print_recursion(curr_node: ParseTree, count: int):
        print("." * count + curr_node.name)
        if curr_node.children:
            for node in curr_node.children:
                pretty_print_recursion(node, count + 4)

    pretty_print_recursion(parse_tree, 0)
