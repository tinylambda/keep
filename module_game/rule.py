# A rule set, how to express
rule = {
    "condition": [
        [
            ("eq", "character.star", 1),
            ("eq", "character.config.quality", 2),
        ],
    ],
    "set_implies_context": [
        [
            ("lte", "character.level", 10),
        ],
    ],
    "set_const_context": {
        "character.extra_add": None,
        "character.need_starexp": 500,
    },
}

RULE_SET = [
    rule,
    rule,
    rule,
]
