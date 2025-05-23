function solution(skill, skill_trees) {
    let result = 0;
    for(const tree of skill_trees){
        const filteredSkill = [...tree].filter(s => skill.includes(s)).join("");
        
        if(skill.startsWith(filteredSkill)) result++;
    }
    return result;
}