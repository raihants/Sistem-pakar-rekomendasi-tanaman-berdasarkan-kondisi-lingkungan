def forward_chaining(facts, rules):
    inferred = set(facts)
    explanations = []
    applied_rules = True

    while applied_rules:
        applied_rules = False
        for rule in rules:
            if rule["if"].issubset(inferred) and rule["then"] not in inferred:
                explanation = f"Rule terpenuhi: {rule['if']} → {rule['then']}"
                print(explanation)
                explanations.append(explanation)
                inferred.add(rule["then"])
                applied_rules = True

    return inferred, explanations