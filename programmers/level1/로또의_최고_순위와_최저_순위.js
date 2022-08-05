function solution(lottos, win_nums) {
  const rank = [6, 6, 5, 4, 3, 2, 1];
  const count_zero = lottos.filter((item) => item === 0).length;
  const answer = win_nums.filter((item) => lottos.includes(item)).length;

  return [rank[count_zero + answer], rank[answer]];
}
