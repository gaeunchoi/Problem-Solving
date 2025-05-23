def solution(skill, skill_trees):
    result = 0
    
    for tree in skill_trees:
        filtered_tree = "".join(s for s in tree if s in skill)
        if skill.startswith(filtered_tree):
            result += 1
    return result