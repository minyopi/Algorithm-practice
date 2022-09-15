function solution(n, words) {
  let answer = [0, 0];
  for (let i = 1; i < words.length; i++) {
    if (
      words.slice(0, i).includes(words[i]) ||
      words[i][0] !== words[i - 1].charAt(words[i - 1].length - 1)
    ) {
      answer[0] = (i % n) + 1;
      answer[1] = parseInt(i / n) + 1;
      break;
    }
  }
  return answer;
}
