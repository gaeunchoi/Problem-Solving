function solution(bandage, health, attacks) {
  let answer = 0;
  const [bandTime, healPerTime, fullHeal] = bandage;
  let [userTime, userHealth] = [0, health];
  for(let i = 0 ; i < attacks.length ; i++){
    let [attackTime, attackDemage] = attacks[i];
    let saveTime = (attackTime - 1) - userTime;
    userHealth += (Math.floor(saveTime / bandTime)) * fullHeal + saveTime * healPerTime;
    userTime = attackTime;

    if(userHealth >= health) userHealth = health;

    userHealth -= attackDemage;
    if(userHealth <= 0) return -1;
  }
  return userHealth;
}