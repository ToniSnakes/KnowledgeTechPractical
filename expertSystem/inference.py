#### Began modifying this file; needs to be finished for it to work


def forward_chaining(KB, query):
    empty = 0
    print(f"We want to prove {query}")

    while empty != 1:   # most outer loop - just iterates. (like epochs)
        new = []
        for rule in KB["rules"]:    # loop over all rules
            premises, conclusion = rule  # the rule has a premise and a conclusion
            for entity in KB["entities"]:   # loop over all entities (to find if the rule applies)
                flag = 1
                for p in premises:           # check if all the premises are in the KB, to see if the rule applies
                    if (p, entity) not in KB["facts"]:     # rule does not apply
                        flag = 0                            # all premises must be in the KB for you to get the conclusion

                if flag == 1 and (conclusion, entity) not in KB["facts"]:   # all premises are there, and the rule is new
                    new.append((conclusion, entity))                        # new fact found!
        if new == []:   # we didn't find any new fact - stop the inference!
            empty = 1
        else:
            for item in new:
                KB["facts"].append(item)    # add all new facts to the KB

        print(f"\tNew Inferred Facts: {new}")

        if query in KB["facts"]:
            print(f"{query} is TRUE")
            return True

    print(f"{query} is FALSE")
    return False

def backward_chaining(KB, query):
    # check outcome of rules
    print(f"We want to prove {query}")

    goal_list = [query]         # we want to "reason back" from the query!
    empty = 0

    while empty != 1:
        flag = 1

        # for all the goals in the goal list, if we
        # can find them, then we're done

        for subgoal in goal_list:
            if subgoal not in KB["facts"]:
                flag = 0
        if flag == 1:  # we have found all our subgoals and are done!
            print(f"{query} is TRUE")
            return True

        # Else, we need to break it down even further
        for items in goal_list: # for all the goals that we need to find,
            proposition, entity = items       # like (swims, tom)

            subgoal_list = []   # we will put new rules here

            for rule in KB["rules"]:
                premise, conclusion = rule
                if conclusion == proposition:   # so, if we take (swims, tim), and we get (frog -> swims), we want to put the premises as subgoals
                    for p_i in premise:
                        if (p_i, entity) not in goal_list:
                            subgoal_list.append((p_i, entity))  #add all new premises to subgoals


            print(f"\tNew Inferred Subgoals: {subgoal_list}")
            goal_list = subgoal_list        # remove the old goals that you've applied and add the new ones

            if subgoal_list == []: # we didn't find any new subgoals
                empty = 1
                break

    print(f"{query} is FALSE")
    return False

def initialize_knowledge_base():
    KB = {}
    KB["rules"] = [                            #([premise1, premise2, ...], conclusion)
        ([("continuity", False)], ("A", True)),
        (["A", True], ["B", True])
    ]

    KB["facts"] = [
        ("continuity", False)
    ]

    return KB

def forward_chaining_examples(example):
    KB = initialize_knowledge_base()
    forward_chaining(KB, example)
    print()

def backward_chaining_examples(example):
    KB = initialize_knowledge_base()
    backward_chaining(KB, example)
    print()


KB = initialize_knowledge_base()
print("Initial facts")
print(KB["facts"])
print()

examples = [("frog", "tim"),
            ("frog", "tom"),
            ("human", "maria"),
            ("human", "tom"),
            ("frog", "tim"),
            ("swims", "tim"),
            ("bird", "nick"),
            ("flies", "maria"),
            ("flies", "nick"),
            ]


for example in examples:
    #print("FORWARD CHAINING")
    #forward_chaining_examples(example)
    print("BACKWARD CHAINING")
    backward_chaining_examples(example)
    print()
